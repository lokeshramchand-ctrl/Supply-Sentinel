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
from dotenv import load_dotenv

load_dotenv()

# OpenAI Client
try:
    from openai import OpenAI
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except ImportError:
    openai_client = None

# Google Gemini Client
try:
    import google.generativeai as genai
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        genai.configure(api_key=gemini_key)
except (ImportError, ValueError):
    genai = None

def call_llm_openai(system_prompt: str, user_input: str) -> str:
    """Call OpenAI's GPT model"""
    if not openai_client:
        raise RuntimeError("OpenAI client not initialized. Check OPENAI_API_KEY.")
    
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

def call_llm_gemini(system_prompt: str, user_input: str) -> str:
    """Call Google Gemini model"""
    if not genai:
        raise RuntimeError("Google Generative AI not initialized. Check GOOGLE_API_KEY.")
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_prompt
    )
    
    response = model.generate_content(user_input)
    return response.text

# Default to OpenAI, but allow switching via environment variable
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

def call_llm(system_prompt: str, user_input: str) -> str:
    """
    Unified LLM interface - routes to configured provider.
    Supports: 'openai' or 'gemini'
    """
    if LLM_PROVIDER == "gemini":
        return call_llm_gemini(system_prompt, user_input)
    elif LLM_PROVIDER == "openai":
        return call_llm_openai(system_prompt, user_input)
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}. Use 'openai' or 'gemini'.")

# Export for use
__all__ = ["call_llm", "call_llm_openai", "call_llm_gemini"]