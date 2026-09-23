import os
from dotenv import load_dotenv
import json
if os.path.exists("appsettings.json"):
      with open("appsettings.json") as f:
          settings = json.load(f)
          for key, value in settings.items():
              os.environ[key] = str(value)
      
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
COHERE_BASE_URL = os.getenv("COHERE_BASE_URL") or None
CHROMA_HOST = os.getenv("CHROMA_HOST", "local")
CHROMA_PORT = os.getenv("CHROMA_PORT", "8000")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-5-mini")