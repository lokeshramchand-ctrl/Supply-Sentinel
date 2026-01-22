import requests

session = requests.Session()

def call_local_llm(system_prompt: str, user_input: str) -> str:
    response = session.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"""
{system_prompt}

User input:
{user_input}

Respond ONLY in valid JSON.
""",
            "stream": False
        },
        timeout=30
    )

    return response.json()["response"]
