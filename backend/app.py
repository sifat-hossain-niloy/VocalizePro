# # # importing dependencies
# # from dotenv import load_dotenv
# # import streamlit as st
# # from PyPDF2 import PdfReader
# # from langchain.text_splitter import CharacterTextSplitter
# # from langchain.embeddings import HuggingFaceEmbeddings
# # from langchain.vectorstores import faiss
# # from langchain.prompts import PromptTemplate
# # from langchain.memory import ConversationBufferMemory
# # from langchain.chains import ConversationalRetrievalChain
# # from langchain.chat_models import ChatOpenAI
# # from htmlTemplates import css, bot_template, user_template

# # # creating custom template to guide llm model
# # custom_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
# # Chat History:
# # {chat_history}
# # Follow Up Input: {question}
# # Standalone question:"""

# # CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)

# # # extracting text from pdf
# # def get_pdf_text(docs):
# #     text=""
# #     for pdf in docs:
# #         pdf_reader=PdfReader(pdf)
# #         for page in pdf_reader.pages:
# #             text+=page.extract_text()
# #     return text

# # # converting text to chunks
# # def get_chunks(raw_text):
# #     text_splitter=CharacterTextSplitter(separator="\n",
# #                                         chunk_size=1000,
# #                                         chunk_overlap=200,
# #                                         length_function=len)   
# #     chunks=text_splitter.split_text(raw_text)
# #     return chunks

# # # using all-MiniLm embeddings model and faiss to get vectorstore
# # def get_vectorstore(chunks):
# #     embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
# #                                      model_kwargs={'device':'cpu'})
# #     vectorstore=faiss.FAISS.from_texts(texts=chunks,embedding=embeddings)
# #     return vectorstore

# # # generating conversation chain  
# # def get_conversationchain(vectorstore):
# #     llm=ChatOpenAI(temperature=0.2)
# #     memory = ConversationBufferMemory(memory_key='chat_history', 
# #                                       return_messages=True,
# #                                       output_key='answer') # using conversation buffer memory to hold past information
# #     conversation_chain = ConversationalRetrievalChain.from_llm(
# #                                 llm=llm,
# #                                 retriever=vectorstore.as_retriever(),
# #                                 condense_question_prompt=CUSTOM_QUESTION_PROMPT,
# #                                 memory=memory)
# #     return conversation_chain

# # # generating response from user queries and displaying them accordingly
# # def handle_question(question):
# #     response=st.session_state.conversation({'question': question})
# #     st.session_state.chat_history=response["chat_history"]
# #     for i,msg in enumerate(st.session_state.chat_history):
# #         if i%2==0:
# #             st.write(user_template.replace("{{MSG}}",msg.content,),unsafe_allow_html=True)
# #         else:
# #             st.write(bot_template.replace("{{MSG}}",msg.content),unsafe_allow_html=True)


# # def main():
# #     load_dotenv()
# #     st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")
# #     st.write(css,unsafe_allow_html=True)
# #     if "conversation" not in st.session_state:
# #         st.session_state.conversation=None

# #     if "chat_history" not in st.session_state:
# #         st.session_state.chat_history=None
    
# #     st.header("Chat with multiple PDFs :books:")
# #     question=st.text_input("Ask question from your document:")
# #     if question:
# #         handle_question(question)
# #     with st.sidebar:
# #         st.subheader("Your documents")
# #         docs=st.file_uploader("Upload your PDF here and click on 'Process'",accept_multiple_files=True)
# #         if st.button("Process"):
# #             with st.spinner("Processing"):
                
# #                 #get the pdf
# #                 raw_text=get_pdf_text(docs)
                
# #                 #get the text chunks
# #                 text_chunks=get_chunks(raw_text)
                
# #                 #create vectorstore
# #                 vectorstore=get_vectorstore(text_chunks)
                
# #                 #create conversation chain
# #                 st.session_state.conversation=get_conversationchain(vectorstore)


# # if __name__ == '__main__':
# #     main()

# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# import streamlit as st
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import faiss
# from htmlTemplates import css, bot_template, user_template

# # Initialize OpenAI client
# load_dotenv()
# token = os.getenv("GITHUB_TOKEN")
# endpoint = "https://models.inference.ai.azure.com"
# model_name = "gpt-4o"

# client = OpenAI(
#     base_url=endpoint,
#     api_key=token,
# )

# # extracting text from pdf
# def get_pdf_text(docs):
#     text = ""
#     for pdf in docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return text

# # converting text to chunks
# def get_chunks(raw_text):
#     text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
#     chunks = text_splitter.split_text(raw_text)
#     return chunks

# # using all-MiniLm embeddings model and faiss to get vectorstore
# def get_vectorstore(chunks):
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device':'cpu'})
#     vectorstore = faiss.FAISS.from_texts(texts=chunks, embedding=embeddings)
#     return vectorstore

# # generating response from user queries using your OpenAI setup
# def get_openai_response(question, context):
#     response = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"{context}\n\n{question}"}
#         ],
#         temperature=0.7,
#         max_tokens=1000,
#         model=model_name
#     )
#     return response.choices[0].message.content

# # generating response from user queries and displaying them accordingly
# def handle_question(question):
#     # Add logic to retrieve the context from FAISS or previous conversation history
#     context = "Some relevant PDF text here"
#     response = get_openai_response(question, context)
    
#     st.session_state.chat_history.append({"user": question, "bot": response})
#     for entry in st.session_state.chat_history:
#         st.write(user_template.replace("{{MSG}}", entry['user']), unsafe_allow_html=True)
#         st.write(bot_template.replace("{{MSG}}", entry['bot']), unsafe_allow_html=True)

# def main():
#     st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
#     st.write(css, unsafe_allow_html=True)

#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     st.header("Chat with multiple PDFs :books:")
#     question = st.text_input("Ask question from your document:")
#     if question:
#         handle_question(question)

#     with st.sidebar:
#         st.subheader("Your documents")
#         docs = st.file_uploader("Upload your PDF here and click on 'Process'", accept_multiple_files=True)
#         if st.button("Process"):
#             with st.spinner("Processing"):
#                 raw_text = get_pdf_text(docs)
#                 text_chunks = get_chunks(raw_text)
#                 vectorstore = get_vectorstore(text_chunks)

# if __name__ == '__main__':
#     main()

from fastapi import FastAPI
from routers import pdf_router, query_router

app = FastAPI()

# Include the routers for PDF processing and querying
app.include_router(pdf_router.router)
app.include_router(query_router.router)

@app.get("/")
async def root():
    return {"message": "API is running successfully!"}

