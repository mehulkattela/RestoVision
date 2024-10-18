# RestoVision: AI-Driven Restaurant Insights

**LangChain, OpenAI, HuggingFace, Chroma, SQL, Streamlit, Docker**

## Summary
RestoVision is an AI-powered chatbot designed to assist restaurants in analyzing operational and financial data to make informed decisions. The application converts natural language queries into SQL, retrieves relevant data, and presents actionable insights.

![image](https://github.com/user-attachments/assets/2d836e22-c0f5-4ac3-aaae-255c74863735)

## Features
- **Financial Analysis:** Provides insights into revenue, costs, and profit margins.
- **Operational Metrics:** Tracks key performance indicators (KPIs) like table turnover rates and customer footfall.
- **Data Visualization:** Presents data in intuitive charts and graphs for easier comprehension.
- **Custom Reports:** Generates tailored reports based on user-defined parameters.
- **User-Friendly Interface:** Allows easy navigation and interaction for restaurant owners and managers.
- **Data-Driven Recommendations:** Offers actionable suggestions based on data trends to optimize operations.
- **SQL Query Generation:** Natural language inputs are converted into SQL queries using LangChain and OpenAI for complex data analysis.
- **Efficient Data Retrieval:** HuggingFace embeddings and Chroma vector store for fast and accurate query results.
- **Few-Shot Learning:** Enhances SQL query generation with limited examples for improved precision.
Streamlit Interface: User-friendly UI for seamless interaction and business insights.
Docker: Containerized for easy deployment and scalability across cloud platforms.
Logging & Monitoring: Ensure reliable performance and application health.
GitHub: Version control and collaboration for streamlined development.
Comprehensive Documentation: Guides for both users and developers to utilize and maintain the system.


## Project Structure

The project follows a modular structure for clarity and maintainability. Here's a breakdown of the folder structure:

```
RestoVision/
│
├── restaurant.sql                           # Folder containing SQL database and data files
│
├── langchain_driver.py                         # Folder for model-related scripts (HuggingFace, LangChain, etc.)
│
├── few_shots.py                        # Folder for miscellaneous scripts
├── main.py
├── Dockerfile                      # Dockerfile to containerize the application
├── requirements.txt                # List of Python dependencies
├── README.md                       # Project documentation (this file)
├── .gitignore                      # Git ignore file to exclude unnecessary files
└── restovision.db                  # SQLite database containing restaurant data (auto-generated)
```

### Explanation of Key Directories:
- **data/**: Contains raw data files that are loaded into the SQL database for analysis.
- **models/**: Handles machine learning and natural language processing, including embeddings and SQL query generation.
- **scripts/**: Contains utility scripts for data pre-processing and setting up the database.
- **app/**: Contains the main application logic and UI components, primarily using Streamlit.

---

## Database Structure

The RestoVision application uses a SQL database to store and manage critical restaurant data, including:

### Tables:
1. **Sales**
   - `sale_id`: Unique ID for each sale (Primary Key)
   - `item_id`: Reference to the item sold (Foreign Key)
   - `quantity`: Number of items sold
   - `total_price`: Total price of the sale
   - `sale_date`: Date and time of the sale

2. **Inventory**
   - `item_id`: Unique ID for each inventory item (Primary Key)
   - `item_name`: Name of the inventory item
   - `quantity_in_stock`: Current stock level
   - `supplier`: Supplier information
   - `last_restocked`: Date of last restocking

3. **Employee Performance**
   - `employee_id`: Unique ID for each employee (Primary Key)
   - `employee_name`: Name of the employee
   - `role`: Employee role (e.g., Server, Chef)
   - `performance_rating`: Employee performance rating (1-5 scale)
   - `last_performance_review`: Date of the last review

4. **Customer Feedback**
   - `feedback_id`: Unique ID for each feedback entry (Primary Key)
   - `customer_name`: Name of the customer providing feedback
   - `feedback_text`: The feedback provided by the customer
   - `rating`: Customer rating (1-5 scale)
   - `date`: Date of the feedback

### Relationships:
- **Sales** are linked to **Inventory** through the `item_id`, keeping track of items sold and stock levels.
- **Employee Performance** is a standalone table tracking reviews and performance data.
- **Customer Feedback** links feedback to the overall service, helping track customer satisfaction.

---

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
