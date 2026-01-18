import gradio as gr
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI  
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = None
qa_chain = None

def process_pdfs(pdf_files):
    global vector_db, qa_chain
    
    documents = []
    for pdf in pdf_files:
        loader = PyPDFLoader(pdf.name)
        documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    vector_db = FAISS.from_documents(docs, embeddings)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        chain_type="stuff"
    )

    return "PDFs uploaded and indexed. You can now ask questions!"

def answer_question(query):
    global qa_chain
    if qa_chain is None:
        return "Please upload PDF files first."
    try:
        result = qa_chain.invoke({"question": query})
        return result["answer"] if "answer" in result else str(result)
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# PDF RAG Chatbot with Memory (OpenAI)")
    with gr.Row():
        with gr.Column():
            pdf_upload = gr.File(file_types=[".pdf"], file_count="multiple", label="Upload up to 2 PDFs")
            upload_btn = gr.Button("Process PDFs")
            upload_output = gr.Textbox(label="Status")

        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Your Question")
            send_btn = gr.Button("Ask")

    upload_btn.click(process_pdfs, inputs=[pdf_upload], outputs=[upload_output])

    def chat_with_bot(user_message, history):
        bot_reply = answer_question(user_message)
        history = history + [[user_message, bot_reply]]
        return history

    send_btn.click(chat_with_bot, inputs=[msg, chatbot], outputs=[chatbot])

if __name__ == "__main__":
    demo.launch()
