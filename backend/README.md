# UniSphere AI - Backend Service

This is the FastAPI backend service for UniSphere AI.

## Project Structure

```text
backend/
├── app/
│   ├── api/            # API endpoints & routing
│   ├── core/           # Configuration, security & core settings
│   ├── models/         # SQLAlchemy database models
│   ├── schemas/        # Pydantic data schemas
│   ├── services/       # Business logic services
│   ├── repositories/   # Database access layer
│   ├── database/       # Database sessions & engine setup
│   └── main.py         # FastAPI application entry point
├── tests/              # Backend unit and integration tests
├── requirements.txt    # Python dependencies
└── README.md           # Backend documentation
```

## Running Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

4. View API Documentation:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`
