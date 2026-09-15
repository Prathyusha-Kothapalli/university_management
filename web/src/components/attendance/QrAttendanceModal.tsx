import React, { useState, useEffect } from 'react';
import { Modal } from '../Modal';
import { Button } from '../Button';
import { QrCode, RefreshCw, CheckCircle2, Clock } from 'lucide-react';

interface QrModalProps {
  isOpen: boolean;
  onClose: () => void;
  sessionTitle: string;
}

export const QrAttendanceModal: React.FC<QrModalProps> = ({ isOpen, onClose, sessionTitle }) => {
  const [qrCodeToken, setQrCodeToken] = useState('QR:SESSION_881A:TOKEN_9921:SHA_90A1F');
  const [secondsRemaining, setSecondsRemaining] = useState(45);
  const [checkedInCount, setCheckedInCount] = useState(28);

  useEffect(() => {
    if (!isOpen) return;
    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          setQrCodeToken(`QR:SESSION_881A:TOKEN_${Math.floor(Math.random() * 9000 + 1000)}:SHA_${Math.floor(Math.random() * 9000 + 1000)}`);
          return 60;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isOpen]);

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={`Live QR Check-in: ${sessionTitle}`}>
      <div style={{ textAlign: 'center', padding: '1rem' }}>
        <div
          style={{
            width: '220px',
            height: '220px',
            margin: '0 auto 1.5rem auto',
            backgroundColor: '#ffffff',
            borderRadius: '16px',
            padding: '16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
          }}
        >
          {/* Simulated High-Res QR Matrix */}
          <div style={{ width: '100%', height: '100%', border: '8px solid #0f172a', borderRadius: '8px', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '4px', padding: '6px' }}>
            {Array.from({ length: 16 }).map((_, i) => (
              <div
                key={i}
                style={{
                  backgroundColor: (i * 7 + secondsRemaining) % 2 === 0 ? '#0f172a' : '#38bdf8',
                  borderRadius: '2px',
                }}
              />
            ))}
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', color: '#38bdf8', fontWeight: 700, fontSize: '1rem', marginBottom: '8px' }}>
          <Clock size={18} /> Refreshing in {secondsRemaining}s
        </div>

        <p style={{ color: '#94a3b8', fontSize: '0.85rem', margin: '0 0 1.5rem 0' }}>
          Students scan with the UniSphere mobile app to verify lecture attendance.
        </p>

        <div style={{ padding: '12px', background: 'rgba(16, 185, 129, 0.1)', borderRadius: '12px', border: '1px solid rgba(16, 185, 129, 0.3)', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', color: '#10b981', fontWeight: 700 }}>
          <CheckCircle2 size={18} /> {checkedInCount} Students Live Checked-In
        </div>
      </div>
    </Modal>
  );
};
