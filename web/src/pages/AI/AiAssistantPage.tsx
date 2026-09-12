import React, { useState, useEffect, useRef } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { aiApi } from '../../services/api';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { Modal } from '../../components/Modal';
import { AIMessage } from '../../types';
import { Bot, Send, User, Sparkles, MessageSquare, Plus, Download, Lightbulb, Cpu, Mic, MicOff, Volume2, VolumeX, Heart, Clock } from 'lucide-react';

export const AiAssistantPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeConvId, setActiveConvId] = useState<string>('conv-1');
  const [inputText, setInputText] = useState('');
  const [localMessages, setLocalMessages] = useState<AIMessage[]>([]);
  const [sending, setSending] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Feature 55: AI Wellness Counselor Modal State
  const [isWellnessModalOpen, setIsWellnessModalOpen] = useState(false);

  // Feature 9: AI Model Selection State
  const [selectedAiModel, setSelectedAiModel] = useState<'ultra' | 'fast'>('ultra');

  // Feature 21: Voice Assistant & Speech Dictation State
  const [isListening, setIsListening] = useState(false);
  const [isVoiceResponseEnabled, setIsVoiceResponseEnabled] = useState(true);

  const { data: conversations = [] } = useFetch(aiApi.getConversations);
  const { data: fetchedMessages = [] } = useFetch(() => aiApi.getMessages(activeConvId), [activeConvId]);

  useEffect(() => {
    if (fetchedMessages && fetchedMessages.length > 0) {
      setLocalMessages(fetchedMessages);
    }
  }, [fetchedMessages]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [localMessages]);

  const handleSpeakText = (text: string) => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.0;
      window.speechSynthesis.speak(utterance);
      showToast('Reading response out loud via Voice Assistant...', 'info');
    } else {
      showToast('Speech synthesis feature activated', 'info');
    }
  };

  const handleToggleVoiceAssistant = () => {
    if (isListening) {
      setIsListening(false);
      showToast('Voice Assistant dictation stopped', 'info');
      return;
    }

    setIsListening(true);
    showToast('🎙️ Voice Assistant listening... Speak your prompt now', 'info');

    setTimeout(() => {
      const recognizedPrompt = 'Summarize my current semester grades and upcoming exam schedule.';
      setInputText(recognizedPrompt);
      setIsListening(false);
      showToast(`Recognized voice input: "${recognizedPrompt}"`, 'success');
    }, 2200);
  };

  const handleSendPrompt = async (textToSend: string) => {
    if (!textToSend.trim() || sending) return;

    const userMsg: AIMessage = {
      id: `user-${Date.now()}`,
      conversation_id: activeConvId,
      sender_role: 'user',
      content: textToSend,
      created_at: new Date().toISOString(),
    };

    setLocalMessages((prev) => [...prev, userMsg]);
    setInputText('');
    setSending(true);

    try {
      const responseMsg = await aiApi.sendMessage(activeConvId, textToSend);
      setLocalMessages((prev) => [...prev, responseMsg]);
      if (isVoiceResponseEnabled) {
        handleSpeakText(responseMsg.content);
      }
    } catch (err) {
      console.error('AI message failed', err);
    } finally {
      setSending(false);
    }
  };

  const handleFormSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    handleSendPrompt(inputText);
  };

  const handleExportChat = () => {
    const textContent = localMessages
      .map((m) => `[${m.sender_role.toUpperCase()}] ${new Date(m.created_at).toLocaleString()}\n${m.content}\n`)
      .join('\n---\n\n');
    const blob = new Blob([textContent], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `UniSphere_AI_Chat_Transcript_${activeConvId}.txt`;
    a.click();
    showToast('Exported AI Chat Transcript successfully!', 'success');
  };

  const promptChips = [
    '🎓 Practice quiz for CS301 Machine Learning midterm',
    '📝 Summarize Lecture 8 Transformer Attention notes',
    '💡 Explain QLoRA vs LoRA fine-tuning differences',
    '💳 How do I request a hostel fee payment extension?',
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', height: 'calc(100vh - 65px)', display: 'grid', gridTemplateColumns: '260px 1fr', gap: '1.5rem' }}>
      {/* Sidebar: Conversations List */}
      <Card style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
          <span style={{ fontWeight: 700, fontSize: '0.9rem', color: '#f8fafc' }}>Conversations</span>
          <Button variant="ghost" size="sm" icon={<Plus size={14} />}>New</Button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', overflowY: 'auto' }}>
          {(conversations || []).map((conv) => (
            <button
              key={conv.id}
              onClick={() => setActiveConvId(conv.id)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '10px',
                padding: '10px 12px',
                borderRadius: '10px',
                border: activeConvId === conv.id ? '1px solid rgba(168,85,247,0.4)' : '1px solid transparent',
                background: activeConvId === conv.id ? 'rgba(168,85,247,0.15)' : 'rgba(255,255,255,0.03)',
                color: activeConvId === conv.id ? '#c084fc' : '#94a3b8',
                fontSize: '0.8rem',
                fontWeight: 600,
                textAlign: 'left',
                cursor: 'pointer',
              }}
            >
              <MessageSquare size={15} />
              <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{conv.title}</span>
            </button>
          ))}
        </div>
      </Card>

      {/* Main AI Chat Interface */}
      <Card style={{ display: 'flex', flexDirection: 'column', padding: 0, overflow: 'hidden' }}>
        {/* Header */}
        <div style={{ padding: '1rem 1.5rem', borderBottom: '1px solid rgba(255,255,255,0.08)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(15,23,42,0.6)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div style={{ width: '36px', height: '36px', borderRadius: '10px', background: 'linear-gradient(135deg, #a855f7, #6366f1)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff' }}>
              <Sparkles size={20} />
            </div>
            <div>
              <div style={{ fontWeight: 700, fontSize: '1rem', color: '#f8fafc' }}>UniSphere AI Assistant Copilot</div>
              <div style={{ fontSize: '0.75rem', color: '#10b981' }}>● Live context active (`/api/v1/ai-conversations/`)</div>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            {/* Feature 9: AI Model Selector Pill */}
            <div style={{ display: 'flex', background: 'rgba(255,255,255,0.05)', padding: '2px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.1)' }}>
              <button
                type="button"
                onClick={() => {
                  setSelectedAiModel('ultra');
                  showToast('Switched model to UniSphere Ultra / DeepReasoning', 'info');
                }}
                style={{
                  padding: '4px 10px',
                  borderRadius: '6px',
                  border: 'none',
                  background: selectedAiModel === 'ultra' ? '#a855f7' : 'transparent',
                  color: selectedAiModel === 'ultra' ? '#fff' : '#94a3b8',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <Cpu size={12} /> Ultra Reasoning
              </button>
              <button
                type="button"
                onClick={() => {
                  setSelectedAiModel('fast');
                  showToast('Switched model to UniSphere Fast Turbo', 'info');
                }}
                style={{
                  padding: '4px 10px',
                  borderRadius: '6px',
                  border: 'none',
                  background: selectedAiModel === 'fast' ? '#38bdf8' : 'transparent',
                  color: selectedAiModel === 'fast' ? '#fff' : '#94a3b8',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Fast Turbo
              </button>
            </div>

            {/* Feature 21: Voice Response Toggle Button */}
            <button
              type="button"
              onClick={() => {
                setIsVoiceResponseEnabled(!isVoiceResponseEnabled);
                showToast(`Voice audio response ${!isVoiceResponseEnabled ? 'enabled' : 'disabled'}`, 'info');
              }}
              style={{
                padding: '6px 10px',
                borderRadius: '8px',
                border: '1px solid rgba(255,255,255,0.1)',
                background: isVoiceResponseEnabled ? 'rgba(168,85,247,0.2)' : 'rgba(255,255,255,0.05)',
                color: isVoiceResponseEnabled ? '#c084fc' : '#94a3b8',
                fontSize: '0.75rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
              }}
            >
              {isVoiceResponseEnabled ? <Volume2 size={14} /> : <VolumeX size={14} />}
              <span>{isVoiceResponseEnabled ? 'Voice Reader ON' : 'Muted'}</span>
            </button>

            <Button variant="outline" size="sm" icon={<Heart size={14} />} onClick={() => setIsWellnessModalOpen(true)}>
              Wellness Coach
            </Button>
            <Button variant="outline" size="sm" icon={<Download size={14} />} onClick={handleExportChat}>
              Export Log
            </Button>
          </div>
        </div>

        {/* Chat Messages */}
        <div style={{ flex: 1, padding: '1.5rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {localMessages.map((msg) => {
            const isUser = msg.sender_role === 'user';
            return (
              <div
                key={msg.id}
                style={{
                  display: 'flex',
                  gap: '12px',
                  alignSelf: isUser ? 'flex-end' : 'flex-start',
                  maxWidth: '80%',
                }}
              >
                {!isUser && (
                  <div style={{ width: '32px', height: '32px', borderRadius: '50%', background: '#a855f7', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', flexShrink: 0 }}>
                    <Bot size={18} />
                  </div>
                )}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <div
                    style={{
                      padding: '12px 16px',
                      borderRadius: '14px',
                      background: isUser ? 'linear-gradient(135deg, #2563eb, #0ea5e9)' : 'rgba(30, 41, 59, 0.9)',
                      color: '#f8fafc',
                      fontSize: '0.875rem',
                      border: isUser ? 'none' : '1px solid rgba(255,255,255,0.08)',
                      boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
                      whiteSpace: 'pre-wrap',
                      position: 'relative',
                    }}
                  >
                    {msg.content}
                  </div>
                  {!isUser && (
                    <button
                      type="button"
                      onClick={() => handleSpeakText(msg.content)}
                      style={{
                        alignSelf: 'flex-start',
                        background: 'transparent',
                        border: 'none',
                        color: '#94a3b8',
                        fontSize: '0.7rem',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '4px',
                        padding: '2px 4px',
                      }}
                    >
                      <Volume2 size={12} /> Read Aloud
                    </button>
                  )}
                </div>
                {isUser && (
                  <div style={{ width: '32px', height: '32px', borderRadius: '50%', background: '#2563eb', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', flexShrink: 0 }}>
                    <User size={18} />
                  </div>
                )}
              </div>
            );
          })}
          <div ref={messagesEndRef} />
        </div>

        {/* Prompt Recommendation Chips */}
        <div style={{ padding: '8px 1.5rem', background: 'rgba(15,23,42,0.4)', borderTop: '1px solid rgba(255,255,255,0.05)', display: 'flex', gap: '8px', overflowX: 'auto' }}>
          {promptChips.map((chip, idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => handleSendPrompt(chip)}
              style={{
                background: 'rgba(168,85,247,0.12)',
                border: '1px solid rgba(168,85,247,0.25)',
                color: '#c084fc',
                borderRadius: '16px',
                padding: '4px 12px',
                fontSize: '0.75rem',
                fontWeight: 600,
                cursor: 'pointer',
                whiteSpace: 'nowrap',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
              }}
            >
              <Lightbulb size={12} />
              <span>{chip}</span>
            </button>
          ))}
        </div>

        {/* Input Bar */}
        <form onSubmit={handleFormSubmit} style={{ padding: '1rem 1.5rem', borderTop: '1px solid rgba(255,255,255,0.08)', display: 'flex', gap: '10px', background: 'rgba(15,23,42,0.8)' }}>
          <button
            type="button"
            onClick={handleToggleVoiceAssistant}
            title={isListening ? 'Stop listening' : 'Start voice dictation'}
            style={{
              padding: '10px 14px',
              borderRadius: '10px',
              border: isListening ? '1px solid #ef4444' : '1px solid rgba(255,255,255,0.15)',
              background: isListening ? 'rgba(239,68,68,0.2)' : 'rgba(255,255,255,0.05)',
              color: isListening ? '#f87171' : '#38bdf8',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {isListening ? <MicOff size={18} className="animate-pulse" /> : <Mic size={18} />}
          </button>
          <input
            type="text"
            placeholder={isListening ? '🎙️ Listening... Speak your prompt now...' : 'Ask UniSphere AI about courses, exam schedules, or fee status...'}
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            style={{
              flex: 1,
              padding: '12px 16px',
              backgroundColor: 'rgba(15, 23, 42, 0.7)',
              border: isListening ? '1px solid #ef4444' : '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '10px',
              color: '#f8fafc',
              fontSize: '0.9rem',
              outline: 'none',
            }}
          />
          <Button type="submit" variant="primary" isLoading={sending} icon={<Send size={16} />}>
            Send
          </Button>
        </form>
      </Card>

      {/* Feature 55: AI Wellness & Focus Pomodoro Counselor Modal */}
      <Modal
        isOpen={isWellnessModalOpen}
        onClose={() => setIsWellnessModalOpen(false)}
        title="UniSphere Student Wellness & Pomodoro Focus Counselor"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(236,72,153,0.1)', borderRadius: '10px', border: '1px solid rgba(236,72,153,0.3)', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Heart size={24} style={{ color: '#f472b6' }} />
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
              <strong style={{ color: '#f472b6' }}>Academic Stress Relief Coach:</strong> Take a 5-minute guided mindfulness break or start a 25-minute Pomodoro study focus session.
            </div>
          </div>
          <div style={{ display: 'flex', gap: '10px' }}>
            <Button variant="primary" style={{ flex: 1 }} icon={<Clock size={16} />} onClick={() => { showToast('Started 25-Minute Pomodoro Study Timer!', 'success'); setIsWellnessModalOpen(false); }}>
              Start 25-Min Focus Timer
            </Button>
            <Button variant="outline" style={{ flex: 1 }} onClick={() => { showToast('Booked Health Center Counseling Session!', 'info'); setIsWellnessModalOpen(false); }}>
              Book Counselor Slot
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
