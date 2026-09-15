import React, { useState } from 'react';
import { Mic, MicOff, Volume2, VolumeX, Sparkles } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const AiVoiceAssistant: React.FC = () => {
  const { showToast } = useToast();
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [transcript, setTranscript] = useState('');

  const toggleListening = () => {
    if (!isListening) {
      setIsListening(true);
      showToast('Listening... Speak your prompt into microphone', 'info');
      setTranscript('What is my upcoming exam schedule and library fine status?');
      setTimeout(() => {
        setIsListening(false);
        setIsSpeaking(true);
        showToast('AI Voice Copilot: Responding via Voice Output', 'success');
        setTimeout(() => setIsSpeaking(false), 3000);
      }, 2500);
    } else {
      setIsListening(false);
    }
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(168, 85, 247, 0.3)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <button
          onClick={toggleListening}
          style={{
            width: '48px',
            height: '48px',
            borderRadius: '50%',
            backgroundColor: isListening ? '#f43f5e' : '#a855f7',
            border: 'none',
            color: '#ffffff',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            boxShadow: isListening ? '0 0 20px rgba(244, 63, 94, 0.6)' : '0 4px 14px rgba(168, 85, 247, 0.4)',
            transition: 'all 0.2s ease',
          }}
        >
          {isListening ? <MicOff size={22} /> : <Mic size={22} />}
        </button>
        <div>
          <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Sparkles size={16} color="#a855f7" /> AI Voice Copilot (Speech-to-Text & Voice Output)
          </h4>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            {isListening
              ? 'Listening to microphone...'
              : isSpeaking
              ? '🔊 Voice Assistant Speaking...'
              : transcript
              ? `Recognized: "${transcript}"`
              : 'Tap mic to speak voice commands to UniSphere AI'}
          </p>
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <button
          onClick={() => {
            setIsSpeaking(!isSpeaking);
            showToast(isSpeaking ? 'Muted AI Voice Output' : 'Unmuted AI Voice Output', 'info');
          }}
          style={{
            backgroundColor: 'rgba(255, 255, 255, 0.05)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            color: isSpeaking ? '#a855f7' : '#94a3b8',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.75rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          {isSpeaking ? <Volume2 size={14} /> : <VolumeX size={14} />} {isSpeaking ? 'Voice Active' : 'Muted'}
        </button>
      </div>
    </div>
  );
};
