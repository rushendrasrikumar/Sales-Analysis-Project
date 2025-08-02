import mysql.connector

def get_mysql_conn():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",             # Change if needed
        password="root", # Use your MySQL root password
        database="sales_db"
    )

# TEST: Connect and print version
if __name__ == "__main__":
    conn = get_mysql_conn()
    print("Connected to MySQL successfully!")
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()
    print("MySQL version:", version)
    conn.close()
