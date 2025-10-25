import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate Sales Data (Sheet 1)
np.random.seed(42)
num_rows = 100

dates = [datetime(2024, 1, 1) + timedelta(days=int(x)) for x in np.random.randint(0, 365, num_rows)]
regions = np.random.choice(['North', 'South', 'East', 'West'], num_rows)
salespeople = np.random.choice(['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona'], num_rows)
products = np.random.choice(['Laptop', 'Tablet', 'Smartphone', 'Headphones', 'Monitor'], num_rows)
units_sold = np.random.randint(1, 50, num_rows)
unit_price = np.random.randint(100, 2000, num_rows)
total_revenue = units_sold * unit_price

sales_data = pd.DataFrame({
    'Date': dates,
    'Region': regions,
    'Salesperson': salespeople,
    'Product': products,
    'Units Sold': units_sold,
    'Unit Price': unit_price,
    'Total Revenue': total_revenue
})

# Generate Customer Info (Sheet 2)
num_customers = 50
customer_data = pd.DataFrame({
    'Customer ID': [f"CUST{i:03}" for i in range(1, num_customers + 1)],
    'Customer Name': np.random.choice(
        ['John', 'Sarah', 'Michael', 'Emma', 'Chris', 'Olivia', 'James', 'Sophia', 'Daniel', 'Ava'], num_customers),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], num_customers),
    'Age': np.random.randint(18, 65, num_customers),
    'Gender': np.random.choice(['Male', 'Female'], num_customers),
    'Satisfaction Score': np.random.randint(1, 10, num_customers)
})

# Create practice guide (Sheet 3)
tasks = [
    "1️⃣ Calculate the total revenue per salesperson using a Pivot Table.",
    "2️⃣ Find the top 3 products by total revenue.",
    "3️⃣ Create a bar chart showing total revenue by region.",
    "4️⃣ Use VLOOKUP or XLOOKUP to match customer region with sales region.",
    "5️⃣ Calculate the average units sold per product.",
    "6️⃣ Find which month had the highest total revenue.",
    "7️⃣ Add a conditional formatting rule to highlight sales above $20,000.",
    "8️⃣ Create a line chart showing sales trend over time."
]
practice_guide = pd.DataFrame({"Excel Practice Tasks": tasks})

# Save to Excel
excel_path = "Excel_Practice_for_Data_Analyst.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    sales_data.to_excel(writer, sheet_name="Sales Data", index=False)
    customer_data.to_excel(writer, sheet_name="Customer Info", index=False)
    practice_guide.to_excel(writer, sheet_name="Practice Guide", index=False)

print(f"✅ Excel file created successfully: {excel_path}")
