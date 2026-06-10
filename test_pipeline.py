from ingestion.embedder import load_vectorstore
from retrieval.semantic import SemanticRetriever
from retrieval.bm25 import BM25Retriever
from retrieval.hybrid import HybridRetriever

if __name__ == '__main__':
    vectorstore = load_vectorstore()
    all_docs = vectorstore.similarity_search("", k=100)
    query = "Servisler nasıl deploy ediliyor?"

    semantic = SemanticRetriever(vectorstore)
    print("=== SEMANTIC ===")
    for doc in semantic.retrieve(query, top_k=3):
        print(doc.page_content[:100])

    bm25 = BM25Retriever(all_docs)
    print("\n=== BM25 ===")
    for doc in bm25.retrieve(query, top_k=3):
        print(doc.page_content[:100])

    hybrid = HybridRetriever(semantic, bm25)
    print("\n=== HYBRID ===")
    for doc in hybrid.retrieve(query, top_k=3):
        print(doc.page_content[:100])