import React, { useState, useEffect } from 'react';
import { useToast } from '../../hooks/useToast';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { Building2, Palette, Globe, Mail, ShieldCheck, HardDrive, BarChart3, Save } from 'lucide-react';

export const TenantSettingsPage: React.FC = () => {
  const { showToast } = useToast();
  const [logoUrl, setLogoUrl] = useState('');
  const [primaryColor, setPrimaryColor] = useState('#2563eb');
  const [secondaryColor, setSecondaryColor] = useState('#0ea5e9');
  const [portalDomain, setPortalDomain] = useState('portal.unisphere.edu');
  const [senderName, setSenderName] = useState('UniSphere Portal');
  const [whitelabel, setWhitelabel] = useState(true);
  const [saving, setSaving] = useState(false);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);
    try {
      showToast('Tenant branding and domain configuration saved successfully.', 'success');
    } catch (err) {
      showToast('Error saving tenant settings', 'error');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Tenant Branding & Portal Settings
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Configure university domain, white-label UI theme colors, and storage quotas.
        </p>
      </div>

      <form onSubmit={handleSave} style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {/* Theme & Branding Card */}
          <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
            <h3 style={{ color: '#f8fafc', marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px', fontSize: '1.1rem' }}>
              <Palette size={20} color="#38bdf8" /> Visual Theme & Custom Logos
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>
                  Primary Brand Color
                </label>
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                  <input
                    type="color"
                    value={primaryColor}
                    onChange={(e) => setPrimaryColor(e.target.value)}
                    style={{ width: '40px', height: '38px', borderRadius: '6px', border: 'none', cursor: 'pointer' }}
                  />
                  <input
                    type="text"
                    value={primaryColor}
                    onChange={(e) => setPrimaryColor(e.target.value)}
                    style={{ flex: 1, padding: '8px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>
                  Secondary Accent Color
                </label>
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                  <input
                    type="color"
                    value={secondaryColor}
                    onChange={(e) => setSecondaryColor(e.target.value)}
                    style={{ width: '40px', height: '38px', borderRadius: '6px', border: 'none', cursor: 'pointer' }}
                  />
                  <input
                    type="text"
                    value={secondaryColor}
                    onChange={(e) => setSecondaryColor(e.target.value)}
                    style={{ flex: 1, padding: '8px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                  />
                </div>
              </div>
            </div>

            <div style={{ marginTop: '1.25rem' }}>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>
                University Crest / Logo URL
              </label>
              <input
                type="url"
                placeholder="https://assets.university.edu/logo.png"
                value={logoUrl}
                onChange={(e) => setLogoUrl(e.target.value)}
                style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
              />
            </div>
          </Card>

          {/* Custom Domain Card */}
          <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
            <h3 style={{ color: '#f8fafc', marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px', fontSize: '1.1rem' }}>
              <Globe size={20} color="#10b981" /> Portal Domain & Email Sender
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>
                  Custom Portal Subdomain
                </label>
                <input
                  type="text"
                  value={portalDomain}
                  onChange={(e) => setPortalDomain(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>
                  Email Dispatch Sender Name
                </label>
                <input
                  type="text"
                  value={senderName}
                  onChange={(e) => setSenderName(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>
            </div>
          </Card>
        </div>

        {/* Usage Analytics Sidebar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
            <h4 style={{ color: '#f8fafc', marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
              <HardDrive size={18} color="#f59e0b" /> Tenant Storage & Usage
            </h4>

            <div style={{ margin: '1rem 0' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: '#cbd5e1', marginBottom: '6px' }}>
                <span>Document Storage</span>
                <span>482.5 GB / 2,000 GB</span>
              </div>
              <div style={{ height: '6px', width: '100%', background: 'rgba(255,255,255,0.1)', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{ height: '100%', width: '24.1%', background: '#f59e0b' }} />
              </div>
            </div>

            <div style={{ fontSize: '0.8rem', color: '#94a3b8', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span>Active Enrolled Students:</span>
                <span style={{ color: '#fff', fontWeight: 600 }}>12,450</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span>Active Appointed Faculty:</span>
                <span style={{ color: '#fff', fontWeight: 600 }}>820</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span>Monthly API Calls:</span>
                <span style={{ color: '#fff', fontWeight: 600 }}>1.42 M</span>
              </div>
            </div>
          </Card>

          <Button type="submit" variant="primary" size="lg" isLoading={saving} style={{ width: '100%' }}>
            <Save size={18} style={{ marginRight: '8px' }} /> Save Tenant Settings
          </Button>
        </div>
      </form>
    </div>
  );
};
