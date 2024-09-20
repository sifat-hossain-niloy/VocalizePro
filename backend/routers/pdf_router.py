# # backend/routers/pdf_router.py
# from fastapi import APIRouter, UploadFile, File, HTTPException
# from services.pdf_service import process_pdf

# router = APIRouter()

# @router.post("/upload_pdf/")
# async def upload_pdf(files: list[UploadFile] = File(...)):
#     if not files:
#         raise HTTPException(status_code=400, detail="No files uploaded.")
#     try:
#         # Process PDF files and extract text
#         chunks = await process_pdf(files)
#         return {"message": "PDFs processed and indexed successfully.", "chunks": len(chunks)}
#     except Exception as e:
#         return HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

from fastapi import APIRouter, UploadFile, File, HTTPException
from services.pdf_service import process_pdf, list_uploaded_files, delete_uploaded_file

router = APIRouter()

# Route to upload PDFs
@router.post("/upload_pdf/")
async def upload_pdf(files: list[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded.")
    try:
        # Process PDF files and extract text
        chunks = await process_pdf(files)
        return {"message": "PDFs processed and indexed successfully.", "chunks": len(chunks)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

# Route to list all uploaded PDFs
@router.get("/files/")
async def list_files():
    return list_uploaded_files()

# Route to delete a specific file
@router.delete("/files/{filename}")
async def delete_file(filename: str):
    return delete_uploaded_file(filename)
