from dotenv import load_dotenv
import os
from groq import Groq


class LLMClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"

    def generate(self, query):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": query}],
            max_tokens=512
        )
        return response.choices[0].message.content

    def generate_stream(self, query):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": query}],
            max_tokens=512,
            stream=True
        )
        for chunk in response:
            piece = chunk.choices[0].delta.content
            if piece is not None:
                yield piece
        
    
if __name__ == "__main__":
    llm = LLMClient()
    print(llm.generate("Merhaba, kendini tanıt."))