import os
import openai 
from openai import OpenAI
from services.faiss_service import search_faiss
from gtts import gTTS
from fastapi import HTTPException
from io import BytesIO
from fastapi.staticfiles import StaticFiles
from uuid import uuid4

token = "Token deleted for security"
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)



async def generate_chat_response(question: str, context: str):
    # Retrieve relevant chunks from FAISS based on the question
    relevant_texts = search_faiss(question, top_k=5)
    
    if not relevant_texts:
        return "I'm sorry, I couldn't find relevant information in the provided PDFs."

    # Combine relevant texts into a single context string
    combined_context = "\n\n".join(relevant_texts)
    
    # Generate the response using OpenAI API
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": f"Context: {combined_context}"},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    
    text_response = response.choices[0].message.content.strip()
    # return response.choices[0].message.content.strip()
    
    try:
        # Ensure the directory exists
        
        # Convert text response to speech using Google TTS
        tts = gTTS(text=text_response, lang='en')
        audio_filename = f"{uuid4()}.mp3"  # Generate a unique filename
        audio_filepath = f"./static/audio/{audio_filename}"
        tts.save(audio_filepath)

        # Return text and the URL of the audio file
        audio_url = f"http://localhost:8000/static/audio/{audio_filename}"
        return {"text": text_response, "audio_url": audio_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")
