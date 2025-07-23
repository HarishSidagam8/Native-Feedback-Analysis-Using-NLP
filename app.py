#**************************************************** Streamlit APP

import streamlit as st
import speech_recognition as sr
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from deep_translator import GoogleTranslator


# Load Sentiment Model
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


def map_sentiment_label(label):
    if '1' in label or '2' in label:
        return 'Negative'
    elif '3' in label:
        return 'Neutral'
    else:
        return 'Positive'


def translate_to_english(text, source_lang):
    try:
        return GoogleTranslator(source=source_lang, target='en').translate(text)
    except Exception as e:
        st.write(f"Translation error: {e}")
        return text


def get_voice_input(language_code):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please speak.")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language_code)
        return text
    except:
        return ""


# Streamlit App
st.title("🌐🗣️ Native Feedback Analysis🔍 ")

# Language Selection for Feedback

language_options = {
    "English": ("en", "en-US"),
    "Telugu": ("te", "te-IN"),
    "Hindi": ("hi", "hi-IN"),
    "Tamil": ("ta", "ta-IN"),
    "Kannada": ("kn", "kn-IN"),
    "Malayalam": ("ml", "ml-IN"),
    "Marathi": ("mr", "mr-IN"),
    "Gujarati": ("gu", "gu-IN"),
    "Bengali": ("bn", "bn-IN"),
    "Punjabi": ("pa", "pa-IN"),
    "Urdu": ("ur", "ur-IN")
}

selected_language = st.selectbox("Select Feedback Language:", list(language_options.keys()))
source_lang_code, speech_lang_code = language_options[selected_language]

# Input Mode
mode = st.radio("Select Input Mode:", ["Type Text", "Speak (Voice Input)"])

# Capture Input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if mode == "Type Text":
    st.session_state.user_input = st.text_area(f"Type your feedback in {selected_language} (Romanized OK):", height=200)
else:
    if st.button("Record Voice"):
        st.session_state.user_input = get_voice_input(speech_lang_code)
        st.write(f"🗣 You said: *{st.session_state.user_input}*")



# Analyze Sentiment
if st.button("Analyze Sentiment"):
    user_input = st.session_state.user_input
    if user_input.strip() == "":
        st.warning("Please enter or speak your feedback.")
    else:
        translated_text = translate_to_english(user_input, source_lang_code)
        st.write(f"🔄 Translated to English: *{translated_text}*")

        result = sentiment_pipeline(translated_text)[0]
        sentiment_label = map_sentiment_label(result['label'])

        st.success(f"🎯 Predicted Sentiment: *{sentiment_label}*")
        st.write(f"Raw Model Output: {result}")




# **********************************************************Gradio APP

# import gradio as gr
# from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
# from deep_translator import GoogleTranslator


# # Load Sentiment Model
# model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


# language_options = {
#     "English": "en",
#     "Telugu": "te",
#     "Hindi": "hi",
#     "Tamil": "ta",
#     "Kannada": "kn",
#     "Malayalam": "ml",
#     "Marathi": "mr",
#     "Gujarati": "gu",
#     "Bengali": "bn",
#     "Punjabi": "pa",
#     "Urdu": "ur"
# }


# def map_sentiment_label(label):
#     if '1' in label or '2' in label:
#         return 'Negative'
#     elif '3' in label:
#         return 'Neutral'
#     else:
#         return 'Positive'


# def translate_to_english(text, source_lang):
#     try:
#         return GoogleTranslator(source=source_lang, target='en').translate(text)
#     except:
#         return text


# def analyze_sentiment(user_input, selected_language):
#     source_lang_code = language_options[selected_language]
#     if user_input.strip() == "":
#         return "No input provided", "No sentiment", 0.0

#     translated_text = translate_to_english(user_input, source_lang_code)
#     result = sentiment_pipeline(translated_text)[0]
#     sentiment_label = map_sentiment_label(result['label'])
#     score = result['score']

#     return translated_text, sentiment_label, round(score, 3)


# # Gradio Interface
# with gr.Blocks() as demo:
#     gr.Markdown("🌐🗣️ Native Feedback Analysis🔍")

#     language = gr.Dropdown(choices=list(language_options.keys()), label="Select Language")

#     with gr.Tab("Text Input"):
#         txt = gr.Textbox(label="Type Your Feedback", placeholder="Write feedback here...")
#         txt_submit = gr.Button("Analyze Text")

#     with gr.Tab("Voice Input"):
#         mic = gr.Audio(sources=["microphone"], type="filepath", label="Record Your Feedback")
#         mic_submit = gr.Button("Analyze Voice")

#     output_text = gr.Textbox(label="Translated to English")
#     output_sentiment = gr.Textbox(label="Sentiment")
#     output_score = gr.Textbox(label="Confidence Score")

#     txt_submit.click(analyze_sentiment, inputs=[txt, language], outputs=[output_text, output_sentiment, output_score])

#     def speech_to_text(filepath, selected_language):
#         import speech_recognition as sr
#         r = sr.Recognizer()
#         with sr.AudioFile(filepath) as source:
#             audio = r.record(source)
#         try:
#             speech_codes = {
#                 "English": "en-US",
#                 "Telugu": "te-IN",
#                 "Hindi": "hi-IN",
#                 "Tamil": "ta-IN",
#                 "Kannada": "kn-IN",
#                 "Malayalam": "ml-IN",
#                 "Marathi": "mr-IN",
#                 "Gujarati": "gu-IN",
#                 "Bengali": "bn-IN",
#                 "Punjabi": "pa-IN",
#                 "Urdu": "ur-IN"
#             }
#             text = r.recognize_google(audio, language=speech_codes[selected_language])
#         except:
#             text = ""
#         return analyze_sentiment(text, selected_language)

#     mic_submit.click(speech_to_text, inputs=[mic, language], outputs=[output_text, output_sentiment, output_score])


# demo.launch()