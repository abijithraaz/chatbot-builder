from openai import OpenAI
from base_llm import BaseLLM

class OpenAiLLM(BaseLLM):

    def __init__(self, openai_key) -> None:
        self.client = OpenAI(api_key=openai_key)

    def llmchat(self, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
        return chat_completion