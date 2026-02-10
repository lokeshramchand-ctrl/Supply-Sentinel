# LLM Configuration Guide

SupplySentinel uses **Google Gemini** as the primary language model provider.

> **Note:** OpenAI support is disabled. Only Gemini is active.

## Setup

### 1. Add API Key to `.env`

Copy `.env.example` and update with your Gemini API key:

```bash
cp .env.example .env
```

**For Google Gemini:**
```env
GEMINI_API_KEY=your-gemini-api-key-here
```

Get your key from: https://aistudio.google.com/app/apikey

### 2. LLM Provider Selection

Gemini is the default and only active provider:

```env
LLM_PROVIDER=gemini
```

OpenAI support is disabled and commented out in the code.

## Usage

The application automatically uses Gemini. No configuration needed beyond setting `GEMINI_API_KEY`.

### Starting the application:
```bash
docker-compose up --build
```

## Models Used

- **Gemini**: `gemini-1.5-flash` (lightweight, free tier friendly)

## Validation

On startup, the backend automatically:
1. ✅ Checks for Gemini API key
2. ✅ Tests the connection with a simple API call
3. ✅ Seeds the database with sample data
4. ✅ Starts the server

Look for logs like:
```
🔑 Google Gemini API Key: AIza...
✅ Gemini API key is valid and working!
```

## Programmatic Usage

The recommended way to use the LLM:

```python
from agents.llm_client import call_llm

# Use Gemini (default and only active provider)
response = call_llm(system_prompt, user_input)
```

> **Note:** `call_llm_openai()` is deprecated and disabled.

## Troubleshooting

**"GEMINI_API_KEY not found"**
- Set `GEMINI_API_KEY` in your `.env` file
- Ensure it's a valid Google Gemini API key from: https://aistudio.google.com/app/apikey

**API validation fails at startup**
- Check your internet connection - the API key is validated with a test request
- Verify the API key is correct and active

## Environment Variables Summary

| Variable | Required | Default | Example |
|----------|----------|---------|---------|
| `GEMINI_API_KEY` | ✅ Yes | - | `AIza...` |
| `LLM_PROVIDER` | No | `gemini` | `gemini` |
