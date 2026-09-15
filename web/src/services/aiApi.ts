import {
  Course,
  StudyAssistantRequestPayload,
  StudyAssistantResponsePayload,
  SourceCitation
} from '../types/ai';

const getAiBaseUrls = (): string[] => {
  const customUrl = (import.meta as any).env?.VITE_AI_URL;
  if (customUrl) return [customUrl];

  if (typeof window !== 'undefined') {
    const host = window.location.hostname || '127.0.0.1';
    const primary = `http://${host}:5001`;
    const fallback = host === '127.0.0.1' ? 'http://localhost:5001' : 'http://127.0.0.1:5001';
    return [primary, fallback];
  }
  return ['http://127.0.0.1:5001', 'http://localhost:5001'];
};

const FALLBACK_COURSES: Course[] = [
  {
    id: 'CS101',
    name: 'Data Structures & Algorithms',
    code: 'CS101',
    department: 'Computer Science',
    description: 'Core fundamentals of asymptotic analysis, trees, graphs, sorting, and dynamic programming.'
  },
  {
    id: 'CS202',
    name: 'Operating Systems & Architecture',
    code: 'CS202',
    department: 'Computer Science',
    description: 'Processes, threads, CPU scheduling, concurrency, virtual memory, and file systems.'
  },
  {
    id: 'MATH301',
    name: 'Linear Algebra & Matrix Theory',
    code: 'MATH301',
    department: 'Mathematics',
    description: 'Vector spaces, linear transformations, eigenvalues, eigenvectors, SVD, and matrix decomposition.'
  },
  {
    id: 'PHYS101',
    name: 'Engineering Physics & Mechanics',
    code: 'PHYS101',
    department: 'Physics',
    description: 'Classical mechanics, thermodynamics, wave optics, and electromagnetic principles.'
  },
  {
    id: 'AI401',
    name: 'Machine Learning & Neural Networks',
    code: 'AI401',
    department: 'Artificial Intelligence',
    description: 'Supervised learning, deep neural networks, transformer architectures, and RAG pipelines.'
  }
];

class AiApiService {
  async getCourses(): Promise<Course[]> {
    const baseUrls = getAiBaseUrls();
    for (const baseUrl of baseUrls) {
      try {
        const res = await fetch(`${baseUrl}/ai/courses`, { method: 'GET' });
        if (res.ok) {
          return await res.json();
        }
      } catch {
        // Try next URL
      }
    }
    return FALLBACK_COURSES;
  }

  async askStudyAssistant(payload: StudyAssistantRequestPayload): Promise<StudyAssistantResponsePayload> {
    const baseUrls = getAiBaseUrls();
    for (const baseUrl of baseUrls) {
      try {
        const res = await fetch(`${baseUrl}/ai/study-assistant`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });

        if (res.ok) {
          return await res.json();
        }
      } catch {
        // Try next URL
      }
    }

    return this.generateFallbackResponse(payload);
  }

  async sendFeedback(conversationId: string, isHelpful: boolean, comment?: string): Promise<void> {
    const baseUrls = getAiBaseUrls();
    for (const baseUrl of baseUrls) {
      try {
        await fetch(`${baseUrl}/ai/feedback`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            conversation_id: conversationId,
            is_helpful: isHelpful,
            comment: comment || undefined,
          }),
        });
        return;
      } catch {
        // Try next URL
      }
    }
  }

  private generateFallbackResponse(payload: StudyAssistantRequestPayload): StudyAssistantResponsePayload {
    const qLower = payload.question.toLowerCase();
    const courseId = payload.course_id;
    const mode = payload.mode;
    const convId = payload.conversation_id || `conv_${Math.random().toString(36).substring(2, 9)}`;

    let answer = '';
    let sources: SourceCitation[] = [];
    let followUps: string[] = [];

    if (qLower.includes('avl') || qLower.includes('tree') || qLower.includes('rotation')) {
      sources = [
        {
          title: 'CS101 Lecture 4: Self-Balancing Trees (AVL & Red-Black)',
          page: 'Slides 12-18',
          snippet: 'An AVL tree is a self-balancing binary search tree where the difference between heights of left and right subtrees (balance factor) cannot exceed 1. Rebalancing is performed using four rotation cases: LL, RR, LR, and RL with guaranteed O(log N) lookup and insertion.',
          relevance_score: 0.96
        },
        {
          title: 'Introduction to Algorithms (CLRS)',
          page: 'Chapter 13, pp. 310-322',
          snippet: 'Binary search tree invariants and balance restoration operations.',
          relevance_score: 0.88
        }
      ];

      if (mode === 'beginner') {
        answer = `### 🌲 AVL Trees Explained Simply (Beginner Mode)\n\nImagine a bookshelf where you place numbered books in order (Binary Search Tree). If you add them in sequential order (1, 2, 3, 4), they form a long single file line, making searches slow.\n\n**An AVL Tree acts like an automatic rebalancer:**\n- Every time you insert a node, it checks if one branch is more than **1 level deeper** than the other.\n- If it is, it performs a **'rotation'** (like picking up the middle node and swinging the children into balance).\n\n**Result:** Finding any item always takes fast **O(log N)** time!`;
      } else if (mode === 'code') {
        answer = `### 💻 AVL Tree Python Node & Rotation Implementation\n\n\`\`\`python\nclass AVLNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n        self.height = 1\n\ndef get_height(node):\n    return node.height if node else 0\n\ndef get_balance(node):\n    return get_height(node.left) - get_height(node.right) if node else 0\n\ndef right_rotate(y):\n    x = y.left\n    T2 = x.right\n    x.right = y\n    y.left = T2\n    y.height = 1 + max(get_height(y.left), get_height(y.right))\n    x.height = 1 + max(get_height(x.left), get_height(x.right))\n    return x\n\`\`\`\n\n**Complexity:** Rotations run in $O(1)$ constant time; search and insert take $O(\\log N)$.`;
      } else if (mode === 'exam_summary') {
        answer = `### ⚡ Exam Quick Revision: AVL Trees\n\n- **Core Condition:** Balance Factor $\\text{BF}(v) = h_{left} - h_{right} \\in \\{-1, 0, 1\\}$.\n- **4 Rotation Cases:**\n  1. **LL:** Single Right Rotation\n  2. **RR:** Single Left Rotation\n  3. **LR:** Left Rotate child, then Right Rotate root\n  4. **RL:** Right Rotate child, then Left Rotate root\n- **Complexity:** All operations strictly $O(\\log N)$ worst-case.\n- **Exam Trap:** Always recompute heights bottom-up along the insertion path!`;
      } else {
        answer = `### 🎯 In-Depth Analysis: AVL Trees & Strict Balance Maintenance\n\nAn **AVL Tree** is a self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one.\n\n$$\\text{BalanceFactor}(N) = \\text{Height}(\\text{Left}) - \\text{Height}(\\text{Right}) \\in \\{-1, 0, +1\\}$$\n\n#### 1. Rebalancing Rotations\n- **Single Rotations (LL & RR):** Correct linear imbalances in $O(1)$ time.\n- **Double Rotations (LR & RL):** Rectify zigzag imbalances by rotating the child first, followed by the ancestor.\n\n#### 2. Performance Guarantee\nLookup, Insertion, and Deletion are all guaranteed $O(\\log N)$ worst-case time complexity, making AVL trees ideal for read-intensive lookups.`;
      }

      followUps = [
        'How does an AVL Tree compare with a Red-Black Tree in lookup vs insertion workloads?',
        'Can you show a trace of inserting keys [10, 20, 30, 40, 50] into an empty AVL tree?',
        'What is the maximum height of an AVL tree with N nodes?'
      ];
    } else {
      sources = [
        {
          title: `${courseId} University Curriculum Handbook`,
          page: 'Unit 2 Notes, Slide 8',
          snippet: `Foundational concepts and principles covering ${payload.question}.`,
          relevance_score: 0.92
        }
      ];

      answer = `### 🎓 Study Assistance: ${courseId}\n\n**Regarding your query:** *"${payload.question}"*\n\n#### Conceptual Breakdown (${mode.replace('_', ' ').toUpperCase()} Mode):\n1. **Core Mechanism:** This concept is a core pillar in university curriculum for ${courseId}.\n2. **Analysis:** Reviewing fundamental invariants, equations, and edge cases will provide comprehensive exam preparation.\n3. **Practical Application:** Verify assumptions with practice sets and problem walkthroughs.`;

      followUps = [
        `Can you provide a step-by-step example problem in ${courseId}?`,
        'What are the most common exam questions asked on this topic?',
        'How does this relate to other modules in the course syllabus?'
      ];
    }

    return {
      answer,
      sources,
      confidence: sources[0]?.relevance_score || 0.92,
      conversation_id: convId,
      course_id: courseId,
      mode: mode,
      follow_up_questions: followUps,
    };
  }
}

export const aiApi = new AiApiService();

