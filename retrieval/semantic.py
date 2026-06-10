from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from retrieval.embedder import QueryEmbedder

class SemanticRetriever:
    """Class to handle semantic retrieval of relevant chunks from the vectorstore."""
    
    def __init__(self, vectorstore: Chroma):
        self.vectorstore = vectorstore
        self.query_embedder = QueryEmbedder()

    def retrieve(self, query: str, top_k: int = 5) -> list[Document]:
        """Retrieve relevant chunks from the vectorstore based on the query."""
        query_embedding = self.query_embedder.embed(query)
        results = self.vectorstore.similarity_search_by_vector(query_embedding, k=top_k)
        return results