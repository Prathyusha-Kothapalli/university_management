"""
Course Knowledge Base and Retrieval Store for RAG-powered AI Study Assistant.
Contains indexed curriculum topics, lecture excerpts, textbook references, and exam notes.
"""
from typing import List, Dict, Any

COURSES = [
    {
        "id": "CS101",
        "name": "Data Structures & Algorithms",
        "code": "CS101",
        "department": "Computer Science",
        "description": "Core fundamentals of asymptotic analysis, trees, graphs, sorting, and dynamic programming."
    },
    {
        "id": "CS202",
        "name": "Operating Systems & Architecture",
        "code": "CS202",
        "department": "Computer Science",
        "description": "Processes, threads, CPU scheduling, concurrency, virtual memory, and file systems."
    },
    {
        "id": "MATH301",
        "name": "Linear Algebra & Matrix Theory",
        "code": "MATH301",
        "department": "Mathematics",
        "description": "Vector spaces, linear transformations, eigenvalues, eigenvectors, SVD, and matrix decomposition."
    },
    {
        "id": "PHYS101",
        "name": "Engineering Physics & Mechanics",
        "code": "PHYS101",
        "department": "Physics",
        "description": "Classical mechanics, thermodynamics, wave optics, and electromagnetic principles."
    },
    {
        "id": "AI401",
        "name": "Machine Learning & Neural Networks",
        "code": "AI401",
        "department": "Artificial Intelligence",
        "description": "Supervised learning, deep neural networks, transformer architectures, and RAG pipelines."
    }
]

COURSE_DOCUMENTS: Dict[str, List[Dict[str, Any]]] = {
    "CS101": [
        {
            "title": "CS101 Lecture 4: Self-Balancing Trees (AVL & Red-Black)",
            "page": "Slides 12-18",
            "keywords": ["avl", "tree", "binary search tree", "bst", "rotation", "balance factor", "red-black", "height"],
            "content": "An AVL tree is a self-balancing binary search tree where the difference between heights of left and right subtrees (balance factor) cannot be more than 1 for all nodes. When insertion or deletion causes balance factor to become >1 or <-1, rebalancing is performed using four rotation cases: LL, RR, LR, and RL. Lookup, Insertion, and Deletion all take guaranteed O(log N) worst-case time."
        },
        {
            "title": "CS101 Lecture 7: Graph Traversal & Shortest Path",
            "page": "Textbook Chapter 6, pp. 142-155",
            "keywords": ["graph", "bfs", "dfs", "dijkstra", "shortest path", "bellman-ford", "a*", "adjacency"],
            "content": "Dijkstra's Algorithm finds the single-source shortest path in weighted graphs with non-negative edge weights using a Min-Priority Queue in O((V + E) log V) time. For negative weights, the Bellman-Ford algorithm with O(V * E) time must be used instead."
        },
        {
            "title": "CS101 Lecture 9: Dynamic Programming & Memoization",
            "page": "Lecture Notes pp. 88-94",
            "keywords": ["dynamic programming", "dp", "memoization", "tabulation", "knapsack", "lcs", "fibonacci"],
            "content": "Dynamic Programming solves problems with overlapping subproblems and optimal substructure. Top-down DP uses recursion with memoization caching, while bottom-up DP constructs iterative table lookups. The 0/1 Knapsack problem operates in pseudo-polynomial time O(N * W)."
        },
        {
            "title": "CS101 Lecture 2: Asymptotic Notation & Complexity Analysis",
            "page": "Syllabus Unit 1, Slide 5",
            "keywords": ["big-o", "asymptotic", "time complexity", "space complexity", "omega", "theta", "worst case"],
            "content": "Big-O represents an asymptotic upper bound: f(n) = O(g(n)) if there exist positive constants c and n0 such that f(n) <= c*g(n) for all n >= n0. Big-Omega represents a lower bound, and Big-Theta represents an asymptotically tight bound."
        }
    ],
    "CS202": [
        {
            "title": "CS202 Unit 2: Process Synchronization & Concurrency",
            "page": "Silberschatz OS Textbook Ch. 5, pp. 210-230",
            "keywords": ["process", "thread", "mutex", "semaphore", "deadlock", "race condition", "critical section"],
            "content": "A race condition occurs when multiple threads manipulate shared data concurrently and the outcome depends on execution order. Mutual exclusion is achieved via Mutex locks, Counting/Binary Semaphores, and Monitors. Deadlock requires four Coffman conditions: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait."
        },
        {
            "title": "CS202 Unit 4: Virtual Memory & Page Replacement",
            "page": "Lecture Slides 22-30",
            "keywords": ["virtual memory", "paging", "page fault", "tlb", "lru", "fifo", "thrashing", "mmu"],
            "content": "Virtual memory maps logical addresses to physical frames via the Page Table and Translation Lookaside Buffer (TLB). Page replacement algorithms include FIFO (susceptible to Belady's Anomaly), LRU (Least Recently Used), and Optimal Page Replacement."
        }
    ],
    "MATH301": [
        {
            "title": "MATH301 Chapter 4: Eigenvalues and Eigenvectors",
            "page": "Strang Linear Algebra, pp. 280-295",
            "keywords": ["eigenvalue", "eigenvector", "characteristic polynomial", "determinant", "diagonalization", "matrix"],
            "content": "For an n x n square matrix A, a non-zero vector v is an eigenvector and lambda is an eigenvalue if A*v = lambda*v, equivalent to det(A - lambda*I) = 0. Diagonalization A = P*D*P^(-1) is possible when A has n linearly independent eigenvectors."
        },
        {
            "title": "MATH301 Chapter 6: Singular Value Decomposition (SVD)",
            "page": "Matrix Computations Handbook pp. 110-125",
            "keywords": ["svd", "singular value", "orthogonal", "pca", "rank", "pseudoinverse"],
            "content": "Singular Value Decomposition factors any real m x n matrix A into A = U * Sigma * V^T, where U (m x m) and V (n x n) are orthogonal matrices, and Sigma is an m x n diagonal matrix containing non-negative singular values ordered by magnitude."
        }
    ],
    "PHYS101": [
        {
            "title": "PHYS101 Unit 3: Rotational Mechanics & Angular Momentum",
            "page": "Halliday & Resnick Fundamentals of Physics, Ch. 10",
            "keywords": ["torque", "angular momentum", "moment of inertia", "rotational", "kinetic energy", "conservation"],
            "content": "Rotational kinetic energy is K_rot = 1/2 * I * omega^2 where I is moment of inertia. Angular momentum L = I * omega is conserved in the absence of net external torque tau = dL/dt = r x F."
        },
        {
            "title": "PHYS101 Unit 6: Thermodynamics & Heat Engines",
            "page": "Thermodynamics Lecture Notes, pp. 45-52",
            "keywords": ["thermodynamics", "entropy", "carnot", "heat engine", "first law", "second law", "efficiency"],
            "content": "The First Law of Thermodynamics states dU = dQ - dW. The Second Law dictates that the total entropy of an isolated system never decreases. The maximum theoretical efficiency of a heat engine is the Carnot efficiency eta = 1 - (T_cold / T_hot)."
        }
    ],
    "AI401": [
        {
            "title": "AI401 Module 3: Backpropagation & Optimization Algorithms",
            "page": "Deep Learning Book (Goodfellow) Ch. 6, pp. 195-215",
            "keywords": ["backpropagation", "gradient descent", "loss function", "adam", "learning rate", "activation", "relu"],
            "content": "Backpropagation computes the gradient of the loss function with respect to each weight using the multivariate chain rule. Adaptive optimization algorithms like Adam compute individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients."
        },
        {
            "title": "AI401 Module 7: Attention Mechanisms & Transformer Architecture",
            "page": "Attention Is All You Need Paper & Notes",
            "keywords": ["transformer", "attention", "self-attention", "query", "key", "value", "rag", "embedding", "llm"],
            "content": "Scaled Dot-Product Attention is computed as Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V. Multi-Head Attention allows the model to jointly attend to information from different representation subspaces at different positions."
        }
    ]
}

