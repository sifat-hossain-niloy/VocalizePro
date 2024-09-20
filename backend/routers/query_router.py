# backend/routers/query_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.faiss_service import search_faiss
from services.openai_service import generate_chat_response

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/chat/")
async def chat_completion(request: QueryRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    # Retrieve relevant context from FAISS
    relevant_context = search_faiss(question, top_k=5)

    # Generate response from OpenAI
    response = await generate_chat_response(question, relevant_context)
    
    return {"answer": response}
