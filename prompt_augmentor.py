import os
from retriever.data_retriever import PineconeDBRetriever
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

class PromptAugmentor:
    def __init__(self) -> None:
        pass

    def augment_prompt(self, query, embedd, llm):
        
        retriever = PineconeDBRetriever()
        vectorstore = retriever.retrieve_data(embedd_client=embedd)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        qa = RetrievalQA.from_chain_type(
        prompt=prompt,
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever())

        mod_query = f"""You are an assistant for question-answering tasks. 
            Use the following pieces of retrieved context to answer the question. 
            If you don't know the answer, just say that you don't know. 
            Use three sentences maximum and keep the answer concise.
            Question: {query} 
            Context: 
            Answer:
            """

        return qa.run(mod_query)
