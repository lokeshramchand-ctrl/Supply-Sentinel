# LLM Configuration Guide

SupplySentinel supports both **OpenAI** and **Google Gemini** as language model providers.

## Setup

### 1. Add API Keys to `.env`

Copy `.env.example` and update with your API keys:

```bash
cp .env.example .env
```

**For OpenAI:**
```env
OPENAI_API_KEY=sk-proj-your-full-openai-key-here
```

Get your key from: https://platform.openai.com/api-keys

**For Google Gemini:**
```env
GEMINI_API_KEY=your-gemini-api-key-here
```

Get your key from: https://aistudio.google.com/app/apikey

### 2. Choose Your LLM Provider

Set `LLM_PROVIDER` in `.env`:

```env
# Use OpenAI (default)
LLM_PROVIDER=openai

# Or use Gemini
LLM_PROVIDER=gemini
```

## Usage

The application automatically uses the configured provider. No code changes needed!

### Starting with OpenAI:
```bash
export LLM_PROVIDER=openai
docker-compose up
```

### Starting with Gemini:
```bash
export LLM_PROVIDER=gemini
docker-compose up
```

## Models Used

- **OpenAI**: `gpt-4o-mini`
- **Gemini**: `gemini-1.5-flash`

## Validation

On startup, the backend automatically:
1. ✅ Checks for the configured API key
2. ✅ Tests the connection with a simple API call
3. ✅ Seeds the database with sample data
4. ✅ Starts the server

Look for logs like:
```
🔑 OpenAI API Key: sk-proj-...
✅ OpenAI API key is valid and working!
```

Or for Gemini:
```
🔑 Google Gemini API Key: AIza...
✅ Gemini API key is valid and working!
```

## Programmatic Usage

If you need to use specific providers in code:

```python
from agents.llm_client import call_llm_openai, call_llm_gemini

# Use OpenAI specifically
response = call_llm_openai(system_prompt, user_input)

# Use Gemini specifically
response = call_llm_gemini(system_prompt, user_input)

# Use configured provider (recommended)
from agents.llm_client import call_llm
response = call_llm(system_prompt, user_input)
```

## Troubleshooting

**"OPENAI_API_KEY not found"**
- Set `OPENAI_API_KEY` in your `.env` file
- Ensure `.env` is in the root directory

**"GEMINI_API_KEY not found"**
- Set `GEMINI_API_KEY` in your `.env` file
- Ensure it's a valid Google Gemini API key

**"Unknown LLM_PROVIDER"**
- Check `LLM_PROVIDER` is set to `openai` or `gemini`
- Default is `openai` if not specified

## Environment Variables Summary

| Variable | Required | Example |
|----------|----------|---------|
| `OPENAI_API_KEY` | For OpenAI provider | `sk-proj-...` |
| `GEMINI_API_KEY` | For Gemini provider | `AIza...` |
| `LLM_PROVIDER` | No (default: openai) | `openai` or `gemini` |
