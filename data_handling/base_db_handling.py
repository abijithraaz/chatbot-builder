import abc

class DataStoring(abc.ABC):

    @abc.abstractmethod
    def vectordata_storing(self, document_chunks):
        """
        Storing the embedded chunks
        """

class DBModify(abc.ABC):

    @abc.abstractmethod
    def modify_db(self, sql_query):
        """
        Modifying the vector DB
        """