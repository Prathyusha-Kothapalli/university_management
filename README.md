# UniSphere AI

**UniSphere AI** is an enterprise-grade, multi-tenant university management platform designed to streamline administrative, academic, AI-driven, and student operations across higher education institutions.

---

## 🎯 Project Overview

UniSphere AI provides a unified digital ecosystem supporting multi-tenancy for diverse universities, campuses, and departments. The system integrates traditional university management functions with modern AI capabilities.

### Team Organization (4 Developers)

| Role | Developer Responsibilities |
| :--- | :--- |
| **Backend & Database Engineer** | FastAPI core APIs, PostgreSQL schema design, database migrations, security & multi-tenancy isolation. |
| **Frontend Web Engineer** | React + TypeScript web portal, layout system, component library, state management, and user experience. |
| **Mobile Applications Engineer** | Flutter cross-platform mobile app (iOS & Android) for students, faculty, and administrators. |
| **AI & Infrastructure Engineer** | Python AI microservice, RAG pipelines, model integration, Docker containerization, Redis caching, and DevOps. |

---

## 🛠️ Technology Stack

* **Web Frontend:** React + TypeScript (Vite)
* **Backend Services:** Python + FastAPI
* **Mobile Application:** Flutter + Dart
* **AI Microservice:** Python (FastAPI / LangChain / RAG ready)
* **Database:** PostgreSQL
* **Caching & Message Broker:** Redis
* **Containerization:** Docker & Docker Compose
* **Version Control:** Git + GitHub

---

## 📁 Repository Structure

```text
unisphere-ai/
│
├── backend/            # FastAPI backend application (REST APIs, Auth, Business logic placeholders)
├── web/                # React + TypeScript web application
├── mobile/             # Flutter + Dart mobile application
├── ai/                 # Python AI microservice & ML pipeline foundation
├── database/           # PostgreSQL migrations, seed data, and schema definitions
├── infrastructure/     # Dockerfiles, Nginx configurations, and deployment tools
├── docs/               # System documentation, architecture diagrams, and setup guides
├── scripts/            # Helper & setup scripts for local development
├── tests/              # Root integration & end-to-end test suite
├── .gitignore          # Project gitignore
├── docker-compose.yml  # Local multi-container development environment
└── README.md           # Project documentation
```

---

## 🚀 Development Setup

### Prerequisites

* [Docker](https://www.docker.com/) & Docker Compose
* [Python 3.11+](https://www.python.org/)
* [Node.js 18+](https://nodejs.org/)
* [Flutter SDK 3.x+](https://flutter.dev/)

### Running Locally with Docker Compose

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/unisphere-ai.git
   cd unisphere-ai
   ```

2. Launch the services:
   ```bash
   docker-compose up --build
   ```

3. Service Endpoints:
   * **Web Frontend:** `http://localhost:3000`
   * **Backend API:** `http://localhost:8000` (Swagger UI: `http://localhost:8000/docs`)
   * **AI Microservice:** `http://localhost:8001`
   * **PostgreSQL:** `localhost:5432`
   * **Redis:** `localhost:6379`

---

## 🔮 Planned Future Modules

The application architecture is structured to support incremental development of the following modules:

1. **Multi-Tenant Administration** (University onboarding, domain separation, role-based access control)
2. **Student & Faculty Management** (Profiles, enrollment, academic history)
3. **Academics & Course Management** (Curriculum, departments, semester scheduling)
4. **Attendance System** (Digital tracking, QR scanning, attendance reporting)
5. **Assignments & Submissions** (Coursework distribution and grading)
6. **Examinations & Results** (Exam schedules, mark sheets, transcript generation)
7. **Fee Management** (Invoicing, payment gateways, receipts)
8. **Library System** (Catalog, book issuing, fine management)
9. **Hostel Management** (Room allocation, mess management, gate passes)
10. **Transportation Services** (Route mapping, bus tracking, passes)
11. **Placement Portal** (Company drives, resumes, interview scheduling)
12. **AI Copilot & Smart Assistant** (Automated query resolution, student performance analytics, intelligent RAG document search)
