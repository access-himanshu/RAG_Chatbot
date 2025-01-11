import streamlit as st

# Streamlit app title
st.title("RAG-Based Chatbot")

# Input text box
question = st.text_input("Ask a question:")

if question:
    response = qa_chain.run(question)
    st.write(f"Answer: {response}")
