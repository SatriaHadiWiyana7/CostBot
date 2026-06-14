import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()

# Konfigurasi UI Halaman Streamlit
st.set_page_config(page_title="CostBot", page_icon="🍜", layout="centered")
st.title("CostBot: Asisten Anak Kos")
st.caption("Ngobrol santai seputar budget, resep akhir bulan, dan produktivitas kuliah!")

# Mengambil API Key dari environment variables (.env)
api_key = os.getenv("GEMINI_API_KEY")

# Pengecekan Keamanan API Key
if not api_key:
    st.error("🚨 API Key tidak ditemukan! Pastikan file .env sudah ada di folder yang sama dengan app.py dan berisi GEMINI_API_KEY=kunci_rahasiamu.")
    st.stop() # Menghentikan proses agar tidak error beruntun

# Konfigurasi Gemini API dengan key yang ditemukan
genai.configure(api_key=api_key)

# Definisi System Prompt (Karakter & Role KosBot)
SYSTEM_PROMPT = """
Kamu adalah KosBot, asisten virtual setia untuk mahasiswa dan anak kos. 
Gaya bahasamu santai, ramah, dan gaul (gunakan sapaan seperti 'Bro' atau 'Sis'). 
Tugas utamamu: membantu berhemat, ngasih ide resep murah akhir bulan, dan manajemen waktu nugas. 
Jika user bahas uang, selalu tanya sisa budgetnya dan ingatkan untuk nabung. 
Jawaban harus singkat, padat, realistis untuk dompet mahasiswa, dan langsung pada intinya.
"""

# Konfigurasi Model Gemini (Menggunakan gemini-1.5-flash)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT,
    generation_config=genai.GenerationConfig(
        temperature=0.7, 
    )
)

# Inisialisasi Chat Session di Streamlit Session State (Untuk Memory)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.welcome_message = "Halo Sis/Bro! KosBot di sini. Ada yang bisa dibantu? Mau curhat soal dompet tipis atau butuh resep tanggal tua?"

# Tampilkan pesan pembuka
with st.chat_message("assistant"):
    st.markdown(st.session_state.welcome_message)

# Tampilkan history percakapan sebelumnya
for message in st.session_state.chat_session.history:
    # Gemini menggunakan role 'user' dan 'model'
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Input Box untuk User
if prompt := st.chat_input("Ketik pesanmu di sini (contoh: Uangku sisa 20 ribu, bisa makan apa?)..."):
    
    # Tampilkan pesan user di UI
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim pesan ke model Gemini dan tangani kemungkinan error
    with st.chat_message("assistant"):
        try:
            # Mengirim pesan dengan efek streaming (muncul perlahan)
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            
            # Fungsi generator untuk membaca aliran teks
            def stream_generator():
                for chunk in response:
                    yield chunk.text
                    
            # Tampilkan ke layar
            st.write_stream(stream_generator)
            
        except Exception as e:
            # Jika API error (misal internet putus / kuota habis), tampilkan ini:
            st.error(f"Waduh, koneksi ke otak KosBot agak gangguan nih: {e}")