import os
from langchain.embeddings.openai import OpenAIEmbeddings

from embedding.base_embedd_generator import BaseEmbeddGenarator

class OpenaiEmbeddGenarator(BaseEmbeddGenarator):
    def __init__(self) -> None:
        self.embed = OpenAIEmbeddings(model=os.getenv('OPENAI_EMBEDD_MODEL',''),openai_api_key=os.getenv('OPENAI_API_KEY',''))

    def embedd_generator(self, data_frame):
        print(data_frame)
        # openai ada embedding
        def get_embedding(text):
            return self.embed.embed_query(text) 
        for data in data_frame['text']:
            data_frame['embeddings'] = [get_embedding(data)]
        return data_frame
