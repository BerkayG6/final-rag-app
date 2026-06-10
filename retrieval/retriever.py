from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from retrieval.bm25 import BM25Retriever
from retrieval.semantic import SemanticRetriever
from retrieval.hybrid import HybridRetriever
import os

class Retriever:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        chroma_path = os.path.join(base_dir, "chroma_db")

        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3", multi_process=False)
        self.vectorstore = Chroma(
            collection_name="pdf_chunks",
            persist_directory=chroma_path,
            embedding_function=embeddings
        )
        result = self.vectorstore.get()
        self.documents = [
             Document(page_content=text, metadata=meta) 
             for text, meta in zip(result["documents"], result["metadatas"])
        ]

        self.bm25_retriever = BM25Retriever(self.documents)
        self.semantic_retriever = SemanticRetriever(self.vectorstore)
        self.hybrid_retriever = HybridRetriever(self.semantic_retriever, self.bm25_retriever)
        
    def retrieve(self, query: str, top_k: int = 5) -> list[Document]:
        """Retrieve relevant chunks from the vectorstore based on the query using hybrid retrieval."""
        return self.hybrid_retriever.retrieve(query, top_k=top_k)
        

