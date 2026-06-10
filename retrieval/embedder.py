from langchain_huggingface import HuggingFaceEmbeddings

class QueryEmbedder:
    """Class to handle embedding of query text using HuggingFaceEmbeddings."""
    
    def __init__(self, model_name: str = "BAAI/bge-m3"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)

    def embed(self, query: str) -> list[float]:
        """Embed the query text and return the embedding vector."""
        return self.embeddings.embed_query(query)