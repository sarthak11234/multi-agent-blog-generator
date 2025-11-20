# AI Capstone Multi-Agent System

A fully working multi-agent AI system using free HuggingFace models with Coordinator, Researcher, Writer, and Editor agents.

## Quick Start

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Activate virtual environment:**
   ```bash
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Start the server:**
   ```bash
   # Option 1: Using the startup script
   python start_server.py
   
   # Option 2: Using uvicorn directly
   uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The server will start at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies (if not already done):**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The frontend will typically start at `http://localhost:5173`

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /generate` - Generate content using multi-agent pipeline
- `GET /logs` - Fetch recent agent execution logs
- `GET /memory` - View long-term memory storage

## Troubleshooting

### Backend not starting

1. **Check if port 8000 is in use:**
   ```bash
   netstat -ano | findstr :8000
   ```

2. **Kill existing Python processes:**
   ```bash
   taskkill /F /IM python.exe
   ```

3. **Check Python version:**
   ```bash
   python --version
   ```
   Should be Python 3.11 or 3.10 (not 3.13 for compatibility)

4. **Verify virtual environment:**
   ```bash
   which python  # Should point to .venv
   pip list  # Should show installed packages
   ```

### Model Loading Issues

The system uses lazy loading - models are loaded on first use, not at startup. This allows the server to start quickly even if models aren't downloaded yet.

- If models fail to load, the system will use mock responses
- To use real models, ensure you have:
  - Sufficient disk space for model downloads
  - Internet connection for first-time downloads
  - Set `LLM_MODE` environment variable if needed

### Frontend can't connect to backend

1. **Check backend is running:**
   - Visit `http://localhost:8000/health` in browser
   - Should return `{"status":"ok"}`

2. **Check CORS settings:**
   - Backend has CORS enabled for all origins
   - If issues persist, check browser console for errors

3. **Verify API base URL:**
   - Frontend uses `http://localhost:8000` by default
   - Can be overridden with `VITE_API_BASE` environment variable

## Environment Variables

### Backend

- `LLM_MODE` - LLM mode: `transformers`, `gguf`, or `hf_api` (default: `transformers`)
- `LLM_MODEL_ID` - Model identifier (default: `google/gemma-2b-it`)
- `LLM_DEVICE` - Device: `cpu` or `cuda` (default: `cpu`)
- `HF_API_TOKEN` - HuggingFace API token (for `hf_api` mode)

### Frontend

- `VITE_API_BASE` - Backend API base URL (default: `http://localhost:8000`)

## Project Structure

```
capstone/
├── backend/
│   ├── agents/          # Agent implementations
│   ├── models/          # LLM wrappers
│   ├── tools/           # Search, SEO tools
│   ├── memory/          # Session & long-term memory
│   ├── services/        # Logging, evaluation
│   ├── main.py          # FastAPI application
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/       # React pages
│   │   ├── components/  # Reusable components
│   │   └── services/    # API client
│   └── package.json
└── README.md
```

## Features

- ✅ Multi-agent orchestration (Coordinator → Researcher → Writer → Editor)
- ✅ Multiple LLM backends (Transformers, GGUF, HuggingFace API)
- ✅ Session and long-term memory
- ✅ Request logging and evaluation metrics
- ✅ Modern React frontend with TailwindCSS
- ✅ Real-time agent trace visualization

## Notes

- Models are loaded lazily on first use to speed up server startup
- Mock responses are used if models fail to load
- All logs are saved to `backend/logs/`
- Long-term memory is stored in `backend/memory/long_term_store.json`

