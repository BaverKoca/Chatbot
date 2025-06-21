from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os

router = APIRouter()

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), '../../feedback.json')

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int

@router.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    try:
        if os.path.exists(FEEDBACK_FILE):
            with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        data.append(feedback.dict())
        with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
