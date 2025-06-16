import asyncio
from app.services.llama_service import get_llama_answer
from app.services.web_search_service import search_web
from app.services.summarizer_service import summarize_texts
from app.utils.preprocess import preprocess_question

MAX_PROMPT_LENGTH = 4096  # Limit total prompt length for LLaMA3:8B
MAX_SUMMARY_LENGTH = 1500  # Limit web summaries length

def truncate_text(text, max_len):
    if len(text) > max_len:
        return text[:max_len] + "... [truncated]"
    return text

async def answer_question(question: str):
    clean_q = preprocess_question(question)
    web_results = await search_web(clean_q)
    summaries = summarize_texts(web_results)
    summaries = truncate_text(summaries, MAX_SUMMARY_LENGTH)
    llama_answer = await get_llama_answer(clean_q)
    final_prompt = f"User question: {clean_q}\n\nWeb summaries:\n{summaries}\n\nModel's own answer: {llama_answer}\n\nUsing both the web information and your own knowledge, answer the question clearly and concisely."
    final_prompt = truncate_text(final_prompt, MAX_PROMPT_LENGTH)
    # Debug logging
    print(f"[DEBUG] Prompt length: {len(final_prompt)}\nPrompt preview:\n{final_prompt[:500]}\n---END PREVIEW---")
    final_answer = await get_llama_answer(final_prompt)
    return final_answer, "internet+llama"
