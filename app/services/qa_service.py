import asyncio
from app.services.llama_service import get_llama_answer
from app.services.web_search_service import search_web
from app.services.summarizer_service import summarize_texts
from app.utils.preprocess import preprocess_question

async def answer_question(question: str):
    clean_q = preprocess_question(question)
    llama_answer = await get_llama_answer(clean_q)
    if not llama_answer or "I don't know" in llama_answer or "not sure" in llama_answer.lower():
        web_results = await search_web(clean_q)
        summaries = summarize_texts(web_results)
        final_prompt = f"User question: {clean_q}\n\nWeb summaries:\n{summaries}\n\nAnswer the question using the above information."
        final_answer = await get_llama_answer(final_prompt)
        return final_answer, "internet+llama"
    return llama_answer, "llama"
