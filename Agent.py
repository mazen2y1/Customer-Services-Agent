from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from tools import get_order , check_shipping , cancel_order , refund_order , create_ticket
import streamlit as st

GOOGLE_API_KEY= st.secrets["GOOGLE_API_KEY"]

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0,
    googgle_api_key=GOOGLE_API_KEY
)
system_prompt = """
You are a customer support agent.

- Investigate the customer's issue using the tools.
- Retrieve order details before taking order actions.
- Check shipping for delivery-related issues.
- Cancel orders only when appropriate.
- Refund orders only when the tool confirms eligibility.
- Create a support ticket for unresolved issues.
- Never claim an action succeeded unless the tool confirms it.
- If the customer requests an action that is not allowed,
  explain the reason and offer an appropriate alternative.
- Be polite, concise, and honest.
"""

agent = create_agent(
    model=model,
    tools = [
    get_order,
    check_shipping,
    cancel_order,
    refund_order,
    create_ticket,
    ],
    system_prompt=system_prompt,
)

def chat(message: str) -> str:
    result = agent.invoke({
        "messages": [
            HumanMessage(content=message)
        ]
    })
    content = result["messages"][-1].content
    if isinstance(content,str):
        return content
    if isinstance(content ,list):
        return " \n".join(
            block['text']
            for block in content
            if isinstance(block,dict)
            and block.get("type") == "text"
        )
    return str(content)