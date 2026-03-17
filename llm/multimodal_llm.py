import base64
import requests
from config.settings import OLLAMA_URL

class MultiModalLLM:

    def __init__(self, model="llava"):
        self.model = model
        self.url = OLLAMA_URL

    def describe_image(self, image_path, prompt):

        with open(image_path, "rb") as f:
            image_base64 = base64.b64encode(f.read()).decode("utf-8")

        payload = {
            "model": self.model,
            "prompt": prompt,
            "images": [image_base64],
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        return response.json()["response"]