from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.utils.gemini_helper import get_gemini_response

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vectorstore(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    vectorstore = FAISS.from_texts(
        chunks,
        embeddings
    )

    return vectorstore


def ask_rag(vectorstore, question):

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are a helpful AI assistant.

    Use ONLY the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    return get_gemini_response(prompt)