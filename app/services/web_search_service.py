import os
import requests
import re

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

# Simple cache for repeated queries
web_cache = {}

# Domains to prioritize
PRIORITY_DOMAINS = ["wikipedia.org", ".gov", ".edu", ".org"]

def is_priority(url):
    return any(domain in url for domain in PRIORITY_DOMAINS)

def chunk_text(text, chunk_size=300):
    # Split text into chunks of about chunk_size characters
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

async def search_web(query: str, num_results: int = 5):
    if query in web_cache:
        return web_cache[query]
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
    # Filter and prioritize
    items = sorted(items, key=lambda x: not is_priority(x.get("link", "")))
    results = []
    for item in items:
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        for chunk in chunk_text(snippet):
            results.append({"text": chunk, "url": link})
    web_cache[query] = results
    return results
