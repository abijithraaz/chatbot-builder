import os

import streamlit as st
from preprocessor.langchain_processor import LangChainDataLoader, LangChainChunkCreator
from embedding.openai_embedd_generator import OpenaiEmbeddGenarator
from data_handling.pinecone_db_handler import PineconeDB

embedd = OpenaiEmbeddGenarator()
dataloader = LangChainDataLoader()
chunkscreator = LangChainChunkCreator()
embedd_creator = OpenaiEmbeddGenarator()
pinecone_db = PineconeDB()

st.header('Chatbot Manager',divider='rainbow')
st.markdown('We can customize the chatbot using this page')

st.markdown('Upload custom text file data to cutomize the chatbot')
input_file = st.file_uploader(label='inputs in txt', type=['txt'])
button = st.button(label='Upload')

if input_file and button:
    loaded_data = dataloader.load_data(input_file)
    data_chunks = chunkscreator.create_chunks(loaded_data)
    vector_dataset = embedd_creator.embedd_generator(data_frame=data_chunks)
    datawrite = pinecone_db.vectordata_storing(data_chunks, embedd)
    if datawrite:
        st.markdown('Chatbot customization is completed.')
        
st.markdown('Please write DELETE in the inpu section to clear the DB')
input_file = st.text_input(label='DELETE Query')
button = st.button(label='CLEAR CUSTOMIZATION')

if input_file=='DELETE' and button:
    clr_flag = pinecone_db.clear_db()
    if clr_flg:
        st.markdown('Chatbot DB is completely wiped.')
