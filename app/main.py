from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LLaMA3 Internet QA Bot")

app.include_router(router)
