import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Urdu ⇄ English Translator", page_icon="🌐")

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&display=swap" rel="stylesheet">
    <style>
    .urdu { direction: rtl; text-align: right; font-family: 'Noto Nastaliq Urdu', serif;
            font-size: 1.4rem; line-height: 2.2; }
    .english { direction: ltr; text-align: left; font-size: 1.2rem; }
    .result-box { padding: 1rem; border-radius: 8px; border: 1px solid #ddd; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌐 Urdu ⇄ English Translator")
st.caption("Powered by Google Translate")

direction = st.radio(
    "Translation direction",
    ["English → Urdu", "Urdu → English"],
    horizontal=True,
)

if direction == "English → Urdu":
    source, target = "en", "ur"
    input_class, output_class = "english", "urdu"
else:
    source, target = "ur", "en"
    input_class, output_class = "urdu", "english"

text = st.text_area("Enter text", height=150, max_chars=5000)

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Translating..."):
                result = GoogleTranslator(source=source, target=target).translate(text)
            st.subheader("Translation")
            st.markdown(
                f'<div class="result-box {output_class}">{result}</div>',
                unsafe_allow_html=True,
            )
            st.code(result, language=None)  # easy copy button
        except Exception as e:
            st.error(f"Translation failed: {e}")
