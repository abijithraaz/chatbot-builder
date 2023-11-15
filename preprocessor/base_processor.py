import abc
from typing import Dict

class DataLoader(abc.ABC):

    @abc.abstractmethod
    def load_data(self, document_path:str) -> Dict:
        """
        Return the loaded data
        """

class DataChunk(abc.ABC):

    @abc.abstractmethod
    def create_chunks(self, loaded_document:dict) -> Dict:
        """
        Return the splitted chunks of data

        """
