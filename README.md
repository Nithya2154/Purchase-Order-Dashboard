📦 Purchase Order Dashboard

A Purchase Order Analysis Dashboard built using Python, Pandas, and Streamlit.
This project allows businesses to analyze purchase order data and generate key insights, trends, and KPIs through an interactive dashboard.

🚀 Features

Total number of orders & total purchase value

Purchase value by Supplier, Product, and Region

Top suppliers and top products by quantity

Monthly & daily purchase trends

Average order value per supplier

Orders by status (Pending, Shipped, Delivered)

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

Average order value per Supplier

Orders by status

High-value orders highlight

Daily purchase trend

Average unit price per product

Filtered orders by status and region

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

3️⃣ Open in browser
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

Business-focused KPIs and insights

Understanding of purchase trends, supplier performance, and high-value orders

🎯 Use Cases

Portfolio project for data analysts

Interview preparation for Python/Pandas roles

Purchase / sales analytics dashboards

Prototype for business intelligence solutions

📄 License

This project is open-source and available under the MIT License.
