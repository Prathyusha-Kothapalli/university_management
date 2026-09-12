import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useToast } from '../../hooks/useToast';
import { Button } from '../../components/Button';
import { Mail, KeyRound, ArrowLeft } from 'lucide-react';

export const ForgotPasswordPage: React.FC = () => {
  const { showToast } = useToast();
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [submittedToken, setSubmittedToken] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || 'Request failed');
      }
      showToast('Password reset link generated successfully.', 'success');
      if (data.reset_token) {
        setSubmittedToken(data.reset_token);
      }
    } catch (err: any) {
      showToast(err.message || 'Error sending request', 'error');
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
          maxWidth: '440px',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          borderRadius: '20px',
          padding: '2.5rem 2rem',
          boxShadow: '0 25px 60px rgba(0, 0, 0, 0.6)',
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <div
            style={{
              width: '54px',
              height: '54px',
              borderRadius: '14px',
              background: 'linear-gradient(135deg, #0ea5e9, #6366f1)',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto 12px auto',
            }}
          >
            <KeyRound size={26} />
          </div>
          <h2 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>
            Forgot Password?
          </h2>
          <p style={{ margin: '6px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Enter your university email to receive password reset instructions
          </p>
        </div>

        {!submittedToken ? (
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                University Email Address
              </label>
              <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
                <Mail size={16} style={{ position: 'absolute', left: '12px', color: '#64748b' }} />
                <input
                  type="email"
                  required
                  placeholder="alex.morgan@unisphere.edu"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px 10px 38px',
                    backgroundColor: 'rgba(15, 23, 42, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '10px',
                    color: '#f8fafc',
                    fontSize: '0.9rem',
                  }}
                />
              </div>
            </div>

            <Button type="submit" variant="primary" size="lg" isLoading={loading} style={{ width: '100%' }}>
              Send Reset Link
            </Button>
          </form>
        ) : (
          <div style={{ textAlign: 'center', padding: '1rem 0' }}>
            <div style={{ padding: '1rem', background: 'rgba(16, 185, 129, 0.1)', border: '1px solid rgba(16, 185, 129, 0.3)', borderRadius: '12px', marginBottom: '1.5rem' }}>
              <p style={{ margin: 0, color: '#10b981', fontSize: '0.9rem', fontWeight: 600 }}>Reset Token Dispatched</p>
              <p style={{ margin: '6px 0 0 0', color: '#cbd5e1', fontSize: '0.8rem', wordBreak: 'break-all' }}>
                Token: <code>{submittedToken}</code>
              </p>
            </div>
            <Link
              to={`/auth/reset-password?token=${submittedToken}`}
              style={{
                display: 'inline-block',
                width: '100%',
                padding: '10px',
                backgroundColor: '#2563eb',
                color: '#fff',
                borderRadius: '10px',
                textDecoration: 'none',
                fontWeight: 600,
              }}
            >
              Proceed to Reset Form
            </Link>
          </div>
        )}

        <div style={{ textAlign: 'center', marginTop: '1.5rem' }}>
          <Link to="/auth/login" style={{ color: '#94a3b8', textDecoration: 'none', fontSize: '0.85rem', display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
            <ArrowLeft size={14} /> Back to Sign In
          </Link>
        </div>
      </div>
    </div>
  );
};
