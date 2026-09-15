import uuid
import re
from typing import List, Dict, Any, Tuple
try:
    from models.study_assistant import (
        StudyAssistantRequest,
        StudyAssistantResponse,
        SourceCitation,
        ExplanationMode
    )
    from rag.knowledge_base import COURSES, COURSE_DOCUMENTS
except ImportError:
    from app.models.study_assistant import (
        StudyAssistantRequest,
        StudyAssistantResponse,
        SourceCitation,
        ExplanationMode
    )
    from app.rag.knowledge_base import COURSES, COURSE_DOCUMENTS


class StudyAssistantService:
    @staticmethod
    def get_available_courses() -> List[Dict[str, Any]]:
        return COURSES

    @staticmethod
    def retrieve_relevant_sources(course_id: str, question: str) -> List[SourceCitation]:
        docs = COURSE_DOCUMENTS.get(course_id, COURSE_DOCUMENTS["CS101"])
        question_lower = question.lower()
        question_words = set(re.findall(r'\w+', question_lower))

        scored_docs: List[Tuple[float, Dict[str, Any]]] = []

        for doc in docs:
            score = 0.5  # Base relevance for course match
            keyword_matches = sum(1 for kw in doc["keywords"] if kw in question_lower or any(w in kw for w in question_words))
            if keyword_matches > 0:
                score += min(0.48, keyword_matches * 0.16)
            
            # Content word overlap
            content_words = set(re.findall(r'\w+', doc["content"].lower()))
            overlap = len(question_words.intersection(content_words))
            score += min(0.25, overlap * 0.04)

            scored_docs.append((min(0.99, score), doc))

        # Sort by relevance score descending
        scored_docs.sort(key=lambda x: x[0], reverse=True)

        sources = []
        for score, doc in scored_docs[:3]:
            sources.append(
                SourceCitation(
                    title=doc["title"],
                    snippet=doc["content"],
                    page=doc["page"],
                    relevance_score=round(score, 2)
                )
            )
        return sources

    @classmethod
    def generate_response(cls, request: StudyAssistantRequest) -> StudyAssistantResponse:
        conv_id = request.conversation_id or f"conv_{uuid.uuid4().hex[:8]}"
        sources = cls.retrieve_relevant_sources(request.course_id, request.question)
        top_source = sources[0] if sources else None
        top_score = top_source.relevance_score if top_source else 0.85

        # Format prompt / context RAG pipeline
        answer, follow_ups = cls._synthesize_answer(
            question=request.question,
            course_id=request.course_id,
            mode=request.mode,
            top_source=top_source
        )

        return StudyAssistantResponse(
            answer=answer,
            sources=sources,
            confidence=round(top_score, 2),
            conversation_id=conv_id,
            course_id=request.course_id,
            mode=request.mode,
            follow_up_questions=follow_ups
        )

    @classmethod
    def _synthesize_answer(
        cls,
        question: str,
        course_id: str,
        mode: ExplanationMode,
        top_source: Any
    ) -> Tuple[str, List[str]]:
        q_lower = question.lower()
        course_name = next((c["name"] for c in COURSES if c["id"] == course_id), course_id)

        # 1. Topic Identification
        if any(w in q_lower for w in ["avl", "tree", "bst", "rotation", "balance"]):
            return cls._answer_avl_trees(mode)
        elif any(w in q_lower for w in ["dijkstra", "shortest path", "graph", "bfs", "dfs"]):
            return cls._answer_dijkstra_graphs(mode)
        elif any(w in q_lower for w in ["dp", "dynamic programming", "memoization", "knapsack"]):
            return cls._answer_dynamic_programming(mode)
        elif any(w in q_lower for w in ["deadlock", "mutex", "semaphore", "process", "thread", "concurrency"]):
            return cls._answer_concurrency_deadlocks(mode)
        elif any(w in q_lower for w in ["eigenvalue", "eigenvector", "svd", "matrix"]):
            return cls._answer_linear_algebra(mode)
        elif any(w in q_lower for w in ["transformer", "attention", "neural", "deep learning", "backpropagation"]):
            return cls._answer_deep_learning(mode)
        else:
            return cls._answer_generic_academic(question, course_name, mode, top_source)

    @staticmethod
    def _answer_avl_trees(mode: ExplanationMode) -> Tuple[str, List[str]]:
        if mode == "beginner":
            answer = (
                "### 🌲 AVL Trees Explained Simply (Beginner Mode)\n\n"
                "Imagine a bookshelf where you store numbered books in order (like a Binary Search Tree). "
                "If you keep adding books in increasing order (1, 2, 3, 4, 5), your shelf becomes a straight long line, "
                "making it slow to find anything!\n\n"
                "**An AVL Tree is like a smart librarian** that checks the height after every book is added:\n"
                "- If one side gets more than **1 level taller** than the other, the tree performs a quick **'rotation'** (pivot).\n"
                "- This keeps the tree balanced like a healthy bushy tree rather than a stick.\n\n"
                "**Key takeaway:** Searching, adding, and deleting items is always blazing fast: **O(log N)**."
            )
        elif mode == "code":
            answer = (
                "### 💻 AVL Tree Node & Rotation Implementation (Python)\n\n"
                "```python\n"
                "class AVLNode:\n"
                "    def __init__(self, key):\n"
                "        self.key = key\n"
                "        self.left = None\n"
                "        self.right = None\n"
                "        self.height = 1\n\n"
                "def get_height(node):\n"
                "    return node.height if node else 0\n\n"
                "def get_balance(node):\n"
                "    return get_height(node.left) - get_height(node.right) if node else 0\n\n"
                "def right_rotate(y):\n"
                "    x = y.left\n"
                "    T2 = x.right\n"
                "    # Perform rotation\n"
                "    x.right = y\n"
                "    y.left = T2\n"
                "    # Update heights\n"
                "    y.height = 1 + max(get_height(y.left), get_height(y.right))\n"
                "    x.height = 1 + max(get_height(x.left), get_height(x.right))\n"
                "    return x\n"
                "```\n\n"
                "**Complexity Analysis:**\n"
                "- **Time Complexity:** Rotations execute in $O(1)$ constant time.\n"
                "- **Lookup / Insert / Delete:** Strictly bounded to $O(\\log N)$ worst-case."
            )
        elif mode == "exam_summary":
            answer = (
                "### ⚡ Exam Quick Revision: AVL Trees\n\n"
                "- **Definition:** Self-balancing BST where Balance Factor $\\text{BF}(v) = h_{\\text{left}} - h_{\\text{right}} \\in \\{-1, 0, 1\\}$.\n"
                "- **Rebalancing Cases:**\n"
                "  1. **Left-Left (LL):** Single Right Rotation\n"
                "  2. **Right-Right (RR):** Single Left Rotation\n"
                "  3. **Left-Right (LR):** Left Rotate left child, then Right Rotate root\n"
                "  4. **Right-Left (RL):** Right Rotate right child, then Left Rotate root\n"
                "- **Worst-Case Heights:** Height $h < 1.44 \\log_2(N + 2)$.\n"
                "- **Exam Trap:** Remember to update height values from bottom-up after rotations!"
            )
        else: # detailed
            answer = (
                "### 🎯 In-Depth Analysis: AVL Trees & Self-Balancing Mechanisms\n\n"
                "An **AVL Tree** (Adelson-Velsky and Landis) is a self-balancing binary search tree. "
                "The core invariant maintained across all mutations is the **Strict Balance Factor**:\n\n"
                "$$\\text{BalanceFactor}(N) = \\text{Height}(\\text{LeftChild}) - \\text{Height}(\\text{RightChild})$$\n\n"
                "For every node $N$ in a valid AVL tree, $\\text{BalanceFactor}(N) \\in \\{-1, 0, +1\\}$.\n\n"
                "#### 1. Rebalancing Rotations\n"
                "When an insertion or deletion violates the balance condition ($|\\text{BF}| \\ge 2$), four symmetric rotation operations restore balance:\n"
                "- **Single Rotations:**\n"
                "  - **LL Case:** Insertion into the left subtree of the left child $\\rightarrow$ Single Right Rotation ($O(1)$).\n"
                "  - **RR Case:** Insertion into the right subtree of the right child $\\rightarrow$ Single Left Rotation ($O(1)$).\n"
                "- **Double Rotations:**\n"
                "  - **LR Case:** Left-rotate left child, followed by Right-rotate root.\n"
                "  - **RL Case:** Right-rotate right child, followed by Left-rotate root.\n\n"
                "#### 2. Asymptotic Complexities\n"
                "| Operation | Average Case | Worst Case | Space Complexity |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| Search | $O(\\log N)$ | $O(\\log N)$ | $O(1)$ |\n"
                "| Insertion | $O(\\log N)$ | $O(\\log N)$ | $O(1)$ |\n"
                "| Deletion | $O(\\log N)$ | $O(\\log N)$ | $O(1)$ |"
            )

        follow_ups = [
            "How does an AVL Tree compare with a Red-Black Tree in lookup vs insertion heavy workloads?",
            "Can you provide a step-by-step trace of inserting keys [10, 20, 30, 40, 50] into an empty AVL tree?",
            "What is the maximum height of an AVL tree with N nodes?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_dijkstra_graphs(mode: ExplanationMode) -> Tuple[str, List[str]]:
        answer = (
            "### 🗺️ Dijkstra's Shortest Path Algorithm\n\n"
            "Dijkstra's Algorithm computes the shortest path from a single source vertex to all other vertices in a directed or undirected graph with **non-negative edge weights**.\n\n"
            "#### How it Works:\n"
            "1. Initialize distances: $dist[source] = 0$, all other $dist[v] = \\infty$.\n"
            "2. Maintain a Min-Priority Queue of unvisited nodes keyed on current shortest distance.\n"
            "3. Greedily extract vertex $u$ with minimum distance and relax all adjacent edges $(u, v)$:\n"
            "   $$\\text{if } dist[u] + weight(u, v) < dist[v] \\implies dist[v] = dist[u] + weight(u, v)$$\n\n"
            "**Time Complexity:** $O((|V| + |E|) \\log |V|)$ using a Binary Min-Heap."
        )
        follow_ups = [
            "Why does Dijkstra fail on graphs with negative edge weights?",
            "How does the Bellman-Ford algorithm solve the negative weight cycle problem?",
            "How does the A* search heuristic optimize Dijkstra for spatial pathfinding?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_dynamic_programming(mode: ExplanationMode) -> Tuple[str, List[str]]:
        answer = (
            "### 🧩 Dynamic Programming (DP) Principles\n\n"
            "Dynamic Programming applies to optimization problems exhibiting two key properties:\n"
            "1. **Optimal Substructure:** Optimal solution to problem contains optimal solutions to subproblems.\n"
            "2. **Overlapping Subproblems:** Subproblems are evaluated repeatedly.\n\n"
            "#### Approaches:\n"
            "- **Top-Down (Memoization):** Recursive approach with hash table or array cache.\n"
            "- **Bottom-Up (Tabulation):** Iterative state transitions filling an array in topological dependency order.\n\n"
            "**Canonical Example:** The 0/1 Knapsack problem with state $DP[i][w] = \\max(DP[i-1][w], DP[i-1][w - wt[i]] + val[i])$."
        )
        follow_ups = [
            "What is the difference between 0/1 Knapsack and Fractional Knapsack?",
            "How do we optimize DP space complexity from 2D table to 1D rolling array?",
            "Can you explain the Longest Common Subsequence (LCS) state recurrence?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_concurrency_deadlocks(mode: ExplanationMode) -> Tuple[str, List[str]]:
        answer = (
            "### 🔒 OS Concurrency, Synchronization & Deadlocks\n\n"
            "A **Deadlock** is a state where a set of processes are blocked because each process is holding a resource and waiting for another resource held by another process.\n\n"
            "#### The 4 Coffman Necessary Conditions:\n"
            "1. **Mutual Exclusion:** At least one resource is held in non-shareable mode.\n"
            "2. **Hold and Wait:** A process is holding resources while waiting for additional ones.\n"
            "3. **No Preemption:** Resources cannot be forcibly taken away before completion.\n"
            "4. **Circular Wait:** A closed cycle of processes where $P_0 \\rightarrow P_1 \\rightarrow \\dots \\rightarrow P_n \\rightarrow P_0$.\n\n"
            "**Resolution:** Dijkstra's Banker's Algorithm prevents deadlock by verifying safe states before allocation."
        )
        follow_ups = [
            "How does a Counting Semaphore differ from a Mutex Lock?",
            "Explain the Banker's Algorithm safety check with a matrix example.",
            "What is Priority Inversion and how does Priority Inheritance solve it?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_linear_algebra(mode: ExplanationMode) -> Tuple[str, List[str]]:
        answer = (
            "### 📐 Linear Algebra: Eigenvalues & Diagonalization\n\n"
            "For an $n \\times n$ square matrix $A$:\n\n"
            "$$A \\mathbf{v} = \\lambda \\mathbf{v} \\iff (A - \\lambda I) \\mathbf{v} = \\mathbf{0}$$\n\n"
            "1. **Characteristic Equation:** Non-trivial solutions exist if and only if $\\det(A - \\lambda I) = 0$.\n"
            "2. **Eigenvector Calculation:** Null space $\\text{Null}(A - \\lambda I)$.\n"
            "3. **Diagonalization:** $A = P D P^{-1}$ where columns of $P$ are linearly independent eigenvectors and $D = \\text{diag}(\\lambda_1, \\dots, \\lambda_n)$."
        )
        follow_ups = [
            "How does Singular Value Decomposition (SVD) extend diagonalization to non-square matrices?",
            "What is the geometric meaning of eigenvalues in coordinate transformations?",
            "How are eigenvalues used in Principal Component Analysis (PCA) for dimensionality reduction?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_deep_learning(mode: ExplanationMode) -> Tuple[str, List[str]]:
        answer = (
            "### 🤖 Transformer Architecture & Self-Attention\n\n"
            "The Transformer architecture replaces recurrent connections with multi-head self-attention mechanisms:\n\n"
            "$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left( \\frac{Q K^T}{\\sqrt{d_k}} \\right) V$$\n\n"
            "- **Query ($Q$), Key ($K$), Value ($V$):** Projections of input token embeddings through learned weight matrices $W_Q, W_K, W_V$.\n"
            "- **Scaling Factor $\\sqrt{d_k}$:** Prevents extremely large dot-product magnitudes that push softmax into regions with vanishing gradients.\n"
            "- **Multi-Head Attention:** Enables models to attend to information from different representation subspaces concurrently."
        )
        follow_ups = [
            "Why is positional encoding necessary in transformers?",
            "How does FlashAttention optimize memory bandwidth in GPU SRAM?",
            "What is the difference between Encoder-only (BERT), Decoder-only (GPT), and Encoder-Decoder (T5) models?"
        ]
        return answer, follow_ups

    @staticmethod
    def _answer_generic_academic(question: str, course_name: str, mode: ExplanationMode, top_source: Any) -> Tuple[str, List[str]]:
        source_title = top_source.title if top_source else f"{course_name} Core Syllabus"
        source_snippet = top_source.snippet if top_source else ""

        answer = (
            f"### 🎓 Study Assistance: {course_name}\n\n"
            f"**Regarding your question:** *\"{question}\"*\n\n"
            f"Based on the official syllabus materials from **{source_title}**:\n\n"
            f"> \"{source_snippet}\"\n\n"
            f"#### Key Conceptual Breakdown ({mode.replace('_', ' ').title()} Mode):\n"
            f"1. **Core Principle:** In higher education curriculum for {course_name}, this concept establishes foundational analytical patterns.\n"
            f"2. **Methodology:** Break the problem into defined inputs, invariants, transition states, and rigorous output verification.\n"
            f"3. **Practical Application:** Reviewing standard derivations and practice exercises ensures high exam readiness.\n"
        )
        follow_ups = [
            f"Can you provide a concrete step-by-step problem example on this topic in {course_name}?",
            "What are the most common exam questions asked on this concept?",
            "How does this connect with subsequent modules in the course?"
        ]
        return answer, follow_ups
