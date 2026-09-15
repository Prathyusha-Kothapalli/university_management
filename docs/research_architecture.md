# Research, Grants & Lab Inventory Architecture Documentation

## Overview
Research project tracking, grant applications, lab equipment booking, patent filings, journal publication records, peer review management.

## System Specifications
- Module Key: `research`
- Platform Layers: Backend (FastAPI), Web (React/TS), Mobile (Flutter), AI Engine (Python ML)
- Data Schemas: SQLAlchemy models with PostgreSQL database engine.

## API Contracts
- `GET /research/` - List entities
- `GET /research/{id}` - Get entity by ID
- `POST /research/` - Create new entity
