# 🤖 UniSphere AI Study Assistant Architecture & Specification

## 1. System Overview
The UniSphere AI Study Assistant is a high-performance, multi-mode RAG (Retrieval-Augmented Generation) copilot designed for higher education campuses. It enables students to query verified course syllabi, lecture slides, proofs, and formulas with guaranteed zero-hallucination grounding.

---

## 2. Microservice Architecture
- **Service Name**: `unisphere-ai`
- **Port**: `5001`
- **Framework**: FastAPI (Python 3.14 / Asynchronous ASGI)
- **Primary Routes**:
  - `POST /ai/study-assistant`: RAG retrieval and response synthesis.
  - `GET /ai/courses`: Available accredited curriculum catalog.
  - `POST /ai/feedback`: Continuous quality rating and telemetry.
  - `GET /health`: Microservice liveness and feature probing.

---

## 3. Explanation Modes
| Mode ID | Display Name | Characteristics |
| :--- | :--- | :--- |
| `detailed` | **Academic & Deep Dive** | Asymptotic analysis, formal mathematical proofs, and system derivations. |
| `beginner` | **Conceptual (ELIF5)** | Intuitive analogies, real-world examples, and accessible plain-English breakdowns. |
| `code` | **Code & Implementation** | Production-ready algorithms, data structures, and commented implementation walkthroughs. |
| `exam_summary` | **High-Yield Exam Prep** | Core bullet points, essential formulas, and common exam trap warnings. |

---

## 4. Grounded Course Modules
- **CS101**: Data Structures & Algorithms (AVL Trees, Graph Traversals, Shortest Paths).
- **CS202**: Operating Systems (Deadlock Avoidance, Banker's Algorithm, Virtual Memory).
- **MATH301**: Linear Algebra (Eigenvalues, SVD, Matrix Diagonalization).
- **AI401**: Deep Learning & Neural Networks (Transformer Attention, Backpropagation).
- **PHYS101**: Classical Mechanics & Electromagnetism (Maxwell's Equations, Lagrangian Dynamics).

---

## 5. Frontend Integration
- **Persistent Floating Bot Widget**: `web/src/components/AIBotWidget.tsx` (Drawer & modal copilot).
- **Dedicated Full-Screen Workspace**: `web/src/components/AIStudyAssistant.tsx` (Session management, search, and revision vault).
- **Design System**: Plus Jakarta Sans, JetBrains Mono, translucent frosted glass panels (`.glass-panel`), glowing badges, and responsive view layouts.
