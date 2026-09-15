import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { ShieldCheck, Search, CheckCircle2, XCircle } from 'lucide-react';

export const PublicIdVerificationPage: React.FC = () => {
  const [cardNumber, setCardNumber] = useState('US-ID-2026-8801A');
  const [verifiedData, setVerifiedData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleVerify = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/api/v1/digital-ids/verify/${cardNumber}`);
      const data = await response.json();
      setVerifiedData(data);
    } catch (err) {
      setVerifiedData(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto', textAlign: 'center' }}>
      <div style={{ marginBottom: '2rem' }}>
        <img src="/logo.png" alt="Logo" style={{ width: '64px', height: '64px', margin: '0 auto 12px auto' }} />
        <h1 style={{ fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Public Digital ID Verification
        </h1>
        <p style={{ color: '#94a3b8', margin: '6px 0 0 0', fontSize: '0.85rem' }}>
          Verify active student or faculty credentials issued by UniSphere AI
        </p>
      </div>

      <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', marginBottom: '1.5rem' }}>
        <form onSubmit={handleVerify} style={{ display: 'flex', gap: '8px' }}>
          <input
            type="text"
            required
            value={cardNumber}
            onChange={(e) => setCardNumber(e.target.value)}
            placeholder="Enter ID Card Number"
            style={{ flex: 1, padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
          />
          <Button type="submit" variant="primary" isLoading={loading}>
            Verify ID
          </Button>
        </form>
      </Card>

      {verifiedData && (
        <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(16, 185, 129, 0.08)', border: '1px solid rgba(16, 185, 129, 0.3)', textAlign: 'left' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1rem' }}>
            <CheckCircle2 size={24} color="#10b981" />
            <div>
              <h3 style={{ margin: 0, color: '#10b981', fontSize: '1.1rem' }}>Valid Active Identity</h3>
              <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Verified at {new Date(verifiedData.verification_timestamp).toLocaleString()}</span>
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', fontSize: '0.85rem', color: '#cbd5e1' }}>
            <div>Holder: <strong style={{ color: '#fff' }}>{verifiedData.holder_name}</strong></div>
            <div>Role: <strong style={{ color: '#fff' }}>{verifiedData.role}</strong></div>
            <div>Department: <strong style={{ color: '#fff' }}>{verifiedData.department}</strong></div>
            <div>Status: <strong style={{ color: '#10b981' }}>{verifiedData.status}</strong></div>
          </div>
        </Card>
      )}
    </div>
  );
};
