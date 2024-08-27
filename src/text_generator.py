import os

from langchain_mistralai import ChatMistralAI

from src.utils import get_api_key


class TextGenerator:
    os.environ["MISTRAL_API_KEY"] = get_api_key()

    def __init__(self, model_name, temperature):
        self.model = ChatMistralAI(model=model_name, temperature=temperature)

    def generate_text(self, prompt):
        response = self.model.invoke(prompt)
        return response.content
