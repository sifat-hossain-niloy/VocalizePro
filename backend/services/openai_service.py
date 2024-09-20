import os
import openai 
from openai import OpenAI
from services.faiss_service import search_faiss


token = "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"


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
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "system", "content": f"Context: {combined_context}"},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error in generating response: {str(e)}"
