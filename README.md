📦 Purchase Order Dashboard

A Purchase Order Analysis Dashboard built using Python, Pandas, and Streamlit. This project allows businesses to analyze purchase order data and generate key insights, trends, and KPIs through an interactive dashboard.

🚀 Features

Display total number of orders and total purchase value

Analyze purchase value by Supplier, Product, and Region

Identify top suppliers and top products by quantity

Visualize monthly & daily purchase trends

Calculate average order value per supplier

Track orders by status (Pending, Shipped, Delivered)

Highlight high-value orders dynamically

Filter orders based on Status and Region

Interactive and user-friendly Streamlit interface

🛠️ Technologies Used

Python – Core programming

Pandas – Data cleaning, aggregation, and analysis

Streamlit – Dashboard visualization and interactivity

JSON – Data source for purchase orders

📊 Dashboard KPIs

Total number of orders

Total purchase value

Purchase value by Supplier

Purchase value by Product

Purchase value by Region

Top Suppliers by purchase value

Top Products by quantity ordered

Orders with quantity above threshold

Monthly purchase trend

Daily purchase trend

Average order value per Supplier

Average unit price per product

Orders by status

High-value orders highlight

Filtered orders by status and region

▶️ How to Run the Project

Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Open in browser

http://localhost:8501

📌 Sample Data Format (purchase.json)
{
  "OrderID": 101,
  "Date": "2025-01-01",
  "Supplier": "Supplier A",
  "Product": "Laptop",
  "Quantity": 5,
  "UnitPrice": 50000,
  "Region": "North",
  "Status": "Delivered"
}

💡 Learning Outcomes

Real-world data cleaning and aggregation using Pandas

Using groupby, filtering, and datetime operations

Building interactive dashboards with Streamlit

Understanding business-focused KPIs and insights

Analyzing purchase trends, supplier performance, and high-value orders

🎯 Use Cases

Portfolio project for data analysts

Interview preparation for Python / Pandas roles

Purchase / sales analytics dashboards

Prototype for business intelligence solutions

📄 License

This project is open-source and available under the MIT License.
