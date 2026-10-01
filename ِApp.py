import streamlit as st
from Agent import chat

st.set_page_config(
    page_title="CSA DEMO",
    page_icon=r"data/assistant.png",
    layout="wide"
)

st.title("Customer Services Agent")
st.markdown("https://github.com/mazen2y1/Customer-Services-Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("wait"):
            try:
                response = chat(prompt)
                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:
                st.error("Something went wrong. Please try again")
                print(f"Agent Error: {e}")