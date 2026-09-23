from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.services.embedding_service import store_chunks
def split_doc(content,index_name, chunk_size=500, chunk_overlap=50):
    documents = [Document(page_content=content)]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )

    chunked_docs = text_splitter.split_documents(documents)
    store_chunks(chunked_docs,index_name)
    return chunked_docs


