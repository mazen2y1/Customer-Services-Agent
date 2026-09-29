import os
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH)

print("ENV PATH:", ENV_PATH)
print("ENV FILE EXISTS:", ENV_PATH.exists())
print("PASSWORD LOADED:", bool(os.getenv("DB_PASSWORD")))

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database="customer_support",
        port=3306,
    )

def fetch_order(order_id: str):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT *
            FROM orders
            WHERE order_id = %s
        """

        cursor.execute(query, (order_id,))
        order = cursor.fetchone()

        if order is None:
            return None

        order["expected_delivery"] = (
            order["expected_delivery"].isoformat()
            if order["expected_delivery"]
            else None
        )

        order["total"] = str(order["total"])
        order["eligible_for_refund"] = bool(
            order["eligible_for_refund"]
        )

        return order

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def update_order_status(order_id: str, status: str) -> bool:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            UPDATE orders
            SET status = %s
            WHERE order_id = %s
        """

        cursor.execute(query, (status, order_id))
        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        raise

def update_refund_status(order_id: str, eligible: bool) -> bool:
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE orders
            SET eligible_for_refund = %s
            WHERE order_id = %s
        """

        cursor.execute(query, (eligible, order_id))
        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        if connection and connection.is_connected():
            connection.rollback()
        raise

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

def insert_ticket(order_id: str, issue: str):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO tickets (order_id, issue)
            VALUES (%s, %s)
        """

        cursor.execute(query, (order_id, issue))
        connection.commit()

        return {
            "ticket_id": cursor.lastrowid,
            "order_id": order_id,
            "issue": issue,
            "status": "open",
        }

    except Exception:
        if connection and connection.is_connected():
            connection.rollback()
        raise

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()