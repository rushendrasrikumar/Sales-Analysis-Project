import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sales_db"
)

# Load data into DataFrame
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)
conn.close()

# Total sales revenue
df['total'] = df['quantity'] * df['price']
print(" Total Revenue:", df['total'].sum())

# Top-selling products
product_sales = df.groupby('product_name')['total'].sum().sort_values(ascending=False)
print("\n Top Selling Products:\n", product_sales)

# Monthly sales
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.to_period('M')
monthly_sales = df.groupby('month')['total'].sum()

# Plot - Top Products
product_sales.plot(kind='bar', title='Top Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# Plot - Monthly Sales
monthly_sales.plot(kind='line', marker='o', title='Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
