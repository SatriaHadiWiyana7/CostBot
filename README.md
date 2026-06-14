# 🍜 CostBot (KosBot) - Asisten Pintar Anak Kos 

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-AI-orange.svg)

**CostBot** adalah chatbot AI interaktif berbasis antarmuka web sederhana yang dirancang khusus sebagai "asisten bertahan hidup" bagi mahasiswa dan anak kos. Menggunakan ketajaman **Google Gemini API**, bot ini bertindak sebagai perencana keuangan mikro, penasihat resep *low-budget*, dan pengingat produktivitas kuliah.

---

## 🎯 Use Case & Parameter Kreatif

Proyek ini dibuat untuk memenuhi tugas akhir pembuatan chatbot AI dengan kriteria berikut:

* **Use Case:** *Personal Productivity & Lifestyle Assistant*. Bot membantu mengelola alokasi dana harian yang sangat ketat dan memberikan ide resep makanan akhir bulan.
* **Gaya Bahasa (Tone):** Santai, ramah, suportif, dan menggunakan bahasa pergaulan mahasiswa (gaul/relatable).
* **Fitur Memory:** Menggunakan `st.session_state` pada Streamlit, sehingga bot mampu mengingat konteks percakapan (seperti sisa *budget* pengguna) selama sesi berlangsung tanpa harus diulang-ulang.
* **Parameter LLM:** * `model`: `gemini-2.5-flash` (cepat dan efisien).
    * `temperature`: `0.7` (Keseimbangan antara jawaban yang solutif/logis dan kreativitas saat memberikan ide resep).

---

## 🛠️ Tech Stack
* **Bahasa:** Python 3.10
* **UI Framework:** Streamlit
* **LLM Engine:** Google Generative AI (Gemini)
* **Environment:** Miniconda / Conda

---

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan CostBot di komputermu sendiri menggunakan Miniconda:

**1. Clone Repositori**
```bash
git clone [https://github.com/USERNAME_GITHUB_KAMU/CostBot.git](https://github.com/USERNAME_GITHUB_KAMU/CostBot.git)
cd CostBot