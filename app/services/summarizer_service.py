from transformers import pipeline
from typing import List

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_texts(texts: List[str], max_length: int = 130, min_length: int = 30) -> str:
    summaries = []
    for text in texts:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return "\n".join(summaries)
