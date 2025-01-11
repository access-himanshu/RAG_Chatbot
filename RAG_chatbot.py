# Loop for chatbot
while True:
    question = input("Ask a question (type 'exit' to quit): ")
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = qa_chain.run(question)
    print(f"Answer: {response}")
with open(log_path, "w") as log_file:
    while True:
        question = input("Ask a question (type 'exit' to quit): ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = qa_chain.run(question)
        print(f"Answer: {response}")
import streamlit as st

# Streamlit app title
st.title("RAG-Based Chatbot")

# Input text box
question = st.text_input("Ask a question:")

if question:
    response = qa_chain.run(question)
    st.write(f"Answer: {response}")
