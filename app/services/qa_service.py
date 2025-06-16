import asyncio
from app.services.llama_service import get_llama_answer
from app.services.web_search_service import search_web
from app.utils.preprocess import preprocess_question

MAX_PROMPT_LENGTH = 4096  # Limit total prompt length for LLaMA3:8B
MAX_SUMMARY_LENGTH = 1500  # Limit web summaries length

# Simple keyword overlap ranking
def rank_chunks(chunks, question, top_n=3):
    question_words = set(question.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = set(chunk['text'].lower().split())
        score = len(question_words & chunk_words)
        scored.append((score, chunk))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored[:top_n]]

async def answer_question(question: str):
    clean_q = preprocess_question(question)
    web_chunks = await search_web(clean_q)
    # Rank and select top 3 relevant chunks
    top_chunks = rank_chunks(web_chunks, clean_q, top_n=3)
    # Build context with source attribution
    context = "\n\n".join([f"{c['text']}\nSource: {c['url']}" for c in top_chunks])
    context = context[:MAX_SUMMARY_LENGTH]
    final_prompt = f"User question: {clean_q}\n\nRelevant web information:\n{context}\n\nUsing only the information above, answer the question clearly and concisely. Cite sources if possible."
    final_prompt = final_prompt[:MAX_PROMPT_LENGTH]
    print(f"[DEBUG] RAG Prompt length: {len(final_prompt)}\nPrompt preview:\n{final_prompt[:500]}\n---END PREVIEW---")
    final_answer = await get_llama_answer(final_prompt)
    return final_answer, "internet+llama"
