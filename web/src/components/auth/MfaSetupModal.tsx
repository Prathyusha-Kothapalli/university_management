import React, { useState } from 'react';
import { ShieldCheck, Copy, Check, QrCode, Key, AlertCircle } from 'lucide-react';

interface MfaSetupModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSuccess: () => void;
}

export const MfaSetupModal: React.FC<MfaSetupModalProps> = ({ isOpen, onClose, onSuccess }) => {
  const [step, setStep] = useState<1 | 2>(1);
  const [verificationCode, setVerificationCode] = useState('');
  const [copiedSecret, setCopiedSecret] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const sampleSecret = 'JBSWY3DPEHPK3PXP';
  const sampleBackupCodes = [
    'A1B2-C3D4', 'E5F6-G7H8', 'I9J0-K1L2', 'M3N4-O5P6',
    'Q7R8-S9T0', 'U1V2-W3X4', 'Y5Z6-A7B8', 'C9D0-E1F2'
  ];

  if (!isOpen) return null;

  const handleCopySecret = () => {
    navigator.clipboard.writeText(sampleSecret);
    setCopiedSecret(true);
    setTimeout(() => setCopiedSecret(false), 2000);
  };

  const handleVerify = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (verificationCode.trim().length !== 6) {
      setError('Please enter a valid 6-digit TOTP verification code.');
      return;
    }
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      onSuccess();
      onClose();
    }, 800);
  };

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(8px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        padding: '1rem',
      }}
    >
      <div
        style={{
          backgroundColor: '#0f172a',
          border: '1px solid rgba(255, 255, 255, 0.15)',
          borderRadius: '16px',
          width: '100%',
          maxWidth: '520px',
          padding: '2rem',
          boxShadow: '0 20px 50px rgba(0,0,0,0.8)',
          color: '#f8fafc',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '1.5rem' }}>
          <div
            style={{
              padding: '10px',
              borderRadius: '12px',
              backgroundColor: 'rgba(37, 99, 235, 0.15)',
              color: '#3b82f6',
            }}
          >
            <ShieldCheck size={24} />
          </div>
          <div>
            <h3 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 700 }}>
              Two-Factor Authentication (2FA) Setup
            </h3>
            <p style={{ margin: '2px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
              Protect your account with an Authenticator App (Google Authenticator, Authy, 1Password)
            </p>
          </div>
        </div>

        {step === 1 ? (
          <div>
            <div
              style={{
                backgroundColor: 'rgba(255, 255, 255, 0.03)',
                border: '1px dashed rgba(255, 255, 255, 0.15)',
                borderRadius: '12px',
                padding: '1.25rem',
                textAlign: 'center',
                marginBottom: '1.5rem',
              }}
            >
              <div
                style={{
                  width: '140px',
                  height: '140px',
                  backgroundColor: '#ffffff',
                  margin: '0 auto 1rem auto',
                  borderRadius: '10px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '8px',
                }}
              >
                <QrCode size={110} color="#0f172a" />
              </div>
              <p style={{ fontSize: '0.8rem', color: '#cbd5e1', margin: '0 0 8px 0' }}>
                Scan this QR code with your Authenticator app, or enter secret key manually:
              </p>

              <div
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '8px',
                  backgroundColor: 'rgba(15, 23, 42, 0.9)',
                  padding: '6px 14px',
                  borderRadius: '8px',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  fontFamily: 'monospace',
                  letterSpacing: '1px',
                  fontSize: '0.9rem',
                }}
              >
                <Key size={14} color="#38bdf8" />
                <span>{sampleSecret}</span>
                <button
                  onClick={handleCopySecret}
                  style={{
                    background: 'none',
                    border: 'none',
                    color: copiedSecret ? '#10b981' : '#94a3b8',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  {copiedSecret ? <Check size={14} /> : <Copy size={14} />}
                </button>
              </div>
            </div>

            <div style={{ marginBottom: '1.5rem' }}>
              <h4 style={{ margin: '0 0 8px 0', fontSize: '0.9rem', color: '#f1f5f9' }}>
                Emergency Backup Recovery Codes
              </h4>
              <div
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(2, 1fr)',
                  gap: '8px',
                  backgroundColor: 'rgba(15, 23, 42, 0.8)',
                  padding: '10px',
                  borderRadius: '10px',
                  border: '1px solid rgba(255, 255, 255, 0.08)',
                  fontFamily: 'monospace',
                  fontSize: '0.8rem',
                  color: '#38bdf8',
                }}
              >
                {sampleBackupCodes.map((c, i) => (
                  <div key={i} style={{ textAlign: 'center', padding: '4px', backgroundColor: 'rgba(255, 255, 255, 0.03)', borderRadius: '6px' }}>
                    {c}
                  </div>
                ))}
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px' }}>
              <button
                type="button"
                onClick={onClose}
                style={{
                  padding: '8px 16px',
                  borderRadius: '8px',
                  border: '1px solid rgba(255, 255, 255, 0.15)',
                  backgroundColor: 'transparent',
                  color: '#cbd5e1',
                  cursor: 'pointer',
                }}
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={() => setStep(2)}
                style={{
                  padding: '8px 18px',
                  borderRadius: '8px',
                  border: 'none',
                  backgroundColor: '#2563eb',
                  color: '#ffffff',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Next: Verify Code
              </button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleVerify}>
            <div style={{ marginBottom: '1.5rem' }}>
              <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, marginBottom: '8px', color: '#cbd5e1' }}>
                Enter 6-Digit Authenticator Code
              </label>
              <input
                type="text"
                maxLength={6}
                placeholder="123456"
                value={verificationCode}
                onChange={(e) => setVerificationCode(e.target.value.replace(/\D/g, ''))}
                style={{
                  width: '100%',
                  padding: '12px',
                  borderRadius: '10px',
                  backgroundColor: 'rgba(15, 23, 42, 0.9)',
                  border: '1px solid rgba(37, 99, 235, 0.4)',
                  color: '#ffffff',
                  fontSize: '1.25rem',
                  letterSpacing: '4px',
                  textAlign: 'center',
                  fontFamily: 'monospace',
                  outline: 'none',
                }}
              />
              {error && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginTop: '8px', color: '#ef4444', fontSize: '0.8rem' }}>
                  <AlertCircle size={14} />
                  <span>{error}</span>
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', gap: '12px' }}>
              <button
                type="button"
                onClick={() => setStep(1)}
                style={{
                  padding: '8px 16px',
                  borderRadius: '8px',
                  border: '1px solid rgba(255, 255, 255, 0.15)',
                  backgroundColor: 'transparent',
                  color: '#cbd5e1',
                  cursor: 'pointer',
                }}
              >
                Back
              </button>
              <button
                type="submit"
                disabled={loading}
                style={{
                  padding: '8px 20px',
                  borderRadius: '8px',
                  border: 'none',
                  backgroundColor: '#10b981',
                  color: '#ffffff',
                  fontWeight: 600,
                  cursor: 'pointer',
                  opacity: loading ? 0.7 : 1,
                }}
              >
                {loading ? 'Verifying...' : 'Enable 2FA Protection'}
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};
