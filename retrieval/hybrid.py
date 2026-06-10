from sentence_transformers import CrossEncoder
from langchain_core.documents import Document
from retrieval.semantic import SemanticRetriever
from retrieval.bm25 import BM25Retriever

class HybridRetriever:
    """Class to handle hybrid retrieval of relevant chunks from the vectorstore."""
    
    def __init__(self, semantic_retriever: SemanticRetriever, bm25_retriever: BM25Retriever):
        self.semantic_retriever = semantic_retriever
        self.bm25_retriever = bm25_retriever
        self.cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def retrieve(self, query: str, top_k: int = 5) -> list[Document]:
        """Retrieve relevant chunks from the vectorstore based on the query using both semantic and BM25 retrieval."""
        semantic_results = self.semantic_retriever.retrieve(query, top_k=top_k*2)
        bm25_results = self.bm25_retriever.retrieve(query, top_k=top_k*2)
        
        seen = set()
        unique_results = []
        for doc in semantic_results + bm25_results:
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                unique_results.append(doc)
                
        # Rerank combined results using cross-encoder
        reranked_results = sorted(unique_results, key=lambda doc: self.cross_encoder.predict([(query, doc.page_content)])[0], reverse=True)
        
        return reranked_results[:top_k]