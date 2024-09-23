
# VocalizePro - Factory Communication System

## Overview
VocalizePro is a chatbot-based communication system designed to simplify the exchange of technical knowledge in a factory setting. Many factory workers may struggle with reading and understanding complex technical documents. VocalizePro extracts text from PDF documents, provides summaries, and delivers audio responses for easy comprehension.

## Features
- **PDF Upload & Text Extraction**: Admins can upload PDF documents.
- **Text-to-Speech**: Generates an audio response for each user query.
- **User & Admin Roles**: Admins validate user accounts; users interact with the system to get responses.
- **React Frontend**: Simple and user-friendly frontend for interaction.
- **FastAPI Backend**: Backend with APIs to handle PDF uploads and queries.

## Tech Stack
- **Frontend**: React, Material UI
- **Backend**: FastAPI
- **Database**: SQLite (for user validation and PDF tracking)
- **Text Processing**: LangChain, FAISS for efficient document indexing and search

## Project Setup

### 1. Clone the Repository
```
git clone https://github.com/sifat-hossain-niloy/VocalizePro.git
cd VocalizePro
```

### 2. Backend Setup

- Create a virtual environment:
  ```
  python -m venv .venv
  source .venv/bin/activate  # Linux/Mac
  .venv\Scripts\activate  # Windows
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Start the backend server:
  ```
  uvicorn app:app --reload
  ```

### 3. Frontend Setup

- Navigate to the `frontend` directory:
  ```
  cd frontend
  ```
- Install frontend dependencies:
  ```
  npm install
  ```
- Start the frontend server:
  ```
  npm start
  ```

## Usage
- Admins can upload PDFs for processing.
- Users can interact with the bot by asking questions related to the PDFs, and get both text and audio responses.

## Future Enhancements
- Support for multiple languages.
- Enhanced user interface.
- Improved document parsing with support for more file types.

## License
MIT License
