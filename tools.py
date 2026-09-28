from langchain.tools import tool
from db import fetch_order

@tool
def get_order(order_id: str) -> dict:
    """Get order details using the order ID."""

    order = fetch_order(order_id)

    if order is None:
        return {
            "success": False,
            "error": "Order not found",
            "order_id": order_id,
        }

    return {
        "success": True,
        **order,
    }

"""
@tool
def get_order(order_id:str) -> dict:
    Get order details using the order ID
    order = ORDERS.get(order_id)
    if order is None:
        return{"error":"order not found"}
    return{
        "order_id":order_id,
        **order,
    }
"""

@tool
def check_shipping(order_id:str) -> dict:
    """Check shipping status and expected delivery date."""
    order = fetch_order(order_id)
    if order is None:
        return{"error":"order not found"}
    return{
        "order_id" : order_id,
        "shipping_status": order['shipping_status'],
        "expected_delivery" : order['expected_delivery'],
    }

@tool
def cancel_order(order_id:str) -> dict:
    """Cancel an order if it has not been shipped."""
    order = fetch_order(order_id)
    if order is None:
        return{"succes":False , "error":"order not found"}
    if order["status"] != "processing":
        return{
            "success":False,
            "error":"order cannot be cancelled"
        }
    order["status"] = "cancelled"
    return{
        "success":True,
        "order_id":order_id,
        "error":"order cancelled"
    }

@tool
def refund_order(order_id:str) -> dict:
    """Refund an order if it is eligible."""
    order = fetch_order(order_id)

    if order is None:
        return{
            "error":"order not found"
        }
    if not order["eligible_for_refund"]:
        return{
            "success":False,
            "error":"Order is not eligible for refund"
        }
    order["eligible_for_refund"] = False
    return{
        "succes":True,
        "order_id":order_id,
        "refund_amount": order["total"]
    }

@tool
def create_ticket(order_id: str, issue: str) -> dict:
    """Create a support ticket for an unresolved issue."""

    ticket = {
        "ticket_id": f"T-{len(TICKETS) + 1:03d}",
        "order_id": order_id,
        "issue": issue,
        "status": "open"
    }

    TICKETS.append(ticket)

    return ticket