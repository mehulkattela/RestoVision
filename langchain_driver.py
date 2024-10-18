from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from few_shots import few_shots
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
import pinecone
import os
import chromadb


from dotenv import load_dotenv

#Load enviroment variables (API KEY)
load_dotenv()

#Configure llm model (OPENAI)
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    max_retries=2,
    api_key=os.environ["OPENAI_API_KEY"],
)

#Configure database (SQLDatabase)
def get_few_shot_db_chain():
    db_user = "root"
    db_password = "5136029850"
    db_host = "localhost"
    db_name = "restaurant_db"
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info = 3)
    #Configure embeddings of your choice (Huggingface used)
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2")
    #Convert the few_shots list of dictionaries into a string with only dict values stored in to_vectorize list
    to_vectorize = [" ".join(examples.values()) for examples in few_shots]
    #Create a vector store (Chroma)
    vector_store = Chroma.from_texts(to_vectorize, embeddings, metadatas = few_shots)
    #Clear the system chache for the client
    chromadb.api.client.SharedSystemClient.clear_system_cache()
    #initializing similarity search using SemanticSimilarityExampleSelector
    example_selector = SemanticSimilarityExampleSelector(vectorstore = vector_store, k=2)
    # Define a prompt template with placeholders for Question, SQLQuery, SQLResult, and Answer.
    # This template will structure how the question and result will be formatted.
    example_prompt = PromptTemplate(
    input_variables = ["Question", "SQLQuery", "SQLResult", "Answer"],
    template = "\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )
    # Create a few-shot prompt template, which selects example prompts to provide context
    # for the model. It uses `example_selector` to pick examples and the above `example_prompt`
    # for formatting. Prefix and suffix provide additional context for the prompt.
    few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = _mysql_prompt,         # Introduction to the prompt that guides the model on what to expect
    suffix = PROMPT_SUFFIX,         # Closing part of the prompt, usually guiding how the answer should be structured
    input_variables = ["input", "table_info", "top_k"] )
    # Build an SQL database chain, which uses the language model (llm) to interact with
    # the database (db). The few-shot prompt guides the query generation and response process.
    chain = SQLDatabaseChain.from_llm(llm, db, verbose = True, prompt=few_shot_prompt)
    # Return the chain, which is ready to take user input, generate SQL queries, and fetch results.
    return chain