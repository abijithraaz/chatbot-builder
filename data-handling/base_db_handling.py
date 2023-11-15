import abc

class DataStoring(abc.ABC):

    @abc.abstractmethod
    def vectordata_storing(self, document_chunks):
        """
        Storing the embedded chunks
        """