# Chatbot

# LLaMA3 Internet QA Bot

A professional FastAPI-based chatbot that answers user questions using the LLaMA 3:8B model (via Ollama). If the model is uncertain, it searches the web and summarizes the results for a more accurate answer.

## Features
- Uses LLaMA 3:8B (Ollama CLI) for initial answers
- Google Custom Search API for web search fallback
- Summarizes top web results using transformers
- REST API with FastAPI

## Setup
1. Clone the repo and enter the directory.
2. Copy `.env.example` to `.env` and fill in your Google API keys.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Make sure Ollama is installed and the LLaMA3:8B model is available:
   ```sh
   ollama pull llama3:8b
   ```
5. Start the API:
   ```sh
   uvicorn app.main:app --reload
   ```

## API Usage
POST `/ask`
```json
{
  "question": "What is the capital of France?"
}
```

Response:
```json
{
  "answer": "Paris is the capital of France.",
  "source": "llama" // or "internet+llama"
}
```

## Notes
- Requires Python 3.8+
- For production, secure your API and environment variables.