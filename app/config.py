from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
PIPER_PATH = os.getenv("PIPER_PATH")
PIPER_MODEL = os.getenv("PIPER_MODEL")