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
        print("❌ ERROR: OPENAI_API_KEY not found in environment")
        print("   Please set OPENAI_API_KEY in your .env file")
        return False
    
    if not api_key.startswith("sk-"):
        print(f"⚠️  WARNING: OPENAI_API_KEY doesn't start with 'sk-' (found: {api_key[:10]}...)")
        print("   This might not be a valid OpenAI API key")
        return False
    
    # Test the API key with a simple request
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        print(f"🔑 OpenAI API Key found: {api_key[:10]}...{api_key[-4:]}")
        print("🧪 Testing OpenAI API connection...")
        
        # Make a minimal test request
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=5
        )
        
        print("✅ OpenAI API key is valid and working!")
        print(f"   Model: {response.model}")
        print(f"   Response ID: {response.id}")
        return True
        
    except Exception as e:
        print(f"❌ ERROR: OpenAI API key validation failed")
        print(f"   Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔍 Validating Environment Configuration")
    print("="*60 + "\n")
    
    if not validate_openai_key():
        print("\n⚠️  Environment validation failed!")
        print("   The application will start but may not function correctly.\n")
        sys.exit(1)
    
    print("\n✅ All environment checks passed!")
    print("="*60 + "\n")
