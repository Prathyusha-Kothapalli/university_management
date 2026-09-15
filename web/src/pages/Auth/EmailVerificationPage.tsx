import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { useToast } from '../../hooks/useToast';
import { Button } from '../../components/Button';
import { CheckCircle2, XCircle, MailCheck, ArrowRight } from 'lucide-react';

export const EmailVerificationPage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const { showToast } = useToast();
  const [token, setToken] = useState(searchParams.get('token') || '');
  const [verifying, setVerifying] = useState(false);
  const [verified, setVerified] = useState(false);

  useEffect(() => {
    if (token) {
      handleVerify(token);
    }
  }, []);

  const handleVerify = async (tok: string) => {
    setVerifying(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/verify-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: tok }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || 'Verification failed');
      }
      setVerified(true);
      showToast('Email verified successfully!', 'success');
    } catch (err: any) {
      showToast(err.message || 'Email verification failed', 'error');
    } finally {
      setVerifying(false);
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
          maxWidth: '440px',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          borderRadius: '20px',
          padding: '2.5rem 2rem',
          boxShadow: '0 25px 60px rgba(0, 0, 0, 0.6)',
          textAlign: 'center',
        }}
      >
        <div style={{ marginBottom: '1.5rem' }}>
          <div
            style={{
              width: '64px',
              height: '64px',
              borderRadius: '20px',
              background: verified ? 'linear-gradient(135deg, #10b981, #059669)' : 'linear-gradient(135deg, #2563eb, #0ea5e9)',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto 16px auto',
            }}
          >
            {verified ? <CheckCircle2 size={32} /> : <MailCheck size={32} />}
          </div>
          <h2 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>
            {verified ? 'Email Verified!' : 'Verify Your Email'}
          </h2>
          <p style={{ margin: '8px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            {verified
              ? 'Your university account is now fully activated and verified.'
              : 'Confirming your student/faculty email address for portal access.'}
          </p>
        </div>

        {!verified && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <input
              type="text"
              placeholder="Paste verification token"
              value={token}
              onChange={(e) => setToken(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 12px',
                backgroundColor: 'rgba(15, 23, 42, 0.7)',
                border: '1px solid rgba(255, 255, 255, 0.12)',
                borderRadius: '10px',
                color: '#f8fafc',
                fontSize: '0.85rem',
              }}
            />
            <Button
              onClick={() => handleVerify(token)}
              variant="primary"
              size="lg"
              isLoading={verifying}
              style={{ width: '100%' }}
            >
              Verify Token Now
            </Button>
          </div>
        )}

        {verified && (
          <Link
            to="/auth/login"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '8px',
              width: '100%',
              padding: '12px',
              backgroundColor: '#2563eb',
              color: '#ffffff',
              borderRadius: '10px',
              fontWeight: 600,
              textDecoration: 'none',
              marginTop: '1rem',
            }}
          >
            Continue to Sign In <ArrowRight size={16} />
          </Link>
        )}
      </div>
    </div>
  );
};
