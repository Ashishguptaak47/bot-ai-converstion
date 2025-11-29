import requests
from .config import GROQ_API_KEY, LLM_MODEL

def call_llm(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}

    payload = {
        "model": LLM_MODEL,
        "messages": messages
    }

    res = requests.post(url, json=payload, headers=headers)
    data = res.json()
    return data["choices"][0]["message"]["content"]
