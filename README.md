# Personal Document Assistant — RAG Chatbot

Kendi PDF dokümanlarınla konuşmanı sağlayan uçtan uca bir RAG (Retrieval-Augmented Generation) uygulaması. Streamlit arayüzü üzerinden sorularını sorabilir, kaynakları görebilirsin.

## Özellikler

- PDF dokümanlarını otomatik işleme ve indeksleme
- Semantik + BM25 hibrit arama (daha iyi retrieval kalitesi)
- Reranking ile cevap kalitesini artırma
- Groq API üzerinden hızlı LLM yanıtı
- Her cevabın kaynağını gösteren citation sistemi
- Streamlit tabanlı sohbet arayüzü

## Mimari

```
final-rag-app/
├── ingestion/
│   ├── loader.py          # PDF yükleme
│   ├── chunker.py         # Metni parçalara bölme
│   ├── embedder.py        # Embedding vektörleri üretme
│   └── run_ingestion.py   # İngestion pipeline'ını çalıştır
├── retrieval/
│   ├── semantic.py        # Semantik (vektör) arama
│   ├── bm25.py            # BM25 anahtar kelime araması
│   ├── hybrid.py          # İki yöntemi birleştiren hybrid search
│   └── retriever.py       # Reranking + ana retriever
├── generation/
│   ├── llm.py             # Groq API bağlantısı
│   ├── prompt_builder.py  # Prompt şablonu
│   └── generator.py       # Cevap üretimi
├── data/                  # PDF dosyaların buraya
├── chroma_db/             # Vektör veritabanı (otomatik oluşur)
├── app.py                 # Streamlit uygulaması
└── test_pipeline.py       # Pipeline testi
```

## Kurulum

### 1. Repoyu klonla

```bash
git clone https://github.com/berkayg6/final-rag-app.git
cd final-rag-app
```

### 2. Sanal ortam oluştur ve aktif et

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

### 4. Ortam değişkenlerini ayarla

`.env.example` dosyasını kopyala ve Groq API anahtarını ekle:

```bash
cp .env.example .env
```

`.env` dosyasını düzenle:

```
GROQ_API_KEY=your_groq_api_key_here
```

> Groq API anahtarını [console.groq.com](https://console.groq.com) adresinden ücretsiz alabilirsin.

### 5. PDF'leri ekle

Kendi PDF dosyalarını `data/` klasörüne koy.

### 6. Dokümanları indeksle

```bash
python ingestion/run_ingestion.py
```

### 7. Uygulamayı başlat

```bash
streamlit run app.py
```

Tarayıcında `http://localhost:8501` adresine git.

## Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Embedding | sentence-transformers (BGE-M3) |
| Vektör DB | ChromaDB |
| Keyword Search | BM25 |
| LLM | Groq API (Llama) |
| Arayüz | Streamlit |


## Nasıl Çalışır?

1. **Ingestion:** PDF'ler yüklenir, chunklara bölünür ve embedding vektörlerine dönüştürülür, ChromaDB'ye kaydedilir.
2. **Retrieval:** Soru geldiğinde hem semantik hem BM25 araması yapılır, sonuçlar reranker ile sıralanır.
3. **Generation:** En iyi chunk'lar LLM'e context olarak verilir, kaynak gösterilerek cevap üretilir.



---

*Bu proje, kişisel NLP öğrenim sürecinin bir parçası olarak geliştirilmiştir.*
