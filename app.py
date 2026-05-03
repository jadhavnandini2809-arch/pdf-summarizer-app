import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text

st.title("📄 AI Document Summarizer")

st.write("Upload a PDF to generate summary")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("File uploaded!")

    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Preview:")
    st.write(text[:500])

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary:")
        st.write(summary)