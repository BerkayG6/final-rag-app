import streamlit as st 
from generation.generator import Generator

# Generator'ı bir kez oluştur, cache'de tut (Singleton)
@st.cache_resource
def load_generator():
    return Generator()

with st.spinner("Sistem yükleniyor..."):
    generator = load_generator()

st.header("ARMIS Platform Onboarding Asistanı")
st.caption("Merhaba! ARMIS projesi hakkında merak ettiğiniz her şeyi sorabilirsiniz.")


# Sayfa ilk açıldığında boş mesaj listesi oluştur
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları ekrana bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        # Asistan mesajlarında kaynakları göster
        if message["role"] == "assistant":
            st.caption(f"Kaynaklar: {', '.join(message['sources'])}")

# Kullanıcı soru yazıp gönderince çalışır
if query := st.chat_input("Sorunuzu yazın... Örn: Servisler nasıl deploy ediliyor?"):
    
    # Kullanıcı mesajını geçmişe ekle ve ekranda göster
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Asistan cevabını üret ve ekrana bas
    with st.chat_message("assistant"):
        # Spinner: retrieval sürerken göster
        with st.spinner("Yanıt üretiliyor..."):
            stream, sources = generator.answer_stream(query)
        # Stream: cevabı kelime kelime ekrana bas, tamamlanmış metni döndürür
        response = st.write_stream(stream)
        # Kaynakları cevabın altında göster
        st.caption(f"Kaynaklar: {', '.join(sources)}")

    # Asistan mesajını geçmişe ekle
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "sources": sources
    })