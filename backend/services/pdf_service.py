# backend/services/pdf_service.py
import fitz  # PyMuPDF for PDF processing
from langchain.text_splitter import CharacterTextSplitter
from services.faiss_service import add_to_faiss
import asyncio

async def process_pdf(files):
    raw_text = ""
    for file in files:
        pdf_document = fitz.open(stream=await file.read(), filetype="pdf")
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

    # Generate embeddings and add to FAISS
    await asyncio.gather(*(add_to_faiss(chunk) for chunk in text_chunks))
