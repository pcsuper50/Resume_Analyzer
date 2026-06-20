from app.rag.rag_engine import ask_rag


def chat_with_rag(vectorstore, user_query):

    answer = ask_rag(
        vectorstore,
        user_query
    )

    return answer