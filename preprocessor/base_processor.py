import abc
from typing import Dict

class DataLoader(abc.ABC):

    @abc.abstractmethod
    def load_data(self, document_path) -> Dict:
        """
        Return the loaded data
        """

class DataChunkCreator(abc.ABC):

    @abc.abstractmethod
    def create_chunks(self, loaded_document:dict):
        """
        Return the splitted chunks of data
        """
