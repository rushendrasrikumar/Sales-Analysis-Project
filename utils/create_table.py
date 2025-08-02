from db_mysql import get_mysql_conn

def create_sales_table():
    conn = get_mysql_conn()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100),
            quantity INT,
            price FLOAT,
            sale_date DATE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("'sales' table created successfully.")

if __name__ == "__main__":
    create_sales_table()
