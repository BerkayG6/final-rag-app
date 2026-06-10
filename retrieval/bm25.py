from rank_bm25 import BM25Okapi
from langchain_core.documents import Document

class BM25Retriever:
    """Class to handle BM25 retrieval of relevant chunks from the vectorstore."""
    
    def __init__(self, documents: list[Document]):
        self.documents = documents
        self.tokenized_corpus = [doc.page_content.split() for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def retrieve(self, query: str, top_k: int = 5) -> list[Document]:
        """Retrieve relevant chunks from the vectorstore based on the query."""
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [self.documents[i] for i in top_indices]
