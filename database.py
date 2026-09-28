ORDERS = {
    "1001": {
        "customer_id": "C001",
        "status": "shipped",
        "shipping_status": "delayed",
        "expected_delivery": "2026-09-30",
        "total": 1500,
        "eligible_for_refund": False,
    },
    "1002": {
        "customer_id": "C002",
        "status": "delivered",
        "shipping_status": "delivered",
        "expected_delivery": "2026-09-25",
        "total": 800,
        "eligible_for_refund": True,
    },
    "1003": {
        "customer_id": "C003",
        "status": "processing",
        "shipping_status": "not_shipped",
        "expected_delivery": "2026-10-02",
        "total": 2500,
        "eligible_for_refund": True,
    },
}

TICKETS = []