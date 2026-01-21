import requests

def call_local_llm(system_prompt: str, user_input: str) -> str:
    response = requests.post(
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
        }
    )

    return response.json()["response"]
