import React, { useState } from 'react';
import { Building2, Shield, Globe, Mail, CheckCircle2, AlertCircle } from 'lucide-react';
import { Button } from '../../components/Button';
import { BrandingPreview } from '../../components/tenants/BrandingPreview';

export const TenantOnboardingPage: React.FC = () => {
  const [name, setName] = useState('');
  const [code, setCode] = useState('');
  const [adminEmail, setAdminEmail] = useState('');
  const [domain, setDomain] = useState('');
  const [primaryColor, setPrimaryColor] = useState('#1E40AF');
  const [secondaryColor, setSecondaryColor] = useState('#3B82F6');
  const [accentColor, setAccentColor] = useState('#10B981');
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (!name || !code || !adminEmail) {
      setError('Please fill in all required tenant onboarding fields.');
      return;
    }
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      setSuccess(true);
    }, 1000);
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1200px', margin: '0 auto', color: '#f8fafc' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ margin: 0, fontSize: '1.8rem', fontWeight: 800 }}>
          Multi-Tenant University Onboarding
        </h1>
        <p style={{ margin: '6px 0 0 0', color: '#94a3b8', fontSize: '0.9rem' }}>
          Provision a isolated university tenant instance with custom branding, domain isolation, and default administrative access.
        </p>
      </div>

      {success ? (
        <div
          style={{
            backgroundColor: 'rgba(16, 185, 129, 0.1)',
            border: '1px solid rgba(16, 185, 129, 0.3)',
            borderRadius: '16px',
            padding: '2.5rem',
            textAlign: 'center',
          }}
        >
          <CheckCircle2 size={48} color="#10b981" style={{ margin: '0 auto 1rem auto' }} />
          <h2 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 700 }}>
            University Tenant Onboarded Successfully!
          </h2>
          <p style={{ color: '#cbd5e1', margin: '8px 0 1.5rem 0' }}>
            Tenant <strong>{name}</strong> ({code}) has been provisioned. An administrator invitation email has been dispatched to <strong>{adminEmail}</strong>.
          </p>
          <Button variant="primary" onClick={() => setSuccess(false)}>
            Onboard Another Tenant
          </Button>
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
          {/* Onboarding Form */}
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              borderRadius: '16px',
              padding: '2rem',
            }}
          >
            <h3 style={{ margin: '0 0 1.5rem 0', fontSize: '1.2rem', fontWeight: 700 }}>
              Tenant Profile & Credentials
            </h3>

            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                  University Full Name *
                </label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Stanford Technological University"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px',
                    borderRadius: '8px',
                    backgroundColor: 'rgba(15, 23, 42, 0.8)',
                    border: '1px solid rgba(255,255,255,0.12)',
                    color: '#ffffff',
                  }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                  Unique Tenant Code *
                </label>
                <input
                  type="text"
                  required
                  placeholder="e.g. STANFORD-TECH"
                  value={code}
                  onChange={(e) => setCode(e.target.value.toUpperCase())}
                  style={{
                    width: '100%',
                    padding: '10px 12px',
                    borderRadius: '8px',
                    backgroundColor: 'rgba(15, 23, 42, 0.8)',
                    border: '1px solid rgba(255,255,255,0.12)',
                    color: '#ffffff',
                    fontFamily: 'monospace',
                  }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                  Tenant Admin Contact Email *
                </label>
                <input
                  type="email"
                  required
                  placeholder="admin@stanfordtech.edu"
                  value={adminEmail}
                  onChange={(e) => setAdminEmail(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px',
                    borderRadius: '8px',
                    backgroundColor: 'rgba(15, 23, 42, 0.8)',
                    border: '1px solid rgba(255,255,255,0.12)',
                    color: '#ffffff',
                  }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
                  Custom Domain (Optional)
                </label>
                <input
                  type="text"
                  placeholder="portal.stanfordtech.edu"
                  value={domain}
                  onChange={(e) => setDomain(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px',
                    borderRadius: '8px',
                    backgroundColor: 'rgba(15, 23, 42, 0.8)',
                    border: '1px solid rgba(255,255,255,0.12)',
                    color: '#ffffff',
                  }}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '0.75rem', color: '#94a3b8', marginBottom: '4px' }}>Primary Color</label>
                  <input type="color" value={primaryColor} onChange={(e) => setPrimaryColor(e.target.value)} style={{ width: '100%', height: '36px', border: 'none', borderRadius: '6px', cursor: 'pointer' }} />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.75rem', color: '#94a3b8', marginBottom: '4px' }}>Secondary Color</label>
                  <input type="color" value={secondaryColor} onChange={(e) => setSecondaryColor(e.target.value)} style={{ width: '100%', height: '36px', border: 'none', borderRadius: '6px', cursor: 'pointer' }} />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.75rem', color: '#94a3b8', marginBottom: '4px' }}>Accent Color</label>
                  <input type="color" value={accentColor} onChange={(e) => setAccentColor(e.target.value)} style={{ width: '100%', height: '36px', border: 'none', borderRadius: '6px', cursor: 'pointer' }} />
                </div>
              </div>

              {error && (
                <div style={{ color: '#ef4444', fontSize: '0.85rem', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <AlertCircle size={16} /> {error}
                </div>
              )}

              <Button type="submit" variant="primary" size="lg" isLoading={loading} style={{ marginTop: '1rem' }}>
                Provision Tenant Instance
              </Button>
            </form>
          </div>

          {/* Live Preview Column */}
          <div>
            <BrandingPreview
              primaryColor={primaryColor}
              secondaryColor={secondaryColor}
              accentColor={accentColor}
              portalTitle={name || 'University Portal'}
              customDomain={domain}
              supportEmail={adminEmail}
            />
          </div>
        </div>
      )}
    </div>
  );
};
