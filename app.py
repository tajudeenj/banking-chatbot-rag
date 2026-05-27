"""
Banking Chatbot with RAG
========================
LangChain + Pinecone + GPT-4 + Streamlit
Author: Tajudeen Jalaudin
"""

import streamlit as st
import os

# In production: pip install langchain openai pinecone-client streamlit
# from langchain.chains import RetrievalQA
# from langchain_openai import AzureOpenAI, AzureOpenAIEmbeddings
# from langchain_pinecone import PineconeVectorStore

st.set_page_config(page_title="Banking RAG Assistant", page_icon="🏦", layout="wide")

# --- Mock Knowledge Base ---
BANKING_KB = {
    "account balance": "You can check your account balance via the mobile app, internet banking, or by visiting any branch.",
    "loan application": "To apply for a loan, visit our website or nearest branch with your Emirates ID, salary certificate, and last 3 months' bank statements.",
    "credit card": "Our credit cards offer up to 5% cashback, zero annual fees for the first year, and worldwide acceptance.",
    "swift transfer": "International transfers use SWIFT. Typical processing time is 1-3 business days. UAE IBAN required for local transfers.",
    "kyc": "KYC (Know Your Customer) verification is required for all accounts. Submit Emirates ID and proof of address at any branch.",
    "fraud": "If you suspect fraud, immediately call our 24/7 hotline at 800-BANK or block your card via the mobile app.",
}

def mock_rag_response(query: str) -> dict:
    """Mock RAG response — replace with real LangChain + Pinecone in production."""
    query_lower = query.lower()
    for key, answer in BANKING_KB.items():
        if any(word in query_lower for word in key.split()):
            return {"answer": answer, "source": key, "confidence": 0.85}
    return {
        "answer": "I don't have specific information about that. Please contact our support team at 800-BANK.",
        "source": "fallback",
        "confidence": 0.0
    }

# --- UI ---
st.title("🏦 Banking RAG Assistant")
st.caption("Powered by Azure OpenAI + LangChain + Pinecone | Built by Tajudeen Jalaudin")

with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("In production mode, connect:\n- Azure OpenAI\n- Pinecone Vector DB\n- Core Banking API")
    st.markdown("**Demo Mode:** Using mock knowledge base")
    st.markdown("---")
    st.markdown("**Skills:** RAG • LangChain • GPT-4 • Pinecone")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Banking Assistant. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask about your account, loans, transfers..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            result = mock_rag_response(prompt)
            response = result["answer"]
            st.write(response)
            if result["confidence"] > 0:
                st.caption(f"📚 Source: {result['source']} | Confidence: {result['confidence']:.0%}")

    st.session_state.messages.append({"role": "assistant", "content": response})
