from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
from app.core.config import COHERE_API_KEY, COHERE_BASE_URL

def get_embeddings():
    return CohereEmbeddings(
        cohere_api_key=COHERE_API_KEY,   # lowercase
        base_url=COHERE_BASE_URL, 
        model="embed-v4.0",
        input_type="search_document"
    )

def store_chunks(chunks,index_name):
    embedding = get_embeddings()
    vectorstore= Chroma(
        collection_name = index_name,
        embedding_function= embedding,
        persist_directory = "./chroma_db"
    )
    vectorstore.add_documents(chunks)
    return vectorstore

def query_embeddings():
    return CohereEmbeddings(
        cohere_api_key=COHERE_API_KEY,   # lowercase
        base_url=COHERE_BASE_URL, 
        model="embed-v4.0",
        input_type="search_query"
    )

def search_chunks(query,index_name):
    embedding = query_embeddings()
    vectorstore= Chroma(
        collection_name = index_name,
        embedding_function= embedding,
        persist_directory = "./chroma_db"
    )
    results = vectorstore.similarity_search(query, k=5)
    return results
