import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma3"