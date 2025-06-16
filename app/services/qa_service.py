import asyncio
from app.services.llama_service import get_llama_answer
from app.services.web_search_service import search_web
from app.services.summarizer_service import summarize_texts
from app.utils.preprocess import preprocess_question

MAX_PROMPT_LENGTH = 4096  # Limit total prompt length for LLaMA3:8B
MAX_SUMMARY_LENGTH = 1500  # Limit web summaries length

async def answer_question(question: str):
    clean_q = preprocess_question(question)
    # RAG: Always search Google, summarize, and give to LLaMA3
    web_results = await search_web(clean_q)
    summaries = summarize_texts(web_results)
    summaries = summaries.split('\n')[:3]  # Take the most relevant 2-3 paragraphs
    summaries = '\n'.join(summaries)
    summaries = summaries[:MAX_SUMMARY_LENGTH]
    final_prompt = f"User question: {clean_q}\n\nRelevant web information:\n{summaries}\n\nUsing only the information above, answer the question clearly and concisely."
    final_prompt = final_prompt[:MAX_PROMPT_LENGTH]
    print(f"[DEBUG] RAG Prompt length: {len(final_prompt)}\nPrompt preview:\n{final_prompt[:500]}\n---END PREVIEW---")
    final_answer = await get_llama_answer(final_prompt)
    return final_answer, "internet+llama"
