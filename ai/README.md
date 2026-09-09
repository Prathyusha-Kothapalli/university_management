# UniSphere AI - AI Microservice

This is the dedicated Python AI service foundation for UniSphere AI.

## Project Structure

```text
ai/
├── app/          # FastAPI entry point & AI API routing
├── services/     # Model inference & AI business logic
├── models/       # LLM wrappers & local model definitions
├── prompts/      # Prompt templates & system instructions
├── rag/          # Vector search, embedding & retrieval-augmented generation
├── tests/        # AI service tests
├── requirements.txt
└── README.md
```

## Running Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the AI server:
   ```bash
   uvicorn app.main:app --reload --port 8001
   ```
