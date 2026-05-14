import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "llama3.2")
        self.timeout = int(os.getenv("OLLAMA_TIMEOUT", "120"))

    def chat(self, prompt, system="", temp=0.7, max_tokens=300):
        url = f"{self.host}/api/chat"

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            },
            "stream": False
        }

        inicio = time.time()
        response = requests.post(url, json=payload, timeout=self.timeout)
        fim = time.time()

        resposta_json = response.json()

        return {
            "resposta": resposta_json["message"]["content"],
            "tempo_ms": round((fim - inicio) * 1000, 2)
        }