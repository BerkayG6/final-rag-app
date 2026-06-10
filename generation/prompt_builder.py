from langchain_core.documents import Document

def build_prompt(query: str, documents: list[Document]) -> str:
    context = "\n\n".join([doc.page_content for doc in documents])
    
    prompt = f"""Sen ARMIS Platform onboarding asistanısın. \
Yeni başlayan mühendislerin sorularını yanıtlıyorsun.
Aşağıdaki dokümanlara dayanarak soruyu 3-4 cümle ile cevapla, kısa tutma.
Sadece verilen context'ten cevap üret. Cevabı bilmiyorsan "Bu bilgi dokümanlarda yer almıyor." de.
Her zaman Türkçe cevap ver.
Günlük soru sorulduğu zaman kaynak gösterme.

Context:
{context}

Soru: {query}

Cevap:"""
    
    return prompt