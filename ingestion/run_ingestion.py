import os
from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_chunks

DATA_DIR = "./data"

if __name__ == "__main__":
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(DATA_DIR, filename)
            print(f"İşleniyor: {filename}")
            text = load_pdf(filepath)
            chunks = chunk_text(text)
            embed_chunks(chunks, filepath)
            print(f"  {len(chunks)} chunk kaydedildi")
    print("Tamamlandı.")