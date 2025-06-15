import re

def preprocess_question(question: str) -> str:
    q = question.strip()
    q = re.sub(r'\s+', ' ', q)
    return q
