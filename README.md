# RAG_Chatbot
This project implements a Retrieval-Augmented Generation (RAG)-based chatbot using LangChain, FAISS, and SentenceTransformers.

## Features
- Custom knowledge base powered by FAISS vector search.
- Free and offline embeddings using SentenceTransformers.
- Interaction logs saved persistently for analysis.

## Project Structure
- `chatbot.ipynb`: Jupyter notebook containing the chatbot implementation.
- `knowledge_base.csv`: Dataset with questions and answers.
- `chatbot_logs.txt`: Sample questions and responses.

## Requirements
Install the required dependencies:
```bash
pip install langchain sentence-transformers faiss-cpu
