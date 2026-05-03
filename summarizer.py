def summarize_text(text):
    # Simple sentence splitting (no NLTK)
    sentences = text.replace('\n', ' ').split('.')

    # Clean sentences
    sentences = [s.strip() for s in sentences if s.strip()]

    # Take first 5 sentences
    summary = ". ".join(sentences[:5])

    return summary + "."
