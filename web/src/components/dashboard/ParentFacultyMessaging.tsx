import React, { useState } from 'react';
import { Send } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface MessageItem {
  id: string;
  sender: string;
  recipient: string;
  text: string;
  time: string;
  isParent: boolean;
}

export const ParentFacultyMessaging: React.FC = () => {
  const { showToast } = useToast();
  const [selectedFaculty, setSelectedFaculty] = useState('Dr. Sarah Jenkins');
  const [inputText, setInputText] = useState('');

  const [messages, setMessages] = useState<MessageItem[]>([
    {
      id: 'M-1',
      sender: 'Dr. Sarah Jenkins',
      recipient: 'Mr. Ramesh Kumar',
      text: 'Good afternoon Mr. Kumar. Rahul scored 88% in his Database Systems test. His attendance is 86%.',
      time: 'Sept 08, 02:15 PM',
      isParent: false,
    },
    {
      id: 'M-2',
      sender: 'Mr. Ramesh Kumar',
      recipient: 'Dr. Sarah Jenkins',
      text: 'Thank you Dr. Jenkins. We are guiding him to prepare for the upcoming mid-term exam as well.',
      time: 'Sept 08, 04:30 PM',
      isParent: true,
    },
  ]);

  const handleSendMessage = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim()) return;

    const newMsg: MessageItem = {
      id: `M-${messages.length + 1}`,
      sender: 'Mr. Ramesh Kumar',
      recipient: selectedFaculty,
      text: inputText,
      time: 'Just now',
      isParent: true,
    };

    setMessages([...messages, newMsg]);
    setInputText('');
    showToast(`Message sent to ${selectedFaculty}`, 'success');
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Faculty Direct Communication Channel
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Direct messaging with Rahul's class instructors & Head of Department
          </p>
        </div>

        <select
          value={selectedFaculty}
          onChange={(e) => setSelectedFaculty(e.target.value)}
          style={{
            backgroundColor: 'rgba(15, 23, 42, 0.8)',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            borderRadius: '8px',
            color: '#f8fafc',
            padding: '4px 10px',
            fontSize: '0.78rem',
            outline: 'none',
            cursor: 'pointer',
          }}
        >
          <option value="Dr. Sarah Jenkins">Dr. Sarah Jenkins (Class Mentor)</option>
          <option value="Prof. Alan Turing">Prof. Alan Turing (OS Instructor)</option>
          <option value="Dr. Robert Rao">Dr. Robert Rao (HOD Computer Science)</option>
        </select>
      </div>

      {/* Message Chat Log */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '10px',
          maxHeight: '260px',
          overflowY: 'auto',
          marginBottom: '1rem',
          paddingRight: '4px',
        }}
      >
        {messages.map((m) => (
          <div
            key={m.id}
            style={{
              alignSelf: m.isParent ? 'flex-end' : 'flex-start',
              maxWidth: '80%',
              backgroundColor: m.isParent ? 'rgba(37, 99, 235, 0.25)' : 'rgba(15, 23, 42, 0.6)',
              border: m.isParent ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '12px',
              padding: '10px 12px',
            }}
          >
            <div style={{ fontSize: '0.72rem', color: m.isParent ? '#38bdf8' : '#a855f7', fontWeight: 700, marginBottom: '2px' }}>
              {m.sender}
            </div>
            <div style={{ fontSize: '0.8rem', color: '#f1f5f9' }}>{m.text}</div>
            <div style={{ fontSize: '0.68rem', color: '#64748b', textAlign: 'right', marginTop: '4px' }}>{m.time}</div>
          </div>
        ))}
      </div>

      {/* Send Message Input */}
      <form onSubmit={handleSendMessage} style={{ display: 'flex', gap: '8px' }}>
        <input
          type="text"
          placeholder={`Message ${selectedFaculty}...`}
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          style={{
            flex: 1,
            backgroundColor: 'rgba(15, 23, 42, 0.8)',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            borderRadius: '8px',
            color: '#f8fafc',
            padding: '8px 12px',
            fontSize: '0.8rem',
            outline: 'none',
          }}
        />
        <button
          type="submit"
          style={{
            backgroundColor: '#2563eb',
            border: 'none',
            color: '#ffffff',
            borderRadius: '8px',
            padding: '8px 14px',
            fontSize: '0.8rem',
            fontWeight: 700,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Send size={14} /> Send
        </button>
      </form>
    </div>
  );
};
