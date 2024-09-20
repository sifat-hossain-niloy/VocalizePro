# # backend/services/pdf_service.py
# import fitz  # PyMuPDF for PDF processing
# from langchain.text_splitter import CharacterTextSplitter
# from services.faiss_service import add_to_faiss
# import asyncio

# async def process_pdf(files):
#     raw_text = ""
#     for file in files:
#         pdf_document = fitz.open(stream=await file.read(), filetype="pdf")
#         for page_num in range(pdf_document.page_count):
#             page = pdf_document.load_page(page_num)
#             text = page.get_text()
#             if text:
#                 raw_text += text + "\n"

#     if not raw_text:
#         raise ValueError("No text extracted from PDFs.")

#     # Split text into chunks
#     text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
#     text_chunks = text_splitter.split_text(raw_text)

#     # Add chunks to FAISS asynchronously
#     await asyncio.gather(*(add_to_faiss(chunk) for chunk in text_chunks))

#     return text_chunks  # Return extracted chunks for debugging/logging

import os
import fitz  # PyMuPDF for PDF processing
from langchain.text_splitter import CharacterTextSplitter
from services.faiss_service import add_to_faiss
import asyncio
from fastapi import HTTPException

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the upload directory exists

# Process and store PDF files
async def process_pdf(files):
    raw_text = ""
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb+") as f:
            f.write(file.file.read())
        
        pdf_document = fitz.open(file_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            if text:
                raw_text += text + "\n"

    if not raw_text:
        raise ValueError("No text extracted from PDFs.")

    # Split text into chunks
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_text(raw_text)

    # Add chunks to FAISS asynchronously
    await asyncio.gather(*(add_to_faiss(chunk) for chunk in text_chunks))

    return text_chunks  # Return extracted chunks for debugging/logging

# List all uploaded files
def list_uploaded_files():
    files = [f for f in os.listdir(UPLOAD_DIR) if os.path.isfile(os.path.join(UPLOAD_DIR, f))]
    return {"files": files}

# Delete a specific file
def delete_uploaded_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": f"File '{filename}' deleted successfully."}
    raise HTTPException(status_code=404, detail="File not found")
