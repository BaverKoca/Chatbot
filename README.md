# LLaMA3 Internet QA Bot

A modern, production-ready Retrieval-Augmented Generation (RAG) chatbot that answers user questions using the LLaMA 3:8B model (via Ollama) and always brings you the latest information from the web.

---

## 🚀 Features
- **LLaMA 3:8B (Ollama):** Fast, local LLM-powered answers
- **Retrieval-Augmented Generation:** Always searches Google for the latest info and provides sources
- **Source Attribution:** Answers include links to original web sources
- **Web Search Filtering:** Prioritizes Wikipedia and official domains for trustworthy results
- **Chunking & Ranking:** Only the most relevant web snippets are sent to the LLM
- **Caching:** Fast repeated answers for similar questions
- **User Feedback:** Like/dislike answers to help improve the system
- **Modern Web UI:** Minimalist, responsive chat interface
- **REST API:** Built with FastAPI for easy integration

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
8. **Open the chat UI**
   - Go to [http://localhost:8000/](http://localhost:8000/) in your browser.

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
    "answer": "Paris is the capital of France.\nSource: https://en.wikipedia.org/wiki/Paris",
    "source": "internet+llama"
  }
  ```

### Submit Feedback
- **Endpoint:** `POST /feedback`
- **Request Body:**
  ```json
  {
    "question": "What is the capital of France?",
    "answer": "Paris is the capital of France.",
    "rating": 1 // 1=like, 0=dislike
  }
  ```

---

## 📝 Notes & Best Practices
- Requires **Python 3.8+**
- For production, always secure your API and environment variables
- You can extend the API with authentication, logging, or a web frontend
- If you encounter issues with summarization, ensure PyTorch or TensorFlow is installed
- For best results, use a valid Google Custom Search Engine set to search the entire web

---

## 🤝 Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License.