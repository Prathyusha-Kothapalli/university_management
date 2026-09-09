# Development Setup Guide

Guide for setting up local environments for developers contributing to UniSphere AI.

## Quick Start with Docker

```bash
# 1. Clone repo
git clone https://github.com/your-org/unisphere-ai.git
cd unisphere-ai

# 2. Boot up local environment
docker-compose up -d --build
```

## Service Ports

- Backend API: `8000`
- Web Frontend: `3000`
- AI Microservice: `8001`
- PostgreSQL: `5432`
- Redis: `6379`
