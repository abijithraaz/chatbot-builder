import os
from typing import Dict
from io import StringIO
import pandas as pd
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from preprocessor.base_processor import DataLoader, DataChunkCreator

class LangChainDataLoader(DataLoader):
    def __init__(self) -> None:
        pass

    def load_data(self, document_path) -> Dict:
        # To convert to a string based IO:
        stringio = StringIO(document_path.getvalue().decode("utf-8"))
        
        # To read file as string:
        string_data = stringio.read()
        with open("./tmp/tmp_input.txt", "w") as f:
            f.write(string_data)

        loader = TextLoader(r"./tmp/tmp_input.txt")
        documents = loader.load()
        return documents
    
class LangChainChunkCreator(DataChunkCreator):
    def __init__(self) -> None:
        pass

    def create_chunks(self, loaded_document: dict):
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(loaded_document)
        chunk_df = pd.DataFrame(columns=['text'])
        for chunk in chunks:
            chunk_df['text'] = [chunk.page_content]
        return chunk_df
    