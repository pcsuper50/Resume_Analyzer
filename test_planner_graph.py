from app.graph.planner_graph import planner_graph
from app.rag.rag_engine import create_vectorstore

vectorstore = create_vectorstore("""
LangGraph is a framework for building AI agents.
RAG stands for Retrieval Augmented Generation.
""")

result = planner_graph.invoke({
    "query": "Explain LangGraph",
    "question": "What is LangGraph?",
    "vectorstore": vectorstore
})

print(result)