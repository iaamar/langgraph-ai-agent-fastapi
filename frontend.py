import streamlit as st
import requests

st.set_page_config(layout="wide", page_title="LangGraph AI Agent")
st.title("🦜🕸️ LangGraph AI Agent")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    system_prompt = st.text_area("Define your AI agent", height=70, placeholder="Type system prompt here...")
    MODEL_NAMES_GROQ = ["deepseek-r1-distill-llama-70b", "llama-3.3-70b-versatile"]
    MODEL_NAMES_OPEN_AI = ["gpt-40-mini"]
    model_provider = st.radio("Select Provider", ["Groq", "OpenAI"])

    if model_provider == "Groq":
        model_name = st.radio("Select Model", MODEL_NAMES_GROQ)
    else:
        model_name = st.radio("Select Model", MODEL_NAMES_OPEN_AI)

    user_query = st.text_area("Enter Prompt", height=80, placeholder="Ask anything...")
    allow_search = st.checkbox("Allow Search")

    # payload
    user_input = {
        "model_name": model_name,
        "model_provider": model_provider,
        "system_prompt": system_prompt,
        "messages": user_query.split("\n"),
        "allow_search": allow_search
    }

    if st.button("Submit"):
        if user_query.strip():
            # Connect backend with frontend
            response = requests.post("http://127.0.0.1:8000/chat_agent", json=user_input)
            response_data = response.json()
            st.session_state.response_data = response_data

with col2:
    if "response_data" in st.session_state:
        st.subheader("Response")
        st.write(st.session_state.response_data)