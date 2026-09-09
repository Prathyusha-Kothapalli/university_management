# Architecture Overview - UniSphere AI

UniSphere AI is built with a microservices-inspired multi-tenant architecture designed to scale across universities, campuses, and user roles (Students, Faculty, Staff, Administrators, Super Admins).

## High-Level Architecture Diagram

```text
React Web
     ↓
Python FastAPI
     ↓
PostgreSQL

Flutter Mobile
     ↓
Python FastAPI

Python AI Services
     ↓
Backend / AI Models
```

---

## Component Breakdown

1. **Web Client (React + TypeScript)**
   - Single Page Application (SPA) built with Vite and TypeScript.
   - Provides administrative, faculty, and student portals.
   - Communicates with Python FastAPI over REST/HTTPS & WebSockets.

2. **Mobile App (Flutter + Dart)**
   - Cross-platform native application for iOS and Android.
   - Shared business logic and UI design system for mobile users.
   - Connects to Python FastAPI backend endpoints.

3. **Backend Core (Python + FastAPI)**
   - High-performance asynchronous API server.
   - Handles authentication, tenant isolation, business domain services, and database persistence.
   - Interacts with PostgreSQL database and Redis caching layer.

4. **AI Microservice (Python)**
   - Independent AI service handling RAG (Retrieval-Augmented Generation), vector store querying, intelligent copilot assistance, and ML analytics.
   - Integrates directly with Backend services and LLM providers.

5. **Data & Storage Layer**
   - **PostgreSQL**: Primary relational database with multi-tenant Row-Level Security (RLS).
   - **Redis**: High-speed caching, session management, and pub/sub message queue.
