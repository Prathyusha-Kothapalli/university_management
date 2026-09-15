import React, { useState, useEffect, useRef } from 'react';
import {
  Course,
  ExplanationMode,
  ChatMessage,
  ConversationSession
} from '../types/ai';
import { aiApi } from '../services/aiApi';

const EXPLANATION_MODES: Array<{ id: ExplanationMode; label: string; icon: string; desc: string }> = [
  { id: 'detailed', label: 'Academic & Deep Dive', icon: '🎯', desc: 'Mathematical derivations, algorithmic proofs & asymptotic analysis' },
  { id: 'beginner', label: 'Conceptual (ELIF5)', icon: '💡', desc: 'Intuitive analogies & simplified plain English breakdown' },
  { id: 'code', label: 'Code & Implementation', icon: '💻', desc: 'Production-ready syntax, data structures & test walkthroughs' },
  { id: 'exam_summary', label: 'High-Yield Exam Prep', icon: '⚡', desc: 'Key bullet points, must-know formulas & common trap warnings' }
];

const CURATED_TOPICS: Array<{ title: string; prompt: string; courseId: string; tag: string }> = [
  {
    title: 'AVL Tree Balancing & Rotations',
    prompt: 'Explain AVL Tree balance factors and how single (LL/RR) and double (LR/RL) rotations maintain O(log N) heights.',
    courseId: 'CS101',
    tag: 'Trees & Complexity'
  },
  {
    title: 'Dijkstra vs Bellman-Ford Shortest Path',
    prompt: 'How does Dijkstra algorithm work with min-heaps, and why does it fail on negative edge weights compared to Bellman-Ford?',
    courseId: 'CS101',
    tag: 'Graph Algorithms'
  },
  {
    title: 'Operating System Deadlocks & Coffman Criteria',
    prompt: 'What are the 4 Coffman necessary conditions for deadlocks, and how does Dijkstra Banker Algorithm ensure safe state allocation?',
    courseId: 'CS202',
    tag: 'Concurrency & OS'
  },
  {
    title: 'Eigenvalues & Matrix Diagonalization',
    prompt: 'Explain eigenvalues, eigenvectors, characteristic polynomials, and the geometric intuition of Singular Value Decomposition (SVD).',
    courseId: 'MATH301',
    tag: 'Linear Algebra'
  },
  {
    title: 'Scaled Dot-Product Attention in Transformers',
    prompt: 'How does Scaled Dot-Product Attention work in Transformer architectures and why is the sqrt(d_k) scaling factor essential?',
    courseId: 'AI401',
    tag: 'Deep Learning'
  }
];

export const AIStudyAssistant: React.FC = () => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [selectedCourseId, setSelectedCourseId] = useState<string>('CS101');
  const [selectedMode, setSelectedMode] = useState<ExplanationMode>('detailed');

  // Sessions and History
  const [sessions, setSessions] = useState<ConversationSession[]>(() => {
    const saved = localStorage.getItem('unisphere_ai_sessions');
    if (saved) {
      try { return JSON.parse(saved); } catch { /* fallback */ }
    }
    return [
      {
        id: 'session_welcome',
        title: 'AVL Trees & Balancing Review',
        courseId: 'CS101',
        mode: 'detailed',
        lastUpdated: new Date().toISOString(),
        messages: [
          {
            id: 'msg_welcome',
            role: 'assistant',
            content: "Welcome to your **UniSphere AI Academic Study Copilot**.\n\nI am connected to your university's verified course materials and lecture notes. Select your subject above, choose an explanation mode, or pick one of the study topics below to get started.",
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            follow_up_questions: [
              'Explain AVL Tree balance factors and rotation cases',
              'How does Dijkstra algorithm find shortest paths with min-heaps?',
              'What are the 4 Coffman conditions for deadlocks in Operating Systems?'
            ]
          }
        ]
      }
    ];
  });

  const [activeSessionId, setActiveSessionId] = useState<string>('session_welcome');
  const [sidebarTab, setSidebarTab] = useState<'history' | 'bookmarks'>('history');
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(true);
  const [historySearch, setHistorySearch] = useState<string>('');

  // Input & state
  const [inputQuery, setInputQuery] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [loadingStep, setLoadingStep] = useState<string>('');
  const [errorState, setErrorState] = useState<string | null>(null);
  const [copiedMessageId, setCopiedMessageId] = useState<string | null>(null);
  const [expandedSources, setExpandedSources] = useState<Record<string, boolean>>({});

  const chatEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Save sessions to localStorage
  useEffect(() => {
    localStorage.setItem('unisphere_ai_sessions', JSON.stringify(sessions));
  }, [sessions]);

  // Load courses
  useEffect(() => {
    const fetchCourses = async () => {
      const data = await aiApi.getCourses();
      setCourses(data);
    };
    fetchCourses();
  }, []);

  // Auto scroll
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [sessions, activeSessionId, isLoading]);

  const activeSession = sessions.find(s => s.id === activeSessionId) || sessions[0];
  const activeCourse = courses.find(c => c.id === selectedCourseId) || courses[0];

  const handleCreateNewSession = () => {
    const newSession: ConversationSession = {
      id: `session_${Date.now()}`,
      title: `${selectedCourseId} Study Note`,
      courseId: selectedCourseId,
      mode: selectedMode,
      lastUpdated: new Date().toISOString(),
      messages: [
        {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: `New session started for **${activeCourse?.name || selectedCourseId}** (${selectedMode.replace('_', ' ').toUpperCase()} mode).\n\nAsk any concept question, homework problem, derivation, or code walkthrough.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          follow_up_questions: [
            `Summarize the key theorems & formulas in ${selectedCourseId}`,
            `What are the most common exam questions for ${selectedCourseId}?`,
            `Show a practical code implementation for ${selectedCourseId}`
          ]
        }
      ]
    };
    setSessions(prev => [newSession, ...prev]);
    setActiveSessionId(newSession.id);
  };

  const handleDeleteSession = (sessionId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (sessions.length <= 1) {
      handleCreateNewSession();
      return;
    }
    const filtered = sessions.filter(s => s.id !== sessionId);
    setSessions(filtered);
    if (activeSessionId === sessionId) {
      setActiveSessionId(filtered[0].id);
    }
  };

  const handleSendMessage = async (queryText: string) => {
    const trimmed = queryText.trim();
    if (!trimmed || isLoading) return;

    setErrorState(null);
    setInputQuery('');

    const userMessage: ChatMessage = {
      id: `user_${Date.now()}`,
      role: 'user',
      content: trimmed,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      course_id: selectedCourseId,
      mode: selectedMode
    };

    setSessions(prev =>
      prev.map(s => {
        if (s.id === activeSessionId) {
          const isFirstUserMsg = !s.messages.some(m => m.role === 'user');
          const title = isFirstUserMsg ? trimmed.slice(0, 36) + (trimmed.length > 36 ? '...' : '') : s.title;
          return {
            ...s,
            title,
            courseId: selectedCourseId,
            mode: selectedMode,
            lastUpdated: new Date().toISOString(),
            messages: [...s.messages, userMessage]
          };
        }
        return s;
      })
    );

    setIsLoading(true);
    setLoadingStep(`Querying ${selectedCourseId} curriculum notes & slides...`);

    try {
      setTimeout(() => {
        setLoadingStep('Synthesizing structured academic answer & citations...');
      }, 350);

      const historyPayload = activeSession.messages.slice(-4).map(m => ({
        role: m.role,
        content: m.content
      }));

      const res = await aiApi.askStudyAssistant({
        question: trimmed,
        course_id: selectedCourseId,
        mode: selectedMode,
        conversation_id: activeSessionId,
        history: historyPayload
      });

      const assistantMessage: ChatMessage = {
        id: `assistant_${Date.now()}`,
        role: 'assistant',
        content: res.answer,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        sources: res.sources,
        confidence: res.confidence,
        conversation_id: res.conversation_id,
        course_id: res.course_id,
        mode: res.mode,
        follow_up_questions: res.follow_up_questions,
        isBookmarked: false,
        helpfulRating: null
      };

      setSessions(prev =>
        prev.map(s => {
          if (s.id === activeSessionId) {
            return {
              ...s,
              lastUpdated: new Date().toISOString(),
              messages: [...s.messages, assistantMessage]
            };
          }
          return s;
        })
      );
    } catch (err: any) {
      setErrorState(err.message || 'Unable to connect to AI study pipeline.');
      const errorMessage: ChatMessage = {
        id: `err_${Date.now()}`,
        role: 'assistant',
        content: '⚠️ **System Notice**: We encountered a temporary issue querying the lecture database. Please retry your query below.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isError: true
      };
      setSessions(prev =>
        prev.map(s => (s.id === activeSessionId ? { ...s, messages: [...s.messages, errorMessage] } : s))
      );
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  const handleCopyText = (text: string, msgId: string) => {
    navigator.clipboard.writeText(text);
    setCopiedMessageId(msgId);
    setTimeout(() => setCopiedMessageId(null), 2000);
  };

  const handleToggleBookmark = (msgId: string) => {
    setSessions(prev =>
      prev.map(s => ({
        ...s,
        messages: s.messages.map(m => {
          if (m.id === msgId) {
            return { ...m, isBookmarked: !m.isBookmarked };
          }
          return m;
        })
      }))
    );
  };

  const handleFeedback = (msgId: string, rating: 'helpful' | 'not_helpful') => {
    setSessions(prev =>
      prev.map(s => ({
        ...s,
        messages: s.messages.map(m => {
          if (m.id === msgId) {
            const nextRating = m.helpfulRating === rating ? null : rating;
            if (nextRating && m.conversation_id) {
              aiApi.sendFeedback(m.conversation_id, nextRating === 'helpful');
            }
            return { ...m, helpfulRating: nextRating };
          }
          return m;
        })
      }))
    );
  };

  const toggleSourceAccordion = (msgId: string) => {
    setExpandedSources(prev => ({ ...prev, [msgId]: !prev[msgId] }));
  };

  const filteredSessions = sessions.filter(s =>
    s.title.toLowerCase().includes(historySearch.toLowerCase()) ||
    s.courseId.toLowerCase().includes(historySearch.toLowerCase())
  );

  const allBookmarkedMessages = sessions
    .flatMap(s => s.messages.filter(m => m.isBookmarked))
    .sort((a, b) => b.timestamp.localeCompare(a.timestamp));

  return (
    <div style={{
      display: 'flex',
      height: 'calc(100vh - 61px)',
      backgroundColor: '#090d16',
      color: '#f8fafc',
      overflow: 'hidden'
    }}>
      {/* Sidebar: Conversation Sessions & Saved Notes */}
      <aside style={{
        width: isSidebarOpen ? '300px' : '0px',
        backgroundColor: '#0f172a',
        borderRight: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        flexDirection: 'column',
        transition: 'width 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
        overflow: 'hidden',
        flexShrink: 0
      }}>
        {/* New Session Button */}
        <div style={{ padding: '1rem', borderBottom: '1px solid rgba(255, 255, 255, 0.06)' }}>
          <button
            onClick={handleCreateNewSession}
            style={{
              width: '100%',
              background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
              color: '#ffffff',
              border: '1px solid rgba(56, 189, 248, 0.3)',
              padding: '0.65rem 1rem',
              borderRadius: '10px',
              fontWeight: 700,
              fontSize: '0.84rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '0.5rem',
              boxShadow: '0 4px 12px rgba(2, 132, 199, 0.25)',
              transition: 'transform 0.15s, box-shadow 0.15s'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.transform = 'translateY(-1px)';
              e.currentTarget.style.boxShadow = '0 6px 16px rgba(2, 132, 199, 0.35)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.transform = 'none';
              e.currentTarget.style.boxShadow = '0 4px 12px rgba(2, 132, 199, 0.25)';
            }}
          >
            <span style={{ fontSize: '1rem' }}>+</span>
            <span>New Study Topic</span>
          </button>

          {/* Search bar */}
          <div style={{ marginTop: '0.75rem' }}>
            <input
              type="text"
              value={historySearch}
              onChange={(e) => setHistorySearch(e.target.value)}
              placeholder="Search previous notes..."
              style={{
                width: '100%',
                padding: '0.45rem 0.75rem',
                backgroundColor: 'rgba(2, 6, 23, 0.6)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
                borderRadius: '8px',
                color: '#f8fafc',
                fontSize: '0.78rem',
                outline: 'none'
              }}
            />
          </div>

          {/* Tab Filter */}
          <div style={{ display: 'flex', marginTop: '0.65rem', gap: '0.25rem', backgroundColor: '#020617', padding: '0.2rem', borderRadius: '8px' }}>
            <button
              onClick={() => setSidebarTab('history')}
              style={{
                flex: 1,
                padding: '0.35rem',
                backgroundColor: sidebarTab === 'history' ? 'rgba(56, 189, 248, 0.15)' : 'transparent',
                color: sidebarTab === 'history' ? '#38bdf8' : '#94a3b8',
                border: 'none',
                borderRadius: '6px',
                fontSize: '0.74rem',
                fontWeight: 600,
                cursor: 'pointer'
              }}
            >
              Recent ({sessions.length})
            </button>
            <button
              onClick={() => setSidebarTab('bookmarks')}
              style={{
                flex: 1,
                padding: '0.35rem',
                backgroundColor: sidebarTab === 'bookmarks' ? 'rgba(245, 158, 11, 0.15)' : 'transparent',
                color: sidebarTab === 'bookmarks' ? '#fcd34d' : '#94a3b8',
                border: 'none',
                borderRadius: '6px',
                fontSize: '0.74rem',
                fontWeight: 600,
                cursor: 'pointer'
              }}
            >
              🔖 Saved ({allBookmarkedMessages.length})
            </button>
          </div>
        </div>

        {/* Sidebar List */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '0.6rem' }}>
          {sidebarTab === 'history' ? (
            filteredSessions.map(s => (
              <div
                key={s.id}
                onClick={() => {
                  setActiveSessionId(s.id);
                  setSelectedCourseId(s.courseId);
                  setSelectedMode(s.mode);
                }}
                style={{
                  padding: '0.65rem 0.75rem',
                  backgroundColor: activeSessionId === s.id ? 'rgba(56, 189, 248, 0.08)' : 'transparent',
                  border: activeSessionId === s.id ? '1px solid rgba(56, 189, 248, 0.35)' : '1px solid transparent',
                  borderRadius: '8px',
                  marginBottom: '0.35rem',
                  cursor: 'pointer',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  transition: 'all 0.15s ease'
                }}
              >
                <div style={{ overflow: 'hidden', paddingRight: '0.5rem' }}>
                  <div style={{
                    fontSize: '0.82rem',
                    fontWeight: activeSessionId === s.id ? 700 : 500,
                    color: activeSessionId === s.id ? '#38bdf8' : '#e2e8f0',
                    whiteSpace: 'nowrap',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis'
                  }}>
                    {s.title}
                  </div>
                  <div style={{ display: 'flex', gap: '0.4rem', alignItems: 'center', marginTop: '0.2rem' }}>
                    <span style={{
                      fontSize: '0.65rem',
                      backgroundColor: 'rgba(255, 255, 255, 0.06)',
                      color: '#94a3b8',
                      padding: '0.05rem 0.35rem',
                      borderRadius: '4px',
                      fontWeight: 700
                    }}>
                      {s.courseId}
                    </span>
                    <span style={{ fontSize: '0.68rem', color: '#64748b' }}>
                      {s.messages.length} notes
                    </span>
                  </div>
                </div>

                <button
                  onClick={(e) => handleDeleteSession(s.id, e)}
                  title="Remove Session"
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#64748b',
                    cursor: 'pointer',
                    fontSize: '0.8rem',
                    padding: '0.2rem',
                    borderRadius: '4px'
                  }}
                  onMouseOver={(e) => (e.currentTarget.style.color = '#ef4444')}
                  onMouseOut={(e) => (e.currentTarget.style.color = '#64748b')}
                >
                  ✕
                </button>
              </div>
            ))
          ) : (
            <div>
              {allBookmarkedMessages.length === 0 ? (
                <div style={{ padding: '2rem 1rem', textAlign: 'center', color: '#64748b', fontSize: '0.78rem' }}>
                  No saved answers yet. Click 🔖 on any answer to save it to your revision vault.
                </div>
              ) : (
                allBookmarkedMessages.map(m => (
                  <div
                    key={m.id}
                    style={{
                      padding: '0.75rem',
                      backgroundColor: 'rgba(245, 158, 11, 0.06)',
                      border: '1px solid rgba(245, 158, 11, 0.25)',
                      borderRadius: '8px',
                      marginBottom: '0.5rem'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.3rem' }}>
                      <span style={{ fontSize: '0.7rem', color: '#fcd34d', fontWeight: 700 }}>Saved Note</span>
                      <span style={{ fontSize: '0.65rem', color: '#64748b' }}>{m.timestamp}</span>
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#cbd5e1', maxHeight: '75px', overflow: 'hidden', textOverflow: 'ellipsis', lineHeight: 1.4 }}>
                      {m.content.slice(0, 130)}...
                    </div>
                  </div>
                ))
              )}
            </div>
          )}
        </div>
      </aside>

      {/* Main Workspace Area */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
        {/* Subject & Style Config Ribbon */}
        <div style={{
          padding: '0.75rem 1.75rem',
          backgroundColor: '#0f172a',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '1rem'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <button
              onClick={() => setIsSidebarOpen(!isSidebarOpen)}
              style={{
                backgroundColor: 'rgba(255, 255, 255, 0.06)',
                border: '1px solid rgba(255, 255, 255, 0.1)',
                color: '#cbd5e1',
                padding: '0.45rem 0.65rem',
                borderRadius: '8px',
                cursor: 'pointer',
                fontSize: '0.8rem',
                fontWeight: 600
              }}
              title={isSidebarOpen ? 'Hide Sidebar' : 'Show Sidebar'}
            >
              {isSidebarOpen ? '◀ Notes' : '▶ Notes'}
            </button>

            {/* Course Selector */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Active Subject:</span>
              <select
                value={selectedCourseId}
                onChange={(e) => setSelectedCourseId(e.target.value)}
                style={{
                  backgroundColor: '#020617',
                  color: '#38bdf8',
                  border: '1px solid rgba(56, 189, 248, 0.4)',
                  padding: '0.45rem 0.85rem',
                  borderRadius: '8px',
                  fontWeight: 700,
                  fontSize: '0.84rem',
                  outline: 'none',
                  cursor: 'pointer',
                  boxShadow: '0 0 10px rgba(56, 189, 248, 0.1)'
                }}
              >
                {courses.map(c => (
                  <option key={c.id} value={c.id}>
                    {c.code}: {c.name}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Explanation Modes */}
          <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
            {EXPLANATION_MODES.map(mode => (
              <button
                key={mode.id}
                onClick={() => setSelectedMode(mode.id)}
                title={mode.desc}
                style={{
                  backgroundColor: selectedMode === mode.id ? 'rgba(2, 132, 199, 0.25)' : 'rgba(255, 255, 255, 0.04)',
                  color: selectedMode === mode.id ? '#38bdf8' : '#94a3b8',
                  border: selectedMode === mode.id ? '1px solid #38bdf8' : '1px solid rgba(255, 255, 255, 0.08)',
                  padding: '0.4rem 0.8rem',
                  borderRadius: '8px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.35rem',
                  boxShadow: selectedMode === mode.id ? '0 0 12px rgba(56, 189, 248, 0.2)' : 'none',
                  transition: 'all 0.15s ease'
                }}
              >
                <span>{mode.icon}</span>
                <span>{mode.label}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Message Stream */}
        <div style={{
          flex: 1,
          overflowY: 'auto',
          padding: '1.75rem',
          display: 'flex',
          flexDirection: 'column',
          gap: '1.5rem',
          maxWidth: '1050px',
          width: '100%',
          margin: '0 auto'
        }}>
          {/* Quick Curated Topics for Fresh Session */}
          {activeSession.messages.length <= 1 && (
            <div style={{
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '14px',
              padding: '1.5rem',
              backdropFilter: 'blur(8px)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.4rem' }}>
                <span style={{ fontSize: '1.1rem' }}>💡</span>
                <h3 style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
                  High-Yield Academic Prompts & Lecture Topics
                </h3>
              </div>
              <p style={{ color: '#94a3b8', fontSize: '0.82rem', margin: '0 0 1rem 0' }}>
                Select a curriculum topic to trigger an in-depth analytical breakdown grounded in syllabus materials:
              </p>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '0.65rem' }}>
                {CURATED_TOPICS.map((topic, i) => (
                  <div
                    key={i}
                    onClick={() => {
                      setSelectedCourseId(topic.courseId);
                      handleSendMessage(topic.prompt);
                    }}
                    style={{
                      backgroundColor: '#0f172a',
                      border: '1px solid rgba(255, 255, 255, 0.08)',
                      padding: '0.85rem 1rem',
                      borderRadius: '10px',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between'
                    }}
                    onMouseOver={(e) => {
                      e.currentTarget.style.borderColor = '#38bdf8';
                      e.currentTarget.style.transform = 'translateY(-2px)';
                      e.currentTarget.style.boxShadow = '0 6px 16px rgba(0, 0, 0, 0.3)';
                    }}
                    onMouseOut={(e) => {
                      e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                      e.currentTarget.style.transform = 'none';
                      e.currentTarget.style.boxShadow = 'none';
                    }}
                  >
                    <div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.35rem' }}>
                        <span style={{
                          fontSize: '0.68rem',
                          fontWeight: 800,
                          color: '#38bdf8',
                          backgroundColor: 'rgba(56, 189, 248, 0.1)',
                          padding: '0.1rem 0.45rem',
                          borderRadius: '4px'
                        }}>
                          {topic.courseId}
                        </span>
                        <span style={{ fontSize: '0.7rem', color: '#64748b' }}>{topic.tag}</span>
                      </div>
                      <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f8fafc', lineHeight: 1.3 }}>
                        {topic.title}
                      </div>
                    </div>
                    <div style={{ fontSize: '0.72rem', color: '#94a3b8', marginTop: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <span>Launch Analysis</span>
                      <span>➜</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Messages */}
          {activeSession.messages.map((msg) => (
            <div
              key={msg.id}
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                width: '100%'
              }}
            >
              {/* Message Header */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.4rem', fontSize: '0.76rem' }}>
                <span style={{ fontWeight: 700, color: msg.role === 'user' ? '#38bdf8' : '#10b981' }}>
                  {msg.role === 'user' ? '🧑‍🎓 You (Student)' : '✨ UniSphere Academic Copilot'}
                </span>
                {msg.mode && (
                  <span style={{
                    backgroundColor: 'rgba(255, 255, 255, 0.06)',
                    color: '#94a3b8',
                    padding: '0.05rem 0.45rem',
                    borderRadius: '4px',
                    fontSize: '0.68rem',
                    fontWeight: 600
                  }}>
                    {msg.mode.replace('_', ' ').toUpperCase()}
                  </span>
                )}
                <span style={{ color: '#475569' }}>•</span>
                <span style={{ color: '#64748b' }}>{msg.timestamp}</span>
              </div>

              {/* Message Box */}
              <div style={{
                backgroundColor: msg.role === 'user' ? '#0369a1' : 'rgba(30, 41, 59, 0.7)',
                backdropFilter: 'blur(8px)',
                color: '#f8fafc',
                padding: '1.35rem 1.5rem',
                borderRadius: msg.role === 'user' ? '14px 14px 2px 14px' : '14px 14px 14px 2px',
                border: msg.role === 'user' ? '1px solid #0284c7' : '1px solid rgba(255, 255, 255, 0.08)',
                maxWidth: msg.role === 'user' ? '80%' : '100%',
                width: msg.role === 'user' ? 'auto' : '100%',
                boxShadow: '0 4px 20px -5px rgba(0, 0, 0, 0.35)',
                lineHeight: 1.6
              }}>
                {/* Confidence & Sources Top Bar for AI Messages */}
                {msg.confidence !== undefined && (
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    marginBottom: '1rem',
                    paddingBottom: '0.65rem',
                    borderBottom: '1px solid rgba(255, 255, 255, 0.08)'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <span style={{
                        backgroundColor: 'rgba(16, 185, 129, 0.15)',
                        color: '#34d399',
                        border: '1px solid rgba(16, 185, 129, 0.35)',
                        padding: '0.2rem 0.6rem',
                        borderRadius: '6px',
                        fontSize: '0.74rem',
                        fontWeight: 700,
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.35rem'
                      }}>
                        <span>⭐</span>
                        <span>{Math.round(msg.confidence * 100)}% Syllabus Match</span>
                      </span>
                    </div>

                    {msg.sources && msg.sources.length > 0 && (
                      <button
                        onClick={() => toggleSourceAccordion(msg.id)}
                        style={{
                          backgroundColor: 'rgba(56, 189, 248, 0.08)',
                          color: '#38bdf8',
                          border: '1px solid rgba(56, 189, 248, 0.25)',
                          padding: '0.25rem 0.65rem',
                          borderRadius: '6px',
                          fontSize: '0.74rem',
                          fontWeight: 600,
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.35rem'
                        }}
                      >
                        <span>📚</span>
                        <span>{msg.sources.length} Academic Citations {expandedSources[msg.id] ? '▲' : '▼'}</span>
                      </button>
                    )}
                  </div>
                )}

                {/* Message Body Content */}
                <div style={{ fontSize: '0.93rem', whiteSpace: 'pre-wrap' }}>
                  {msg.content}
                </div>

                {/* Collapsible Verified Citations Accordion */}
                {msg.sources && msg.sources.length > 0 && expandedSources[msg.id] && (
                  <div style={{
                    marginTop: '1.25rem',
                    paddingTop: '1rem',
                    borderTop: '1px solid rgba(255, 255, 255, 0.08)'
                  }}>
                    <div style={{ fontSize: '0.76rem', fontWeight: 700, color: '#38bdf8', marginBottom: '0.65rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                      Verified University Course References & Slide Citations:
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                      {msg.sources.map((src, idx) => (
                        <div
                          key={idx}
                          style={{
                            backgroundColor: '#090d16',
                            border: '1px solid rgba(255, 255, 255, 0.08)',
                            borderRadius: '8px',
                            padding: '0.85rem'
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.3rem' }}>
                            <span style={{ fontWeight: 700, fontSize: '0.82rem', color: '#f8fafc' }}>
                              {src.title}
                            </span>
                            <span style={{
                              color: '#38bdf8',
                              fontSize: '0.72rem',
                              fontWeight: 700,
                              backgroundColor: 'rgba(56, 189, 248, 0.1)',
                              padding: '0.1rem 0.45rem',
                              borderRadius: '4px'
                            }}>
                              {src.page}
                            </span>
                          </div>
                          <p style={{ margin: 0, fontSize: '0.78rem', color: '#94a3b8', fontStyle: 'italic', lineHeight: 1.4 }}>
                            "{src.snippet}"
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Actions Toolbar */}
                {msg.role === 'assistant' && !msg.isError && (
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    marginTop: '1.25rem',
                    paddingTop: '0.85rem',
                    borderTop: '1px solid rgba(255, 255, 255, 0.08)',
                    flexWrap: 'wrap',
                    gap: '0.5rem'
                  }}>
                    <div style={{ display: 'flex', gap: '0.45rem' }}>
                      {/* Copy */}
                      <button
                        onClick={() => handleCopyText(msg.content, msg.id)}
                        style={{
                          backgroundColor: 'rgba(255, 255, 255, 0.06)',
                          border: '1px solid rgba(255, 255, 255, 0.1)',
                          color: copiedMessageId === msg.id ? '#34d399' : '#cbd5e1',
                          padding: '0.35rem 0.75rem',
                          borderRadius: '6px',
                          fontSize: '0.76rem',
                          cursor: 'pointer',
                          fontWeight: 600,
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.35rem'
                        }}
                      >
                        {copiedMessageId === msg.id ? '✓ Copied to Clipboard' : '📋 Copy Notes'}
                      </button>

                      {/* Bookmark */}
                      <button
                        onClick={() => handleToggleBookmark(msg.id)}
                        style={{
                          backgroundColor: msg.isBookmarked ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255, 255, 255, 0.06)',
                          border: `1px solid ${msg.isBookmarked ? '#f59e0b' : 'rgba(255, 255, 255, 0.1)'}`,
                          color: msg.isBookmarked ? '#fcd34d' : '#cbd5e1',
                          padding: '0.35rem 0.75rem',
                          borderRadius: '6px',
                          fontSize: '0.76rem',
                          cursor: 'pointer',
                          fontWeight: 600,
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.35rem'
                        }}
                      >
                        {msg.isBookmarked ? '🔖 Saved in Vault' : '🔖 Save Note'}
                      </button>
                    </div>

                    {/* Feedback */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                      <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Helpful?</span>
                      <button
                        onClick={() => handleFeedback(msg.id, 'helpful')}
                        style={{
                          backgroundColor: msg.helpfulRating === 'helpful' ? 'rgba(16, 185, 129, 0.25)' : 'rgba(255, 255, 255, 0.06)',
                          border: `1px solid ${msg.helpfulRating === 'helpful' ? '#10b981' : 'rgba(255, 255, 255, 0.1)'}`,
                          color: msg.helpfulRating === 'helpful' ? '#34d399' : '#94a3b8',
                          padding: '0.3rem 0.6rem',
                          borderRadius: '6px',
                          fontSize: '0.76rem',
                          cursor: 'pointer',
                          fontWeight: 600
                        }}
                      >
                        👍 Yes
                      </button>
                      <button
                        onClick={() => handleFeedback(msg.id, 'not_helpful')}
                        style={{
                          backgroundColor: msg.helpfulRating === 'not_helpful' ? 'rgba(239, 68, 68, 0.25)' : 'rgba(255, 255, 255, 0.06)',
                          border: `1px solid ${msg.helpfulRating === 'not_helpful' ? '#ef4444' : 'rgba(255, 255, 255, 0.1)'}`,
                          color: msg.helpfulRating === 'not_helpful' ? '#fca5a5' : '#94a3b8',
                          padding: '0.3rem 0.6rem',
                          borderRadius: '6px',
                          fontSize: '0.76rem',
                          cursor: 'pointer',
                          fontWeight: 600
                        }}
                      >
                        👎 No
                      </button>
                    </div>
                  </div>
                )}
              </div>

              {/* Follow-up Question Chips */}
              {msg.follow_up_questions && msg.follow_up_questions.length > 0 && (
                <div style={{ marginTop: '0.65rem', width: '100%' }}>
                  <div style={{ fontSize: '0.74rem', color: '#94a3b8', marginBottom: '0.4rem', fontWeight: 600 }}>
                    💡 Suggested Next Questions:
                  </div>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.45rem' }}>
                    {msg.follow_up_questions.map((fq, idx) => (
                      <button
                        key={idx}
                        onClick={() => handleSendMessage(fq)}
                        style={{
                          backgroundColor: 'rgba(15, 23, 42, 0.8)',
                          border: '1px solid rgba(56, 189, 248, 0.3)',
                          color: '#38bdf8',
                          padding: '0.4rem 0.85rem',
                          borderRadius: '8px',
                          fontSize: '0.78rem',
                          fontWeight: 500,
                          cursor: 'pointer',
                          textAlign: 'left',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.4rem',
                          transition: 'all 0.15s ease'
                        }}
                        onMouseOver={(e) => {
                          e.currentTarget.style.backgroundColor = 'rgba(56, 189, 248, 0.15)';
                          e.currentTarget.style.borderColor = '#38bdf8';
                        }}
                        onMouseOut={(e) => {
                          e.currentTarget.style.backgroundColor = 'rgba(15, 23, 42, 0.8)';
                          e.currentTarget.style.borderColor = 'rgba(56, 189, 248, 0.3)';
                        }}
                      >
                        <span>➜</span>
                        <span>{fq}</span>
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}

          {/* Loading Skeleton Indicator */}
          {isLoading && (
            <div style={{
              backgroundColor: 'rgba(30, 41, 59, 0.6)',
              border: '1px solid rgba(56, 189, 248, 0.4)',
              borderRadius: '14px',
              padding: '1.5rem',
              maxWidth: '650px',
              display: 'flex',
              flexDirection: 'column',
              gap: '0.85rem',
              backdropFilter: 'blur(8px)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
                <div style={{
                  width: '12px',
                  height: '12px',
                  borderRadius: '50%',
                  backgroundColor: '#38bdf8',
                  boxShadow: '0 0 12px #38bdf8',
                  animation: 'pulse 1.2s infinite'
                }} />
                <span style={{ fontSize: '0.86rem', color: '#38bdf8', fontWeight: 600 }}>
                  {loadingStep || 'Querying academic syllabus documents...'}
                </span>
              </div>
              <div style={{ height: '10px', backgroundColor: 'rgba(255, 255, 255, 0.08)', borderRadius: '4px', width: '92%' }} />
              <div style={{ height: '10px', backgroundColor: 'rgba(255, 255, 255, 0.08)', borderRadius: '4px', width: '78%' }} />
            </div>
          )}

          {/* Error Alert Box */}
          {errorState && (
            <div style={{
              backgroundColor: 'rgba(239, 68, 68, 0.12)',
              border: '1px solid rgba(239, 68, 68, 0.35)',
              color: '#fca5a5',
              padding: '1.25rem',
              borderRadius: '12px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              gap: '1rem'
            }}>
              <div>
                <div style={{ fontWeight: 700, fontSize: '0.88rem' }}>Query Processing Issue</div>
                <div style={{ fontSize: '0.8rem', color: '#cbd5e1', marginTop: '0.2rem' }}>{errorState}</div>
              </div>
              <button
                onClick={() => handleSendMessage(inputQuery || 'Explain core concepts')}
                style={{
                  backgroundColor: '#ef4444',
                  color: '#fff',
                  border: 'none',
                  padding: '0.45rem 0.95rem',
                  borderRadius: '6px',
                  fontSize: '0.78rem',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              >
                Retry
              </button>
            </div>
          )}

          <div ref={chatEndRef} />
        </div>

        {/* Input Bar */}
        <div style={{
          padding: '1rem 1.75rem',
          backgroundColor: '#0f172a',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)'
        }}>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSendMessage(inputQuery);
            }}
            style={{
              display: 'flex',
              gap: '0.75rem',
              alignItems: 'center',
              maxWidth: '1050px',
              margin: '0 auto'
            }}
          >
            <input
              ref={inputRef}
              type="text"
              value={inputQuery}
              onChange={(e) => setInputQuery(e.target.value)}
              placeholder={`Ask a question in ${activeCourse?.code || 'Course'} (${selectedMode.replace('_', ' ')})...`}
              style={{
                flex: 1,
                padding: '0.85rem 1.25rem',
                backgroundColor: 'rgba(2, 6, 23, 0.7)',
                border: '1px solid rgba(255, 255, 255, 0.12)',
                borderRadius: '12px',
                color: '#f8fafc',
                fontSize: '0.92rem',
                outline: 'none',
                boxShadow: 'inset 0 2px 4px rgba(0, 0, 0, 0.3)',
                transition: 'border-color 0.2s'
              }}
              onFocus={(e) => (e.target.style.borderColor = '#38bdf8')}
              onBlur={(e) => (e.target.style.borderColor = 'rgba(255, 255, 255, 0.12)')}
            />

            <button
              type="submit"
              disabled={isLoading || !inputQuery.trim()}
              style={{
                background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
                color: '#ffffff',
                border: '1px solid rgba(56, 189, 248, 0.3)',
                padding: '0.85rem 1.6rem',
                borderRadius: '12px',
                fontWeight: 700,
                fontSize: '0.9rem',
                cursor: isLoading || !inputQuery.trim() ? 'not-allowed' : 'pointer',
                opacity: isLoading || !inputQuery.trim() ? 0.5 : 1,
                boxShadow: '0 4px 12px rgba(2, 132, 199, 0.3)',
                transition: 'all 0.15s ease',
                display: 'flex',
                alignItems: 'center',
                gap: '0.4rem'
              }}
            >
              <span>Ask Copilot</span>
              <span>➜</span>
            </button>
          </form>
        </div>
      </main>
    </div>
  );
};
