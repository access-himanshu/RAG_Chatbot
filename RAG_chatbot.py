from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from langchain.vectorstores import FAISS
from langchain.docstore.in_memory import InMemoryDocstore
from langchain.schema import Document

# Loading dataset
df = pd.read_csv(dataset_path)
texts = [f"Question: {row['Question']} Answer: {row['Answer']}" for _, row in df.iterrows()]

model = SentenceTransformer('all-MiniLM-L6-v2')

embedding_vectors = model.encode(texts)

# Converting embeddings to NumPy array
embedding_array = np.array(embedding_vectors, dtype='float32')

index = faiss.IndexFlatL2(embedding_array.shape[1])
index.add(embedding_array)

documents = {i: Document(page_content=text) for i, text in enumerate(texts)}

docstore = InMemoryDocstore(documents)

def embedding_function(text):
    return model.encode([text])[0]

# Creating FAISS vectorstore
vectorstore = FAISS(index=index, docstore=docstore, index_to_docstore_id=list(documents.keys()), embedding_function=embedding_function)

print("Vector store successfully created!")
from langchain.chains import RetrievalQA
from langchain.llms.fake import FakeListLLM

# Initializing the fake LLM 
responses = [row["Answer"] for _, row in df.iterrows()]
fake_llm = FakeListLLM(responses=responses)

qa_chain = RetrievalQA.from_chain_type(llm=fake_llm, retriever=vectorstore.as_retriever())

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
