import streamlit as st
from langchain_community.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import requests

st.set_page_config('Willinn IA-Api')
st.header('Vectorizar PDF')

pdf_file = st.file_uploader("Cargar PDF", type="pdf",
on_change=st.cache_resource.clear)
@st.cache_resource
def create_embeddings(pdf):
    
    reader = PdfReader(pdf)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        length_function=len
    )

    join_chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    vectorial_data_base = FAISS.from_texts(join_chunks, embeddings)

    return vectorial_data_base

if pdf_file is not None:
    data_base = create_embeddings(pdf_file)
    user_question = st.text_input('Consulta sobre el PDF Cargado')

    if user_question:
        context = data_base.similarity_search(user_question, 3)

        llm = Ollama(model="llama2", base_url='http://localhost:11434')
        chain = load_qa_chain(llm, chain_type="stuff")
        answer = chain.run(input_documents=context, question=user_question)
        st.write(answer)

else:
    user_question = st.text_input('Consulta sobre el PDF Default')

    if user_question:
        response = requests.post("http://localhost:5555/llama2", json={"question": user_question})

        if response.status_code == 200:
            answer = response.json().get("answer")
            st.write(answer)
        else:
            st.write("Error en la solicitud:", response.json().get("error"))