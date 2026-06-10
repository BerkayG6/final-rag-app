from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os

def embed_chunks(chunks, filepath):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
    
    vectorstore = Chroma(
        collection_name="pdf_chunks",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )
    
    filename = os.path.basename(filepath)
    documents = [
        Document(
            page_content=chunk,
            metadata={"source": filename}
        )
        for chunk in chunks
    ]
    
    vectorstore.add_documents(
        documents=documents,
        ids=[f"{filepath}_chunk_{i}" for i in range(len(chunks))]
    )
    return vectorstore