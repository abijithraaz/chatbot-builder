import abc

class BaseLLM(abc.ABC):
    name = "BaseExtractor (abstract)"

    @abc.abstractmethod
    def llmchat(self, prompt:str) -> str:
        """
        Returning the query response.
        """