#!/usr/bin/env python3
"""
Validate environment variables before starting the application.
"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def validate_openai_key():
    """Validate OpenAI API key"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("⚠️  OPENAI_API_KEY not found")
        return False
    
    if not api_key.startswith("sk-"):
        print(f"⚠️  OPENAI_API_KEY doesn't start with 'sk-' (found: {api_key[:10]}...)")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        print(f"🔑 OpenAI API Key: {api_key[:10]}...{api_key[-4:]}")
        print("🧪 Testing OpenAI API connection...")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=5
        )
        
        print("✅ OpenAI API key is valid and working!")
        print(f"   Model: {response.model}")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API key validation failed: {str(e)}")
        return False

def validate_gemini_key():
    """Validate Google Gemini API key"""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("⚠️  GEMINI_API_KEY not found")
        return False
    
    print(f"🔑 Google Gemini API Key: {api_key[:10]}...{api_key[-4:]}")
    print("✅ Gemini API key is configured!")
    print("   Model: gemini-1.5-flash (lightweight, free tier friendly)")
    return True
    
    # Note: Removed API connection test to avoid exceeding free tier quota
    # The key will be validated on first API call

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔍 Validating Environment Configuration")
    print("="*60 + "\n")
    
    llm_provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    
    print(f"📌 LLM Provider: {llm_provider}\n")
    
    # Always validate the configured provider
    if llm_provider == "gemini":
        if not validate_gemini_key():
            print("\n⚠️  Gemini validation failed!")
            sys.exit(1)
    elif llm_provider == "openai":
        print("⚠️  OpenAI support is disabled. Using Gemini instead.")
        if not validate_gemini_key():
            print("\n⚠️  Gemini validation failed!")
            sys.exit(1)
    else:
        print(f"❌ Unknown LLM_PROVIDER: {llm_provider}")
        print("   Use 'gemini' (default)")
        sys.exit(1)
    
    print("\n✅ All environment checks passed!")
    print("="*60 + "\n")
