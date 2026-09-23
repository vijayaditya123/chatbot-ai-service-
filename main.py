from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.documents import router as document_upload
from app.api.routes.query import router as  user_question

app=  FastAPI()

app.include_router(health_router)

app.include_router(document_upload)

app.include_router(user_question)