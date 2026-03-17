from openai import OpenAI
from .base_llm import BaseLLM
from config.settings import OPENAI_API_KEY

class OpenAILLM(BaseLLM):

    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = model

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content