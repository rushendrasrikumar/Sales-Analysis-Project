from utils.db_mysql import get_mysql_conn
from datetime import date

def insert_sample_data():
    sales_data = [
        ("Laptop", 3, 75000.0, date(2024, 1, 15)),
        ("Smartphone", 5, 30000.0, date(2024, 2, 10)),
        ("Headphones", 10, 1500.0, date(2024, 3, 5)),
        ("Monitor", 2, 12000.0, date(2024, 3, 22)),
        ("Keyboard", 7, 700.0, date(2024, 4, 12)),
    ]

    conn = get_mysql_conn()
    cursor = conn.cursor()

    query = "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, sales_data)

    conn.commit()
    cursor.close()
    conn.close()
    print(" Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()
