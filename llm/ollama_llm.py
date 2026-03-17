import requests
from .base_llm import BaseLLM
from config.settings import OLLAMA_URL, DEFAULT_MODEL

class OllamaLLM(BaseLLM):

    def __init__(self, model=DEFAULT_MODEL):
        self.model = model

    def generate(self, prompt: str):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
    
    def stream(self, prompt: str):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )

        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8")
                if '"response"' in data:
                    import json
                    chunk = json.loads(data)
                    yield chunk.get("response", "")