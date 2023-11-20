import abc

class BaseEmbeddGenarator(abc.ABC):
    name = "Base embedding generator class"

    @abc.abstractmethod
    def embedd_generator(self, data_frame):
        """
        Returning the query response.
        """