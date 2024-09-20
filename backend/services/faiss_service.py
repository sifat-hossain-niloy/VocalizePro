# import faiss
# from langchain.embeddings import HuggingFaceEmbeddings

# # Load FAISS and HuggingFace Embeddings
# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device':'cpu'})
# index = faiss.IndexFlatL2(384)

# # Function to retrieve relevant chunks
# def get_relevant_chunks(query):
#     query_embedding = embedding_model.embed_query(query)
#     distances, indices = index.search(query_embedding.reshape(1, -1), k=3)
    
#     # Retrieve the top matching chunks based on FAISS
#     relevant_chunks = [pdf_texts[i] for i in indices[0]]
#     return " ".join(relevant_chunks)

# backend/services/faiss_service.py
import faiss
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize global variables
pdf_texts = []  # List to store text chunks
dimension = 384  # Dimension for all-MiniLM-L6-v2 embeddings
index = faiss.IndexFlatL2(dimension)
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device':'cpu'})

def initialize_faiss():
    global index
    if not index.is_trained:
        index.train(np.array([]))  # Dummy training if necessary

async def add_to_faiss(text):
    global index, pdf_texts, embeddings_model
    # Generate embedding
    embedding = embeddings_model.embed_query(text)
    embedding = np.array(embedding).astype('float32').reshape(1, -1)
    # Add to FAISS index
    index.add(embedding)
    # Store the text chunk
    pdf_texts.append(text)

def search_faiss(query, top_k=5):
    global index, pdf_texts, embeddings_model
    if index.ntotal == 0:
        return []
    
    # Generate embedding for the query
    query_embedding = embeddings_model.embed_query(query)
    query_embedding = np.array(query_embedding).astype('float32').reshape(1, -1)
    
    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)
    
    # Retrieve relevant texts
    relevant_texts = [pdf_texts[idx] for idx in indices[0] if idx < len(pdf_texts)]
    return relevant_texts
