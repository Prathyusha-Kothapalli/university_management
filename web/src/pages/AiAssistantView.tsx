import React, { useState } from 'react';

interface ChatMessage {
  id: string;
  sender: 'ai' | 'user';
  text: string;
  time: string;
}

export const AiAssistantView: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'm1',
      sender: 'ai',
      text: 'Hello Alex! I am your UniSphere AI Academic Assistant. How can I help you navigate your courses, attendance, timetable, or exams today?',
      time: '09:40 AM',
    },
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  const quickPrompts = [
    'Where is my next class?',
    'Summarize my attendance status',
    'Upcoming deadlines this week',
    'Explain Transformer Attention',
  ];

  const handleSend = (textToSend?: string) => {
    const text = textToSend || input;
    if (!text.trim()) return;

    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      sender: 'user',
      text,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!textToSend) setInput('');
    setIsTyping(true);

    setTimeout(() => {
      let reply = "I've checked the university knowledge graph for that inquiry.";
      const lower = text.toLowerCase();

      if (lower.includes('class') || lower.includes('where') || lower.includes('next')) {
        reply = "Your next class is **Deep Learning & Neural Architectures (CS-401)** at **10:00 AM** in **Turing Hall B-204** with Prof. Arthur Vance.";
      } else if (lower.includes('attendance')) {
        reply = "Your overall attendance is **89.0%** (143/160 hours attended). All enrolled courses are comfortably above the 75% university eligibility threshold!";
      } else if (lower.includes('deadline') || lower.includes('assignment')) {
        reply = "You have **2 pending assignments**: \n1. Transformer Architecture Implementation (CS-401) due Sep 18.\n2. MapReduce Distributed Log Analyzer (DS-310) due Sep 22.";
      } else if (lower.includes('transformer') || lower.includes('attention')) {
        reply = "Scaled Dot-Product Attention calculates Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V. This allows the model to dynamically weight representations across arbitrary token distances.";
      } else {
        reply = `I have received your query: "${text}". Campus databases confirm your records are up to date. Feel free to ask about exams, placements, or room allocations!`;
      }

      const aiMsg: ChatMessage = {
        id: `a-${Date.now()}`,
        sender: 'ai',
        text: reply,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => [...prev, aiMsg]);
      setIsTyping(false);
    }, 600);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', minHeight: '520px' }}>
      {/* Bot Header Card */}
      <div style={{
        padding: '0.85rem 1.25rem',
        background: 'rgba(30, 41, 59, 0.7)',
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
      }}>
        <div style={{
          width: '36px',
          height: '36px',
          borderRadius: '50%',
          background: 'linear-gradient(135deg, #0ea5e9, #6366f1)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '1.2rem',
        }}>
          ✨
        </div>
        <div>
          <div style={{ fontSize: '0.9rem', fontWeight: 700, color: '#f8fafc' }}>
            UniSphere AI Copilot
          </div>
          <div style={{ fontSize: '0.72rem', color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px' }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#10b981' }} />
            Connected to Campus Brain
          </div>
        </div>
      </div>

      {/* Messages Scroll Area */}
      <div style={{ flex: 1, padding: '1rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {messages.map((m) => (
          <div
            key={m.id}
            style={{
              alignSelf: m.sender === 'user' ? 'flex-end' : 'flex-start',
              maxWidth: '85%',
              display: 'flex',
              flexDirection: 'column',
              alignItems: m.sender === 'user' ? 'flex-end' : 'flex-start',
            }}
          >
            <div style={{
              padding: '10px 14px',
              borderRadius: m.sender === 'user' ? '16px 16px 4px 16px' : '16px 16px 16px 4px',
              background: m.sender === 'user'
                ? 'linear-gradient(135deg, #2563eb, #3b82f6)'
                : 'rgba(30, 41, 59, 0.85)',
              border: m.sender === 'user' ? 'none' : '1px solid rgba(255, 255, 255, 0.08)',
              color: '#f8fafc',
              fontSize: '0.85rem',
              lineHeight: '1.4',
              whiteSpace: 'pre-line',
            }}>
              {m.text}
            </div>
            <span style={{ fontSize: '0.68rem', color: '#64748b', marginTop: '3px', padding: '0 4px' }}>
              {m.time}
            </span>
          </div>
        ))}

        {isTyping && (
          <div style={{
            alignSelf: 'flex-start',
            background: 'rgba(30, 41, 59, 0.85)',
            padding: '8px 14px',
            borderRadius: '16px 16px 16px 4px',
            fontSize: '0.78rem',
            color: '#94a3b8',
            fontStyle: 'italic',
          }}>
            AI is thinking...
          </div>
        )}
      </div>

      {/* Prompt Chips */}
      <div style={{
        padding: '0 1rem',
        display: 'flex',
        gap: '6px',
        overflowX: 'auto',
        whiteSpace: 'nowrap',
        paddingBottom: '8px',
      }}>
        {quickPrompts.map((q, i) => (
          <button
            key={i}
            onClick={() => handleSend(q)}
            style={{
              background: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(56, 189, 248, 0.3)',
              color: '#38bdf8',
              fontSize: '0.7rem',
              padding: '4px 10px',
              borderRadius: '12px',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            {q}
          </button>
        ))}
      </div>

      {/* Input Form */}
      <div style={{
        padding: '0.75rem 1rem',
        background: 'rgba(15, 23, 42, 0.85)',
        borderTop: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        gap: '8px',
      }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask AI anything about campus..."
          style={{
            flex: 1,
            background: 'rgba(30, 41, 59, 0.9)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            borderRadius: '12px',
            padding: '8px 12px',
            color: '#f8fafc',
            fontSize: '0.85rem',
            outline: 'none',
          }}
        />
        <button
          onClick={() => handleSend()}
          className="btn btn-primary"
          style={{ padding: '8px 14px', borderRadius: '12px', fontSize: '0.85rem' }}
        >
          Send
        </button>
      </div>
    </div>
  );
};
