# LLaMA3 Internet QA Bot

A professional, production-ready chatbot API that answers user questions using the LLaMA 3:8B model (via Ollama). If the model is uncertain, it automatically searches the web, summarizes the most relevant results, and generates a reliable answer.

---

## 🚀 Features
- **LLaMA 3:8B (Ollama CLI):** Fast, local LLM-powered answers
- **Web Search Fallback:** Uses Google Custom Search API for up-to-date information
- **Automatic Summarization:** Summarizes top web results using Hugging Face Transformers
- **REST API:** Built with FastAPI for easy integration
- **Environment-based Secrets:** Secure API keys with `.env` files
- **Modular, Extensible Codebase:** Clean architecture for easy customization

---

## 🛠️ Setup & Installation

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd Chatbot
   ```
2. **Create and configure your environment variables**
   - Copy `.env.example` to `.env` and fill in your Google API keys:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     GOOGLE_CSE_ID=your_custom_search_engine_id
     ```
3. **(Recommended) Create and activate a virtual environment**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Install Ollama and the LLaMA3:8B model**
   - [Download Ollama](https://ollama.com/download)
   - Pull the model:
     ```sh
     ollama pull llama3:8b
     ```
6. **Start the Ollama service** (if not already running)
   ```sh
   ollama serve
   ```
7. **Run the FastAPI server**
   ```sh
   uvicorn app.main:app --reload
   ```

---

## 📚 API Usage

### Ask a Question
- **Endpoint:** `POST /ask`
- **Request Body:**
  ```json
  {
    "question": "What is the capital of France?"
  }
  ```
- **Response:**
  ```json
  {
    "answer": "Paris is the capital of France.",
    "source": "llama" // or "internet+llama"
  }
  ```

---

## 📝 Notes & Best Practices
- Requires **Python 3.8+**
- For production, always secure your API and environment variables
- You can extend the API with authentication, logging, or a web frontend
- If you encounter issues with summarization, ensure PyTorch or TensorFlow is installed

---

## 🤝 Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License.