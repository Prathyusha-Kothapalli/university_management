from fastapi import FastAPI

app = FastAPI(
    title="UniSphere AI Service",
    version="0.1.0",
    description="Dedicated AI microservice for UniSphere AI Platform"
)

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "service": "UniSphere AI Microservice",
        "message": "AI Service foundation ready"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai"
    }
