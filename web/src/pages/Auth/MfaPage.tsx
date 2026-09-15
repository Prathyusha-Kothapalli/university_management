import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useToast } from '../../hooks/useToast';
import { Button } from '../../components/Button';
import { ShieldCheck, Smartphone, KeyRound, Copy } from 'lucide-react';

export const MfaPage: React.FC = () => {
  const { showToast } = useToast();
  const navigate = useNavigate();

  const [otpCode, setOtpCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [mfaSecret, setMfaSecret] = useState<string | null>(null);
  const [backupCodes, setBackupCodes] = useState<string[]>([]);

  const handleEnableMfa = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/mfa/enable', {
        method: 'POST',
        headers: { Authorization: 'Bearer DEMO_TOKEN' },
      });
      const data = await response.json();
      setMfaSecret(data.secret);
      setBackupCodes(data.backup_codes || []);
      showToast('2FA setup initiated. Scan QR or save secret code.', 'info');
    } catch (err: any) {
      showToast('Error enabling MFA', 'error');
    }
  };

  const handleVerifyOtp = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/mfa/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: '00000000-0000-0000-0000-000000000000', code: otpCode }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'OTP verification failed');

      showToast('2FA Verification successful!', 'success');
      navigate('/dashboard');
    } catch (err: any) {
      showToast(err.message || 'Invalid OTP Code', 'error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'radial-gradient(circle at 50% 30%, rgba(37, 99, 235, 0.15), rgba(15, 23, 42, 1) 70%)',
        padding: '1.5rem',
      }}
    >
      <div
        style={{
          width: '100%',
          maxWidth: '460px',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          borderRadius: '20px',
          padding: '2.5rem 2rem',
          boxShadow: '0 25px 60px rgba(0, 0, 0, 0.6)',
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: '1.5rem' }}>
          <div
            style={{
              width: '54px',
              height: '54px',
              borderRadius: '14px',
              background: 'linear-gradient(135deg, #10b981, #3b82f6)',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto 12px auto',
            }}
          >
            <ShieldCheck size={28} />
          </div>
          <h2 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>
            Two-Factor Authentication
          </h2>
          <p style={{ margin: '6px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Secure your university account with TOTP authenticator app
          </p>
        </div>

        {!mfaSecret ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <form onSubmit={handleVerifyOtp} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                  6-Digit OTP Code
                </label>
                <input
                  type="text"
                  required
                  maxLength={6}
                  placeholder="123456"
                  value={otpCode}
                  onChange={(e) => setOtpCode(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '12px',
                    backgroundColor: 'rgba(15, 23, 42, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '10px',
                    color: '#38bdf8',
                    fontSize: '1.4rem',
                    fontWeight: 700,
                    textAlign: 'center',
                    letterSpacing: '6px',
                  }}
                />
              </div>

              <Button type="submit" variant="primary" size="lg" isLoading={loading} style={{ width: '100%' }}>
                Verify & Login
              </Button>
            </form>

            <div style={{ borderTop: '1px solid rgba(255, 255, 255, 0.1)', paddingTop: '1rem', textAlign: 'center' }}>
              <button
                type="button"
                onClick={handleEnableMfa}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#38bdf8',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Configure / Enable 2FA Authenticator App
              </button>
            </div>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ padding: '1rem', backgroundColor: 'rgba(255, 255, 255, 0.05)', borderRadius: '12px', border: '1px solid rgba(255, 255, 255, 0.1)' }}>
              <p style={{ margin: 0, fontSize: '0.8rem', color: '#94a3b8' }}>Secret Key:</p>
              <code style={{ fontSize: '1rem', color: '#38bdf8', fontWeight: 700 }}>{mfaSecret}</code>
            </div>

            {backupCodes.length > 0 && (
              <div>
                <p style={{ margin: '0 0 6px 0', fontSize: '0.8rem', color: '#cbd5e1', fontWeight: 600 }}>Emergency Recovery Backup Codes:</p>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px' }}>
                  {backupCodes.map((code, idx) => (
                    <div key={idx} style={{ padding: '6px', backgroundColor: 'rgba(0,0,0,0.3)', borderRadius: '6px', fontSize: '0.75rem', fontFamily: 'monospace', color: '#10b981', textAlign: 'center' }}>
                      {code}
                    </div>
                  ))}
                </div>
              </div>
            )}

            <Button onClick={() => setMfaSecret(null)} variant="secondary" style={{ width: '100%' }}>
              Done / Return to Verification
            </Button>
          </div>
        )}
      </div>
    </div>
  );
};
