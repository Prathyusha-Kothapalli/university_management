import React, { useState, useEffect, useRef } from 'react';
import {
  Course,
  ExplanationMode,
  ChatMessage
} from '../types/ai';
import { aiApi } from '../services/aiApi';

const EXPLANATION_MODES: Array<{ id: ExplanationMode; label: string; icon: string; desc: string }> = [
  { id: 'detailed', label: 'Academic', icon: '🎯', desc: 'Mathematical & algorithmic proofs' },
  { id: 'beginner', label: 'ELIF5', icon: '💡', desc: 'Intuitive analogies' },
  { id: 'code', label: 'Code', icon: '💻', desc: 'Syntax & data structures' },
  { id: 'exam_summary', label: 'Exam Prep', icon: '⚡', desc: 'High-yield points & traps' }
];

const CURATED_PROMPTS = [
  { text: 'Explain AVL Tree balance factors & rotations', course: 'CS101' },
  { text: 'What are the 4 Coffman conditions for deadlocks?', course: 'CS202' },
  { text: 'Explain eigenvalues & SVD matrix decomposition', course: 'MATH301' },
  { text: 'How does self-attention work in Transformers?', course: 'AI401' }
];

interface AIBotWidgetProps {
  isOpen: boolean;
  onToggle: () => void;
}

export const AIBotWidget: React.FC<AIBotWidgetProps> = ({ isOpen, onToggle }) => {
  const [isExpanded, setIsExpanded] = useState<boolean>(false);
  const [courses, setCourses] = useState<Course[]>([]);
  const [selectedCourseId, setSelectedCourseId] = useState<string>('CS101');
  const [selectedMode, setSelectedMode] = useState<ExplanationMode>('detailed');

  // Chat State
  const [messages, setMessages] = useState<ChatMessage[]>(() => {
    const saved = localStorage.getItem('unisphere_bot_messages');
    if (saved) {
      try { return JSON.parse(saved); } catch { /* fallback */ }
    }
    return [
      {
        id: 'bot_init',
        role: 'assistant',
        content: "Hi! 👋 I am your **UniSphere AI Academic Bot**.\n\nAsk me anything about your enrolled subjects, lecture slides, formulas, or code implementations.",
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        follow_up_questions: [
          'Explain AVL Tree balance factors & rotations',
          'What are the 4 Coffman deadlock conditions?',
          'How does Transformer self-attention work?'
        ]
      }
    ];
  });

  const [inputQuery, setInputQuery] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [loadingStep, setLoadingStep] = useState<string>('');
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [expandedSources, setExpandedSources] = useState<Record<string, boolean>>({});
  const [activeTab, setActiveTab] = useState<'chat' | 'bookmarks'>('chat');

  const chatEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Persistence
  useEffect(() => {
    localStorage.setItem('unisphere_bot_messages', JSON.stringify(messages));
  }, [messages]);

  // Load courses
  useEffect(() => {
    const fetchCourses = async () => {
      const data = await aiApi.getCourses();
      setCourses(data);
    };
    fetchCourses();
  }, []);

  // Auto-scroll
  useEffect(() => {
    if (isOpen) {
      chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, isOpen, isLoading]);

  // Focus input when opened
  useEffect(() => {
    if (isOpen && activeTab === 'chat') {
      setTimeout(() => inputRef.current?.focus(), 150);
    }
  }, [isOpen, activeTab]);

  const activeCourse = courses.find(c => c.id === selectedCourseId) || courses[0];

  const handleSendMessage = async (text: string, courseIdOverride?: string) => {
    const trimmed = text.trim();
    if (!trimmed || isLoading) return;

    const courseToUse = courseIdOverride || selectedCourseId;
    if (courseIdOverride) {
      setSelectedCourseId(courseIdOverride);
    }

    setInputQuery('');

    const userMessage: ChatMessage = {
      id: `user_${Date.now()}`,
      role: 'user',
      content: trimmed,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      course_id: courseToUse,
      mode: selectedMode
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setLoadingStep(`Searching ${courseToUse} syllabus notes...`);

    try {
      setTimeout(() => {
        setLoadingStep('Synthesizing academic answer & citations...');
      }, 300);

      const historyPayload = messages.slice(-4).map(m => ({
        role: m.role,
        content: m.content
      }));

      const res = await aiApi.askStudyAssistant({
        question: trimmed,
        course_id: courseToUse,
        mode: selectedMode,
        conversation_id: `bot_conv_${courseToUse}`,
        history: historyPayload
      });

      const botMessage: ChatMessage = {
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

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      const errMessage: ChatMessage = {
        id: `err_${Date.now()}`,
        role: 'assistant',
        content: '⚠️ **Bot Connection Notice**: Syllabus service is temporarily unreachable. Please retry.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isError: true
      };
      setMessages(prev => [...prev, errMessage]);
    } finally {
      setIsLoading(false);
      setLoadingStep('');
    }
  };

  const handleCopy = (content: string, id: string) => {
    navigator.clipboard.writeText(content);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleBookmark = (id: string) => {
    setMessages(prev =>
      prev.map(m => (m.id === id ? { ...m, isBookmarked: !m.isBookmarked } : m))
    );
  };

  const handleFeedback = (id: string, rating: 'helpful' | 'not_helpful') => {
    setMessages(prev =>
      prev.map(m => {
        if (m.id === id) {
          const next = m.helpfulRating === rating ? null : rating;
          if (next && m.conversation_id) {
            aiApi.sendFeedback(m.conversation_id, next === 'helpful');
          }
          return { ...m, helpfulRating: next };
        }
        return m;
      })
    );
  };

  const handleClearChat = () => {
    if (confirm('Clear chat conversation?')) {
      setMessages([
        {
          id: `bot_${Date.now()}`,
          role: 'assistant',
          content: "Chat cleared. What course or concept would you like to explore?",
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          follow_up_questions: [
            'Explain AVL Tree balance factors & rotations',
            'What are the 4 Coffman deadlock conditions?',
            'How does Transformer self-attention work?'
          ]
        }
      ]);
    }
  };

  const bookmarkedMessages = messages.filter(m => m.isBookmarked);

  return (
    <>
      {/* Floating Action Button (Always Visible at Bottom Right) */}
      <div style={{
        position: 'fixed',
        bottom: '24px',
        right: '24px',
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        gap: '0.65rem'
      }}>
        {!isOpen && (
          <div style={{
            backgroundColor: 'rgba(15, 23, 42, 0.92)',
            backdropFilter: 'blur(10px)',
            color: '#e2e8f0',
            padding: '0.45rem 0.85rem',
            borderRadius: '9999px',
            border: '1px solid rgba(56, 189, 248, 0.35)',
            boxShadow: '0 4px 16px rgba(0, 0, 0, 0.35)',
            fontSize: '0.78rem',
            fontWeight: 600,
            pointerEvents: 'none',
            display: 'flex',
            alignItems: 'center',
            gap: '0.4rem'
          }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#10b981' }} />
            <span>AI Study Copilot</span>
          </div>
        )}

        <button
          onClick={onToggle}
          title={isOpen ? 'Close AI Bot' : 'Open AI Study Assistant Bot'}
          style={{
            width: '56px',
            height: '56px',
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
            color: '#ffffff',
            border: '2px solid rgba(255, 255, 255, 0.25)',
            cursor: 'pointer',
            boxShadow: '0 8px 24px rgba(2, 132, 199, 0.45), 0 0 15px rgba(99, 102, 241, 0.35)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '1.4rem',
            transition: 'transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s',
            position: 'relative'
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.transform = 'scale(1.08)';
            e.currentTarget.style.boxShadow = '0 10px 28px rgba(2, 132, 199, 0.6), 0 0 20px rgba(99, 102, 241, 0.5)';
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.transform = 'scale(1)';
            e.currentTarget.style.boxShadow = '0 8px 24px rgba(2, 132, 199, 0.45), 0 0 15px rgba(99, 102, 241, 0.35)';
          }}
        >
          {isOpen ? '✕' : '✨'}
        </button>
      </div>

      {/* Floating Chatbot Widget Panel */}
      {isOpen && (
        <div style={{
          position: 'fixed',
          bottom: isExpanded ? '20px' : '90px',
          right: isExpanded ? '20px' : '24px',
          width: isExpanded ? 'calc(100vw - 40px)' : '420px',
          height: isExpanded ? 'calc(100vh - 40px)' : '620px',
          maxWidth: isExpanded ? '1100px' : 'calc(100vw - 36px)',
          maxHeight: isExpanded ? '92vh' : 'calc(100vh - 120px)',
          backgroundColor: '#0f172a',
          borderRadius: '16px',
          border: '1px solid rgba(56, 189, 248, 0.35)',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(2, 132, 199, 0.2)',
          display: 'flex',
          flexDirection: 'column',
          zIndex: 9998,
          overflow: 'hidden'
        }}>
          {/* Header */}
          <div style={{
            padding: '0.85rem 1rem',
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            background: 'linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(15, 23, 42, 0.95) 100%)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
              <div style={{
                width: '32px',
                height: '32px',
                borderRadius: '8px',
                background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1rem',
                color: '#fff',
                boxShadow: '0 0 10px rgba(2, 132, 199, 0.4)'
              }}>
                ✨
              </div>
              <div>
                <div style={{ fontSize: '0.9rem', fontWeight: 800, color: '#f8fafc', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                  <span>UniSphere AI Bot</span>
                  <span style={{
                    backgroundColor: 'rgba(16, 185, 129, 0.2)',
                    color: '#34d399',
                    fontSize: '0.62rem',
                    padding: '0.05rem 0.4rem',
                    borderRadius: '9999px',
                    fontWeight: 700
                  }}>
                    RAG 2.0
                  </span>
                </div>
                <div style={{ fontSize: '0.68rem', color: '#94a3b8', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                  <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#10b981' }} />
                  <span>Syllabus Indexed • Ready</span>
                </div>
              </div>
            </div>

            {/* Widget Controls */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
              <button
                onClick={() => setActiveTab(activeTab === 'chat' ? 'bookmarks' : 'chat')}
                title={activeTab === 'chat' ? 'View Saved Notes' : 'Back to Chat'}
                style={{
                  background: activeTab === 'bookmarks' ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255, 255, 255, 0.06)',
                  border: `1px solid ${activeTab === 'bookmarks' ? '#f59e0b' : 'rgba(255, 255, 255, 0.1)'}`,
                  color: activeTab === 'bookmarks' ? '#fcd34d' : '#cbd5e1',
                  padding: '0.3rem 0.55rem',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '0.74rem',
                  fontWeight: 600
                }}
              >
                {activeTab === 'chat' ? `🔖 (${bookmarkedMessages.length})` : '💬 Chat'}
              </button>

              <button
                onClick={handleClearChat}
                title="Clear conversation"
                style={{
                  background: 'rgba(255, 255, 255, 0.06)',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  color: '#94a3b8',
                  padding: '0.3rem 0.5rem',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '0.74rem'
                }}
              >
                🗑️
              </button>

              <button
                onClick={() => setIsExpanded(!isExpanded)}
                title={isExpanded ? 'Dock Window' : 'Expand Fullscreen'}
                style={{
                  background: 'rgba(255, 255, 255, 0.06)',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  color: '#cbd5e1',
                  padding: '0.3rem 0.5rem',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '0.74rem'
                }}
              >
                {isExpanded ? '⤢' : '⤡'}
              </button>

              <button
                onClick={onToggle}
                title="Minimize Bot"
                style={{
                  background: 'rgba(239, 68, 68, 0.1)',
                  border: '1px solid rgba(239, 68, 68, 0.25)',
                  color: '#fca5a5',
                  padding: '0.3rem 0.55rem',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '0.74rem',
                  fontWeight: 700
                }}
              >
                ✕
              </button>
            </div>
          </div>

          {/* Subject & Mode Selection Toolbar */}
          <div style={{
            padding: '0.55rem 0.85rem',
            backgroundColor: '#090d16',
            borderBottom: '1px solid rgba(255, 255, 255, 0.06)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '0.5rem',
            flexWrap: 'wrap'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', flex: 1, minWidth: '160px' }}>
              <span style={{ fontSize: '0.72rem', color: '#94a3b8', fontWeight: 600 }}>Subject:</span>
              <select
                value={selectedCourseId}
                onChange={(e) => setSelectedCourseId(e.target.value)}
                style={{
                  flex: 1,
                  backgroundColor: '#0f172a',
                  color: '#38bdf8',
                  border: '1px solid rgba(56, 189, 248, 0.3)',
                  padding: '0.3rem 0.5rem',
                  borderRadius: '6px',
                  fontWeight: 700,
                  fontSize: '0.76rem',
                  outline: 'none',
                  cursor: 'pointer'
                }}
              >
                {courses.map(c => (
                  <option key={c.id} value={c.id}>
                    {c.code}: {c.name}
                  </option>
                ))}
              </select>
            </div>

            <div style={{ display: 'flex', gap: '0.25rem' }}>
              {EXPLANATION_MODES.map(mode => (
                <button
                  key={mode.id}
                  onClick={() => setSelectedMode(mode.id)}
                  title={mode.desc}
                  style={{
                    backgroundColor: selectedMode === mode.id ? 'rgba(2, 132, 199, 0.25)' : 'rgba(255, 255, 255, 0.04)',
                    color: selectedMode === mode.id ? '#38bdf8' : '#94a3b8',
                    border: selectedMode === mode.id ? '1px solid #38bdf8' : '1px solid rgba(255, 255, 255, 0.08)',
                    padding: '0.25rem 0.5rem',
                    borderRadius: '6px',
                    fontSize: '0.7rem',
                    fontWeight: 600,
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.25rem'
                  }}
                >
                  <span>{mode.icon}</span>
                  <span>{mode.label}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Body: Chat Stream or Bookmarks */}
          {activeTab === 'chat' ? (
            <div style={{
              flex: 1,
              overflowY: 'auto',
              padding: '1rem',
              display: 'flex',
              flexDirection: 'column',
              gap: '1rem'
            }}>
              {/* Quick Prompts Carousel for New Chat */}
              {messages.length <= 1 && (
                <div style={{
                  backgroundColor: 'rgba(30, 41, 59, 0.4)',
                  border: '1px solid rgba(255, 255, 255, 0.06)',
                  borderRadius: '10px',
                  padding: '0.85rem'
                }}>
                  <div style={{ fontSize: '0.74rem', color: '#94a3b8', fontWeight: 600, marginBottom: '0.5rem' }}>
                    💡 Tap a prompt to start learning:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.35rem' }}>
                    {CURATED_PROMPTS.map((cp, idx) => (
                      <button
                        key={idx}
                        onClick={() => handleSendMessage(cp.text, cp.course)}
                        style={{
                          textAlign: 'left',
                          backgroundColor: '#0f172a',
                          border: '1px solid rgba(56, 189, 248, 0.2)',
                          color: '#e2e8f0',
                          padding: '0.45rem 0.75rem',
                          borderRadius: '6px',
                          fontSize: '0.76rem',
                          cursor: 'pointer',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          transition: 'all 0.15s ease'
                        }}
                        onMouseOver={(e) => {
                          e.currentTarget.style.borderColor = '#38bdf8';
                          e.currentTarget.style.color = '#38bdf8';
                        }}
                        onMouseOut={(e) => {
                          e.currentTarget.style.borderColor = 'rgba(56, 189, 248, 0.2)';
                          e.currentTarget.style.color = '#e2e8f0';
                        }}
                      >
                        <span>{cp.text}</span>
                        <span style={{ fontSize: '0.65rem', color: '#38bdf8', fontWeight: 700 }}>{cp.course} ➜</span>
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* Chat Message List */}
              {messages.map(msg => (
                <div
                  key={msg.id}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                    width: '100%'
                  }}
                >
                  <div style={{ fontSize: '0.68rem', color: '#64748b', marginBottom: '0.25rem' }}>
                    {msg.role === 'user' ? 'You' : 'AI Copilot'} • {msg.timestamp}
                  </div>

                  <div style={{
                    backgroundColor: msg.role === 'user' ? '#0284c7' : 'rgba(30, 41, 59, 0.8)',
                    color: '#f8fafc',
                    padding: '0.85rem 1rem',
                    borderRadius: msg.role === 'user' ? '12px 12px 2px 12px' : '12px 12px 12px 2px',
                    border: msg.role === 'user' ? '1px solid #0369a1' : '1px solid rgba(255, 255, 255, 0.08)',
                    maxWidth: '92%',
                    fontSize: '0.84rem',
                    lineHeight: 1.5,
                    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.2)'
                  }}>
                    {/* Confidence score & citations top tag */}
                    {msg.confidence !== undefined && (
                      <div style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        gap: '0.5rem',
                        marginBottom: '0.65rem',
                        paddingBottom: '0.45rem',
                        borderBottom: '1px solid rgba(255, 255, 255, 0.08)'
                      }}>
                        <span style={{
                          backgroundColor: 'rgba(16, 185, 129, 0.15)',
                          color: '#34d399',
                          border: '1px solid rgba(16, 185, 129, 0.3)',
                          padding: '0.1rem 0.45rem',
                          borderRadius: '4px',
                          fontSize: '0.68rem',
                          fontWeight: 700
                        }}>
                          ⭐ {Math.round(msg.confidence * 100)}% Match
                        </span>

                        {msg.sources && msg.sources.length > 0 && (
                          <button
                            onClick={() => setExpandedSources(p => ({ ...p, [msg.id]: !p[msg.id] }))}
                            style={{
                              background: 'none',
                              border: 'none',
                              color: '#38bdf8',
                              fontSize: '0.7rem',
                              fontWeight: 600,
                              cursor: 'pointer',
                              padding: 0
                            }}
                          >
                            📚 {msg.sources.length} Citations {expandedSources[msg.id] ? '▲' : '▼'}
                          </button>
                        )}
                      </div>
                    )}

                    {/* Content */}
                    <div style={{ whiteSpace: 'pre-wrap' }}>
                      {msg.content}
                    </div>

                    {/* Citations Accordion */}
                    {msg.sources && msg.sources.length > 0 && expandedSources[msg.id] && (
                      <div style={{
                        marginTop: '0.75rem',
                        paddingTop: '0.65rem',
                        borderTop: '1px solid rgba(255, 255, 255, 0.08)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '0.4rem'
                      }}>
                        {msg.sources.map((src, i) => (
                          <div key={i} style={{ backgroundColor: '#090d16', padding: '0.5rem', borderRadius: '6px', fontSize: '0.72rem' }}>
                            <div style={{ fontWeight: 700, color: '#38bdf8' }}>{src.title} ({src.page})</div>
                            <div style={{ color: '#94a3b8', fontStyle: 'italic', marginTop: '0.2rem' }}>"{src.snippet}"</div>
                          </div>
                        ))}
                      </div>
                    )}

                    {/* Toolbar buttons */}
                    {msg.role === 'assistant' && !msg.isError && (
                      <div style={{
                        marginTop: '0.75rem',
                        paddingTop: '0.5rem',
                        borderTop: '1px solid rgba(255, 255, 255, 0.08)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        gap: '0.5rem'
                      }}>
                        <div style={{ display: 'flex', gap: '0.35rem' }}>
                          <button
                            onClick={() => handleCopy(msg.content, msg.id)}
                            style={{
                              backgroundColor: 'rgba(255, 255, 255, 0.06)',
                              border: '1px solid rgba(255, 255, 255, 0.1)',
                              color: copiedId === msg.id ? '#34d399' : '#cbd5e1',
                              padding: '0.2rem 0.5rem',
                              borderRadius: '4px',
                              fontSize: '0.7rem',
                              cursor: 'pointer'
                            }}
                          >
                            {copiedId === msg.id ? '✓ Copied' : '📋 Copy'}
                          </button>

                          <button
                            onClick={() => handleBookmark(msg.id)}
                            style={{
                              backgroundColor: msg.isBookmarked ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255, 255, 255, 0.06)',
                              border: `1px solid ${msg.isBookmarked ? '#f59e0b' : 'rgba(255, 255, 255, 0.1)'}`,
                              color: msg.isBookmarked ? '#fcd34d' : '#cbd5e1',
                              padding: '0.2rem 0.5rem',
                              borderRadius: '4px',
                              fontSize: '0.7rem',
                              cursor: 'pointer'
                            }}
                          >
                            {msg.isBookmarked ? '🔖 Saved' : '🔖 Save'}
                          </button>
                        </div>

                        <div style={{ display: 'flex', gap: '0.25rem', alignItems: 'center' }}>
                          <button
                            onClick={() => handleFeedback(msg.id, 'helpful')}
                            style={{
                              backgroundColor: msg.helpfulRating === 'helpful' ? 'rgba(16, 185, 129, 0.25)' : 'transparent',
                              border: '1px solid rgba(255, 255, 255, 0.1)',
                              color: msg.helpfulRating === 'helpful' ? '#34d399' : '#94a3b8',
                              padding: '0.2rem 0.4rem',
                              borderRadius: '4px',
                              fontSize: '0.7rem',
                              cursor: 'pointer'
                            }}
                          >
                            👍
                          </button>
                          <button
                            onClick={() => handleFeedback(msg.id, 'not_helpful')}
                            style={{
                              backgroundColor: msg.helpfulRating === 'not_helpful' ? 'rgba(239, 68, 68, 0.25)' : 'transparent',
                              border: '1px solid rgba(255, 255, 255, 0.1)',
                              color: msg.helpfulRating === 'not_helpful' ? '#fca5a5' : '#94a3b8',
                              padding: '0.2rem 0.4rem',
                              borderRadius: '4px',
                              fontSize: '0.7rem',
                              cursor: 'pointer'
                            }}
                          >
                            👎
                          </button>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Follow-up Chips */}
                  {msg.follow_up_questions && msg.follow_up_questions.length > 0 && (
                    <div style={{ marginTop: '0.45rem', width: '100%', display: 'flex', flexDirection: 'column', gap: '0.3rem' }}>
                      {msg.follow_up_questions.map((fq, i) => (
                        <button
                          key={i}
                          onClick={() => handleSendMessage(fq)}
                          style={{
                            textAlign: 'left',
                            backgroundColor: 'rgba(15, 23, 42, 0.9)',
                            border: '1px solid rgba(56, 189, 248, 0.25)',
                            color: '#38bdf8',
                            padding: '0.35rem 0.65rem',
                            borderRadius: '6px',
                            fontSize: '0.74rem',
                            cursor: 'pointer'
                          }}
                          onMouseOver={(e) => (e.currentTarget.style.backgroundColor = 'rgba(56, 189, 248, 0.12)')}
                          onMouseOut={(e) => (e.currentTarget.style.backgroundColor = 'rgba(15, 23, 42, 0.9)')}
                        >
                          ➜ {fq}
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              ))}

              {/* Loading Indicator */}
              {isLoading && (
                <div style={{
                  backgroundColor: 'rgba(30, 41, 59, 0.5)',
                  border: '1px solid rgba(56, 189, 248, 0.3)',
                  borderRadius: '10px',
                  padding: '0.75rem',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem'
                }}>
                  <div style={{
                    width: '8px',
                    height: '8px',
                    borderRadius: '50%',
                    backgroundColor: '#38bdf8',
                    animation: 'pulse 1s infinite'
                  }} />
                  <span style={{ fontSize: '0.76rem', color: '#38bdf8', fontWeight: 600 }}>
                    {loadingStep || 'Querying syllabus...'}
                  </span>
                </div>
              )}

              <div ref={chatEndRef} />
            </div>
          ) : (
            <div style={{ flex: 1, overflowY: 'auto', padding: '1rem' }}>
              <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#fcd34d', marginBottom: '0.75rem' }}>
                🔖 Saved Revision Vault Notes ({bookmarkedMessages.length})
              </div>
              {bookmarkedMessages.length === 0 ? (
                <div style={{ color: '#64748b', fontSize: '0.78rem', textAlign: 'center', padding: '2rem 1rem' }}>
                  No saved notes yet. Tap "🔖 Save" on any AI response to pin it here.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
                  {bookmarkedMessages.map(bm => (
                    <div key={bm.id} style={{
                      backgroundColor: 'rgba(245, 158, 11, 0.08)',
                      border: '1px solid rgba(245, 158, 11, 0.25)',
                      padding: '0.75rem',
                      borderRadius: '8px'
                    }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.35rem' }}>
                        <span style={{ fontSize: '0.7rem', color: '#fcd34d', fontWeight: 700 }}>{bm.course_id || 'Course'} Note</span>
                        <span style={{ fontSize: '0.65rem', color: '#64748b' }}>{bm.timestamp}</span>
                      </div>
                      <div style={{ fontSize: '0.78rem', color: '#cbd5e1', whiteSpace: 'pre-wrap' }}>
                        {bm.content}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Input Bar */}
          {activeTab === 'chat' && (
            <div style={{
              padding: '0.75rem',
              backgroundColor: '#090d16',
              borderTop: '1px solid rgba(255, 255, 255, 0.08)'
            }}>
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSendMessage(inputQuery);
                }}
                style={{ display: 'flex', gap: '0.45rem' }}
              >
                <input
                  ref={inputRef}
                  type="text"
                  value={inputQuery}
                  onChange={(e) => setInputQuery(e.target.value)}
                  placeholder={`Ask ${activeCourse?.code || 'Course'} (${selectedMode})...`}
                  style={{
                    flex: 1,
                    padding: '0.6rem 0.85rem',
                    backgroundColor: '#0f172a',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '8px',
                    color: '#f8fafc',
                    fontSize: '0.82rem',
                    outline: 'none'
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
                    border: 'none',
                    padding: '0.6rem 0.95rem',
                    borderRadius: '8px',
                    fontWeight: 700,
                    fontSize: '0.82rem',
                    cursor: isLoading || !inputQuery.trim() ? 'not-allowed' : 'pointer',
                    opacity: isLoading || !inputQuery.trim() ? 0.5 : 1
                  }}
                >
                  Send
                </button>
              </form>
            </div>
          )}
        </div>
      )}
    </>
  );
};
