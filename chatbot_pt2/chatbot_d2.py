from ollama import chat
import streamlit as st


st.set_page_config(page_title = "Llama App", page_icon = "👽")
st.title("Llamabot - Here to talk !!")


personality = " your friendly doctor named Llama. Answer kindly. Answer in one line"

if "history" not in st.session_state:
    st.session_state.history = [{"role" : "system", "content": personality}]

with st.chat_message("assistent"):
    st.write("Hello! i'm Llama . Ask something to start conversation...")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type something....")
if question:
    st.session_state.history.append({"role": "user","content": question})

    with st.chat_message("user"):
        st.write(question)