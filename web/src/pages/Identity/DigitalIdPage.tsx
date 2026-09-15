import React, { useState, useEffect } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { QrCode, ShieldCheck, RefreshCw, Smartphone, CheckCircle, Clock } from 'lucide-react';

export const DigitalIdPage: React.FC = () => {
  const [seconds, setSeconds] = useState(30);

  useEffect(() => {
    const timer = setInterval(() => {
      setSeconds((prev) => (prev <= 1 ? 30 : prev - 1));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Digital Campus ID & Gate Access
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Official University NFC & Time-Sensitive QR Digital Identification
        </p>
      </div>

      {/* Digital ID Card Container */}
      <div
        style={{
          width: '100%',
          maxWidth: '440px',
          margin: '0 auto',
          background: 'linear-gradient(135deg, #0f172a 0%, #1e293b 100%)',
          border: '1px solid rgba(56, 189, 248, 0.3)',
          borderRadius: '24px',
          padding: '2rem',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6)',
          position: 'relative',
        }}
      >
        {/* Card Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <img src="/logo.png" alt="Logo" style={{ width: '32px', height: '32px', objectFit: 'contain' }} />
            <span style={{ fontWeight: 800, color: '#fff', fontSize: '1.1rem' }}>UniSphere AI</span>
          </div>
          <span style={{ padding: '4px 10px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.2)', color: '#10b981', fontWeight: 700, fontSize: '0.75rem' }}>
            ACTIVE STUDENT
          </span>
        </div>

        {/* Student Photo & Details */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem', marginBottom: '1.5rem' }}>
          <div style={{ width: '72px', height: '72px', borderRadius: '20px', background: 'linear-gradient(135deg, #2563eb, #38bdf8)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 800, fontSize: '1.8rem' }}>
            AM
          </div>
          <div>
            <h2 style={{ margin: 0, fontSize: '1.4rem', color: '#f8fafc', fontWeight: 800 }}>Alex Morgan</h2>
            <p style={{ margin: '2px 0 0 0', color: '#38bdf8', fontSize: '0.85rem', fontWeight: 600 }}>ID: US-ID-2026-8801A</p>
            <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Computer Science & AI • Exp: 06/2028</span>
          </div>
        </div>

        {/* Dynamic Anti-Spoofing QR */}
        <div style={{ padding: '1.25rem', background: '#ffffff', borderRadius: '16px', textAlign: 'center', marginBottom: '1rem' }}>
          <div style={{ width: '140px', height: '140px', margin: '0 auto', border: '6px solid #0f172a', borderRadius: '8px', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '4px', padding: '4px' }}>
            {Array.from({ length: 16 }).map((_, i) => (
              <div key={i} style={{ backgroundColor: (i * 5 + seconds) % 2 === 0 ? '#0f172a' : '#2563eb', borderRadius: '2px' }} />
            ))}
          </div>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', color: '#0f172a', fontWeight: 700, fontSize: '0.8rem', marginTop: '8px' }}>
            <Clock size={14} /> Refreshes in {seconds}s
          </span>
        </div>

        <div style={{ textAlign: 'center', fontSize: '0.75rem', color: '#94a3b8' }}>
          Hold near turnstile NFC reader or show QR code to campus security.
        </div>
      </div>
    </div>
  );
};
