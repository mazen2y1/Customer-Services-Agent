from db import get_connection

connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")

    orders = cursor.fetchall()

    for order in orders:
        print(order)

except Exception as error:
    print("Database error:", error)

finally:
    if cursor:
        cursor.close()

    if connection and connection.is_connected():
        connection.close()