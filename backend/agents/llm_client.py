# import requests

# session = requests.Session()

# def call_local_llm(system_prompt: str, user_input: str) -> str:
#     response = session.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "mistral",
#             "prompt": f"""
# {system_prompt}

# User input:
# {user_input}

# Respond ONLY in valid JSON.
# """,
#             "stream": False
#         },
#         timeout=30
#     )

#     return response.json()["response"]
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system_prompt: str, user_input: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content