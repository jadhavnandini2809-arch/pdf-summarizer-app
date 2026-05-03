def summarize_text(text):
    import nltk
    nltk.download('punkt', quiet=True)

    from nltk.tokenize import sent_tokenize

    sentences = sent_tokenize(text)

    # Take first 5 sentences as summary
    summary = " ".join(sentences[:5])

    return summary
