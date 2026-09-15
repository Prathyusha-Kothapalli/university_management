import React, { useState } from 'react';
import { Plus } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const DigitalWalletCard: React.FC = () => {
  const { showToast } = useToast();
  const [balance, setBalance] = useState(2450);

  const handleTopup = () => {
    setBalance(balance + 500);
    showToast('Added ₹500 to UniSphere NFC Campus Wallet via UPI', 'success');
  };

  return (
    <div
      style={{
        background: 'linear-gradient(135deg, rgba(37, 99, 235, 0.3), rgba(14, 165, 233, 0.2))',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(56, 189, 248, 0.3)',
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
      <div>
        <div style={{ fontSize: '0.78rem', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '1px', fontWeight: 600 }}>
          Campus NFC Digital Wallet
        </div>
        <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', margin: '4px 0' }}>
          ₹{balance.toLocaleString('en-IN')}
        </div>
        <div style={{ fontSize: '0.75rem', color: '#cbd5e1' }}>
          Valid at Canteen, Library Fines, Campus Store & Printing Kiosks
        </div>
      </div>

      <button
        onClick={handleTopup}
        style={{
          backgroundColor: '#38bdf8',
          border: 'none',
          color: '#0f172a',
          borderRadius: '10px',
          padding: '8px 16px',
          fontSize: '0.825rem',
          fontWeight: 700,
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          boxShadow: '0 4px 14px rgba(56, 189, 248, 0.4)',
        }}
      >
        <Plus size={16} /> Top-Up Wallet (+₹500)
      </button>
    </div>
  );
};
