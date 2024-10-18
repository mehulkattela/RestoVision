from langchain_driver import get_few_shot_db_chain
import streamlit as st

# Set the background image for the app's main container. 
# The image covers the full viewport width (100vw) and height (100vh).
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-photo/mexican-food_23-2148024760.jpg?w=2000&t=st=1729272708~exp=1729273308~hmac=5b24c31f06c3827af9df93b63a386a94991a776bed0a6ed0f764ebcdf038a03c");
    background-size: 100vw 100vh;  # Ensures the image covers the entire background
    background-position: center;  
    background-repeat: no-repeat;  # Prevents the background image from repeating
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)  # Inject the CSS to set the background image


# Style the input text box. Changes background color, text color, and ensures transparency of containers.
input_style = """
<style>
input[type="text"] {
    background-color: #646670;  # Darker background for the input box
    color: #a19eae;  # Light text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;  # Makes the input container background transparent
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;  # Makes the overall app container transparent
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)  # Inject the CSS for input styling


# Display the app's title
st.title("RestoVision - Data insights for restaurants")

# Take input from the user (the restaurant-related question)
question = st.text_input("Question: ")

if question:
    # Call the chain function to process the question and run the database query
    chain = get_few_shot_db_chain()
    result = chain.run(question)

    # Display the answer to the user
    st.header("Answer:")
    st.write(result)
