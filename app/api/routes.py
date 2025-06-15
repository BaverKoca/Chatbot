from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.qa_service import answer_question

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    source: str

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        answer, source = await answer_question(request.question)
        return AnswerResponse(answer=answer, source=source)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
