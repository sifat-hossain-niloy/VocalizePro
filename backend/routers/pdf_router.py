# backend/routers/pdf_router.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from services.pdf_service import process_pdf

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(files: list[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded.")
    try:
        await process_pdf(files)
        return {"message": "PDFs processed and indexed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
