import os
import pinecone
from langchain.vectorstores import Pinecone

from retriever.base_retriever import DataRetriever

class PineconeDBRetriever(DataRetriever):
    def __init__(self) -> None:
        pinecone.init(api_key=os.getenv('PINECONE_API_KEY', ''), environment=os.getenv('PINECONE_ENVIRONMENT', ''))

    def retrieve_data(self, embedd_client):
        text_field = "text"

        # switch back to normal index for langchain
        index = pinecone.Index(os.environ['PINECONE_INDEX_NAME'])

        vectorstore = Pinecone(index, embedd_client.embed_query, text_field)

        return vectorstore