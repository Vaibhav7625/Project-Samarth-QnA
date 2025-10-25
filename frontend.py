import streamlit as st
import requests

st.set_page_config(page_title="Project Samarth", page_icon="🌾")
st.title("🌾 Project Samarth: Intelligent Q&A System")
st.write("Ask data-driven questions about India's agricultural and climate trends!")

API_URL = "http://127.0.0.1:8000/ask"

if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_query = st.chat_input("Ask your question...")

if user_query:
    # Display user message
    st.session_state.history.append({"role": "user", "content": user_query})
    with st.spinner("Thinking..."):
        response = requests.post(API_URL, json={"query": user_query})
        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "No answer")
            code = data.get("generated_code", "")
            st.session_state.history.append({"role": "assistant", "content": answer, "code": code})
        else:
            st.error("Backend error! Please check your FastAPI server.")

# Display chat history
for msg in st.session_state.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])
            with st.expander("🧠 Show generated code"):
                st.code(msg["code"], language="python")