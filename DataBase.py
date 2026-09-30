from supabase import create_client
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url,key)
supabase = init_connection()

def fetch_order(order_id: str):
    response = (
        supabase
        .table("orders")
        .select("*")
        .eq("order_id", order_id)
        .maybe_single()
        .execute()
    )

    order = response.data

    if order is None:
        return None

    return order


def update_order_status(order_id: str, status: str) -> bool:
    response = (
        supabase
        .table("orders")
        .update({
            "status": status
        })
        .eq("order_id", order_id)
        .execute()
    )

    return len(response.data) > 0


def update_refund_status(order_id: str, eligible: bool) -> bool:
    response = (
        supabase
        .table("orders")
        .update({
            "eligible_for_refund": eligible
        })
        .eq("order_id", order_id)
        .execute()
    )

    return len(response.data) > 0


def insert_ticket(order_id: str, issue: str):
    response = (
        supabase
        .table("tickets")
        .insert({
            "order_id": order_id,
            "issue": issue,
            "status": "open"
        })
        .execute()
    )

    ticket = response.data[0]

    return {
        "ticket_id": ticket["ticket_id"],
        "order_id": ticket["order_id"],
        "issue": ticket["issue"],
        "status": ticket["status"]
    }