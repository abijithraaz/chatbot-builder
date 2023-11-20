import os
import pinecone
import time
from langchain.vectorstores import Pinecone

from data_handling.base_db_handling import DataStoring

class PineconeDB(DataStoring):
    def __init__(self) -> None:
        pinecone.init(api_key=os.getenv('PINECONE_API_KEY', ''), environment=os.getenv('PINECONE_ENVIRONMENT', ''))

    def vectordata_storing(self, document_chunks, embedd_obj):
        index = pinecone.Index(os.environ['PINECONE_INDEX_NAME'])
        # wait a moment for the index to be fully initialized
        time.sleep(1)

        # print('DocumentsChunks:',document_chunks)
        for ind, row in document_chunks.iterrows():
            vector_data = {'id':str(ind), 'values': row['embeddings'],'metadata': {'text': row['text']}}
            index.upsert([vector_data])
        print('Vector data storing completed!!!!')
        return True