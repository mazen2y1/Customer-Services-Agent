# Customer Services Agent 🤖

An AI-powered customer support agent built with **Python, LangChain, Google Gemini, Supabase, and Streamlit**.

The agent understands customer requests and uses tools to interact with the database and handle common customer service tasks.

## Features

* Get order details
* Check shipping status
* Cancel orders
* Process refunds
* Create support tickets

## Files

* **`app.py`** — Streamlit chat interface.
* **`Agent.py`** — AI agent and Gemini configuration.
* **`tools.py`** — Customer service tools used by the agent.
* **`DataBase.py`** — Handles Supabase database operations.
* **`.streamlit/secrets.toml`** — Stores API keys and configuration.

## How It Works

```text
Customer
   ↓
Streamlit
   ↓
Gemini Agent
   ↓
Tools
   ↓
Supabase Database
   ↓
Response
```