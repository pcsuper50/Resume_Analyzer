from app.rag.rag_engine import ask_rag


def rag_agent(state):

    vectorstore = state["vectorstore"]

    question = state["question"]

    answer = ask_rag(
        vectorstore,
        question
    )

    return {
        "rag_answer": answer
    }