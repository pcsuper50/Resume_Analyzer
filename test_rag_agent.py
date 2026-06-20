from app.rag.rag_engine import create_vectorstore
from app.agents.rag_agent import rag_agent

text = """
LangGraph is a framework for building AI agents.
RAG stands for Retrieval Augmented Generation.
"""

vectorstore = create_vectorstore(text)

state = {
    "vectorstore": vectorstore,
    "question": "What is LangGraph?"
}

print(rag_agent(state))