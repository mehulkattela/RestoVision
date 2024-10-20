# RestoVision: AI-Driven Restaurant Insights

**LangChain, OpenAI, HuggingFace, Chroma, SQL, Streamlit, Docker**

## Summary
RestoVision is an AI-powered application designed to assist restaurants in analyzing operational and financial data to make informed decisions. The application converts natural language queries into SQL, retrieves relevant data, and presents actionable insights.

![image](https://github.com/user-attachments/assets/2d836e22-c0f5-4ac3-aaae-255c74863735)

## Features
- **LLM Integration for SQL Query Generation:** Utilizes OpenAI's `gpt-3.5-turbo-instruct` model to generate and optimize SQL queries from user-provided natural language inputs, enabling seamless interaction with the restaurant database.
- **Few-Shot Learning with Semantic Similarity:** Implements few-shot learning using `SemanticSimilarityExampleSelector` to dynamically select the most relevant examples from a vector store (Chroma) for better query accuracy and natural language understanding.
- **Vector Embedding for Enhanced Query Context:** Uses `HuggingFaceEmbeddings` for sentence transformers to create vector representations of examples, improving the model’s ability to understand and retrieve contextually relevant data from the restaurant database.
- **Chroma Vector Store for Efficient Example Storage:** Manages and stores vector embeddings of few-shot examples using Chroma, enabling fast and scalable similarity searches for prompt enhancement.
- **Custom SQL Prompt Engineering:** Builds custom SQL prompts using `PromptTemplate` and `FewShotPromptTemplate` to structure input and output, guiding the language model to effectively interact with the SQL database and generate insightful responses.
- **Real-Time Restaurant Data Insights:** Provides real-time answers to operational and financial questions related to the restaurant, including performance metrics such as sales, inventory, and customer traffic, by directly querying the MySQL-based `restaurant_db`.
- **Database Chain for Seamless LLM-Database Interaction:** Leverages `SQLDatabaseChain` to handle seamless communication between the language model and the MySQL database, allowing for precise query generation and data retrieval.
- **Streamlit-based Interactive UI:** Implements a user-friendly interface using Streamlit, allowing restaurant managers to input questions and receive real-time insights in an intuitive format, with customizable background and input styling.
- **Embeddable and Containerized Application:** Supports Docker containerization via a `Dockerfile`, allowing the application to be easily deployed and scaled across different environments.



## Project Structure

The project follows a modular structure for clarity and maintainability. Here's a breakdown of the folder structure:

```
RestoVision/
│
├── restaurant.sql           # Contains the SQL commands for setting up the restaurant database, including table schemas and initial data.
│
├── langchain_driver.py      # Configures the LangChain and OpenAI models, handling database chains and few-shot learning to generate SQL queries from natural language input.
│
├── few_shots.py             # Includes a list of few-shot learning examples used for improving query context and accuracy.
├── main.py                  # The core Streamlit app that takes user input, processes the query, and returns insights based on database analysis.
├── Dockerfile               # Defines the steps required to create a Docker container for the application, ensuring it runs consistently in any environment.
├── requirements.txt         # Lists all the Python libraries and their versions required to run the project, allowing easy setup of the project environment.
├── README.md                # Project documentation providing an overview, features, installation steps, and usage instructions.
└── .gitignore               # Prevents unnecessary or sensitive files from being tracked in the Git repository.
```

### **Database Structure**

The **RestoVision** application utilizes a SQL database, named `restaurant_db`, which stores and manages essential restaurant-related data. The database contains various tables to handle menu items, inventory, sales, employees, suppliers, expenses, and customer feedback.

#### **Tables:**

##### **1. `menu_items`**
- `menu_item_id`: Unique ID for each menu item (Primary Key)
- `name`: Name of the menu item
- `category`: Category of the menu item (Starters, Main Course, Desserts, Beverages)
- `cost_price`: Cost price of the menu item
- `selling_price`: Selling price of the menu item
- `is_available`: Availability status of the menu item (Boolean)

##### **2. `inventory`**
- `inventory_id`: Unique ID for each inventory item (Primary Key)
- `item_name`: Name of the inventory item
- `category`: Category of the inventory item (Vegetables, Spices, Grains, Beverages)
- `stock_quantity`: Current stock level of the item
- `reorder_level`: Minimum stock quantity before reordering
- `unit`: Unit of measurement (kg, liters, units)
- `supplier_id`: Reference to the supplier (Foreign Key)
- `last_order_date`: Date of the last order
- `next_reorder_date`: Date when the item should be reordered

##### **3. `suppliers`**
- `supplier_id`: Unique ID for each supplier (Primary Key)
- `name`: Name of the supplier
- `contact`: Contact information of the supplier
- `item_supplied`: List of items supplied by the supplier
- `payment_due`: Amount due for payment to the supplier

##### **4. `sales`**
- `sale_id`: Unique ID for each sale (Primary Key)
- `sale_date`: Date of the sale
- `sale_time`: Time of the sale
- `order_id`: Unique ID for each order
- `menu_item_id`: Reference to the menu item sold (Foreign Key)
- `quantity`: Number of items sold in the sale
- `price_per_unit`: Price of each item sold
- `total`: Total price of the sale
- `payment_method`: Method of payment (Cash, Card, Online)

##### **5. `employees`**
- `employee_id`: Unique ID for each employee (Primary Key)
- `name`: Name of the employee
- `role`: Employee's role (Chef, Waiter, Cashier, Manager)
- `salary`: Employee's salary
- `hire_date`: Date when the employee was hired
- `hours_worked`: Total hours worked by the employee
- `leave_balance`: Leave balance of the employee

##### **6. `expenses`**
- `expense_id`: Unique ID for each expense (Primary Key)
- `expense_date`: Date of the expense
- `category`: Expense category (Rent, Utilities, Marketing, Maintenance)
- `amount`: Amount spent on the expense
- `description`: Description of the expense

##### **7. `customer_feedback`**
- `feedback_id`: Unique ID for each customer feedback (Primary Key)
- `feedback_date`: Date of the feedback
- `customer_name`: Name of the customer providing feedback
- `menu_item_id`: Reference to the menu item for which the feedback is provided (Foreign Key)
- `rating`: Customer rating (1-5 scale)
- `comments`: Customer's feedback comments

---

### **Relationships:**
- `sales` table is linked to the `menu_items` table through the `menu_item_id` foreign key to track which items were sold.
- `inventory` table is linked to the `suppliers` table via the `supplier_id` foreign key to manage supplier details for each inventory item.
- `customer_feedback` table is linked to the `menu_items` table via the `menu_item_id` foreign key to record feedback on specific items. 


## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mehulkattela/RestoVision.git
   ```

2. Build and run the Docker container:
   ```bash
   docker build -t restovision .
   docker run -p 8501:8501 restovision
   ```

3. Access the application in your browser:
   ```
   http://localhost:8501
   ```

---

## Usage

Simply enter your questions in natural language, and the system will generate SQL queries and return insights on restaurant performance, sales, inventory, and customer feedback.

---

## Contributions

Contributions are welcome! Please feel free to open an issue or submit a pull request with any changes or improvements.

---
