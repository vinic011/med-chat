from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_db(splits, embeddings = OpenAIEmbeddings()):
    db = FAISS.from_documents(splits, embeddings)
    retriever = db.as_retriever()
    return retriever