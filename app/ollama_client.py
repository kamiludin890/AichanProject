import requests
from app.config import OLLAMA_MODEL, OLLAMA_URL


def ask_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 120,
            "temperature": 0.7,
            "num_thread": 4,
            "num_ctx": 1024
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    data = response.json()

    return data.get("response", "Tidak ada respon")