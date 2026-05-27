# 💬 Banking Chatbot with RAG

> LangChain + Pinecone + GPT-4 + Streamlit  
> Built by [Tajudeen Jalaudin](https://github.com/Tajudeenj)

## Overview

A conversational banking assistant using **RAG (Retrieval-Augmented Generation)**. Answers customer queries about accounts, loans, SWIFT transfers, KYC, and fraud using internal banking knowledge bases.

## Quick Start

```bash
git clone https://github.com/Tajudeenj/banking-chatbot-rag.git
cd banking-chatbot-rag
pip install -r requirements.txt
streamlit run app.py
```

## Production Architecture

```
User Query → Streamlit UI
     → LangChain RetrievalQA
     → Pinecone Vector Search (top-k docs)
     → Azure GPT-4 (answer with context)
     → Response with source citation
```

## Related Skills

`LangChain` `Pinecone` `GPT-4` `RAG` `Streamlit` `Azure OpenAI` `Banking AI` `Conversational AI`

---
*Part of the [Tajudeen Jalaudin](https://github.com/Tajudeenj) Banking Tech Portfolio*
