# 🌍 Multilingual Sentiment Analysis App (Text + Voice)

A Streamlit web application that allows users to provide feedback in **any language** (via **text** or **voice**), automatically detects the input language, translates it to English, and performs **sentiment analysis** using a multilingual BERT model.

---

## 🚀 Features

- 🌐 **Supports multiple languages** including English, Telugu, Hindi, Tamil, Kannada, Bengali, Marathi, Malayalam, Gujarati, Urdu, etc.
- 🎙️ **Voice input support** (with language-based recognition)
- 🔄 **Auto-translation** of typed or spoken feedback to English
- 🤖 **Sentiment Analysis** using HuggingFace's `nlptown/bert-base-multilingual-uncased-sentiment`
- ✅ Detects **Positive**, **Neutral**, or **Negative** feedback
- 🧠 Based on **Transformers**, `deep-translator`, and `langdetect`

---

## 📷 Demo

![Demo Screenshot](screenshots/demo_ui.png)  
*(Add your own screenshot or screen recording here)*

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/) — For interactive UI
- [Transformers (HuggingFace)](https://huggingface.co/) — Sentiment model
- [Deep Translator](https://pypi.org/project/deep-translator/) — For translation
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — For voice input
- [langdetect](https://pypi.org/project/langdetect/) — Language detection

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/HarishSdagam8/multilingual-sentiment-analysis.git
cd multilingual-sentiment-analysis

python -m venv translate-env
# Windows
translate-env\Scripts\activate
# Linux/Mac
source translate-env/bin/activate

pip install -r requirements.txt

streamlit run app.py
.
├── app.py                       # Main Streamlit app
    ├── utils.py                    # Language detection helper
    ├── translation_api.py         # Deep Translator wrapper
├── requirements.txt           # Python dependencies
├── README.md
└── screenshots/               # (Optional) For demo image or GIF

🌍 Supported Languages
This app currently supports input in:

English

Telugu

Hindi

Tamil

Kannada

Bengali

Marathi

Malayalam

Urdu

Gujarati
(More languages can be added easily.)

📖 How it Works
User selects input language (e.g., Telugu)

User gives feedback (via text or microphone)

App:

Detects or uses selected language

Translates feedback to English

Applies sentiment analysis using a multilingual BERT model

Displays sentiment result and confidence score

📊 Model Details
🤖 Model: nlptown/bert-base-multilingual-uncased-sentiment

✅ Trained on multiple languages

⭐ Predicts rating from 1 to 5, mapped to sentiment

✅ Future Improvements
Add support for Romanized input detection (e.g., "iroju food baagundi" → "ఇరోజు ఫుడ్ బాగుంది")

Add real-time transliteration as user types

Save feedbacks to a database (for analytics)

Export feedback reports (CSV or PDF)

🙌 Acknowledgements
Hugging Face Transformers

Deep Translator

Streamlit Community

Google SpeechRecognition API

📝 License
This project is licensed under the MIT License.

