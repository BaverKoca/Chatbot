from transformers import pipeline
from typing import List
import os
import requests

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_texts(texts: List[str], max_length: int = 130, min_length: int = 30) -> str:
    summaries = []
    for text in texts:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return "\n".join(summaries)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

async def search_web(query: str, num_results: int = 5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    items = resp.json().get("items", [])
    results = []
    for item in items:
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        results.append(f"{snippet}\nSource: {link}")
    return results
