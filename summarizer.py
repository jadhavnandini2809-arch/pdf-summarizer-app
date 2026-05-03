def summarize_text(text):
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, 3)

    final_summary = ""
    for sentence in summary:
        final_summary += str(sentence) + " "

    return final_summary