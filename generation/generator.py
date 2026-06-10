from retrieval.retriever import Retriever
from generation.llm import LLMClient
from generation.prompt_builder import build_prompt

class Generator:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMClient()

    def answer(self, query: str) -> str:
        documents = self.retriever.retrieve(query)
        prompt = build_prompt(query, documents)
        response = self.llm.generate(prompt)

        sources = list(set([
            doc.metadata.get("source", "Bilinmiyor") 
            for doc in documents
        ]))
    
        return {
            "answer": response,
            "sources": sources
        }
    def answer_stream(self, query: str):
        documents = self.retriever.retrieve(query)
        prompt = build_prompt(query, documents)
        
        sources = list(set([
            doc.metadata.get("source", "Bilinmiyor")
            for doc in documents
        ]))
        
        stream = self.llm.generate_stream(prompt)
        return stream, sources
if __name__ == "__main__":
    generator = Generator()
    result = generator.answer("Servisler nasıl deploy ediliyor?")
    print("Cevap:", result["answer"])
    print("Kaynaklar:", result["sources"])