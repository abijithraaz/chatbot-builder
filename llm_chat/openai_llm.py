import os
from openai import OpenAI
from llm_chat.base_llm import BaseLLM

class OpenAiLLM(BaseLLM):
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.getenv('OPENAI_AP_KEY', ''))

    def llmchat(self, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
        return chat_completion.choices[0].message.content
