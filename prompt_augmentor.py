import os
from retriever.data_retriever import PineconeDBRetriever
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA


template = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

class PromptAugmentor:
    def __init__(self) -> None:
        pass

    def augment_prompt(self, query, embedd, llm):
        
        retriever = PineconeDBRetriever()
        vectorstore = retriever.retrieve_data(embedd_client=embedd)

        qa = RetrievalQA.from_chain_type(
        prompt=prompt,
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever())

        return qa.run(query)