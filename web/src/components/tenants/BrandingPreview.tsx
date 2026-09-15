import React from 'react';
import { Palette, Globe, Mail } from 'lucide-react';

interface BrandingPreviewProps {
  primaryColor: string;
  secondaryColor: string;
  accentColor: string;
  portalTitle: string;
  customDomain?: string;
  supportEmail?: string;
}

export const BrandingPreview: React.FC<BrandingPreviewProps> = ({
  primaryColor,
  secondaryColor,
  accentColor,
  portalTitle,
  customDomain,
  supportEmail,
}) => {
  return (
    <div
      style={{
        backgroundColor: 'rgba(15, 23, 42, 0.7)',
        border: '1px solid rgba(255, 255, 255, 0.12)',
        borderRadius: '16px',
        padding: '1.5rem',
        boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '1rem', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '0.75rem' }}>
        <Palette size={20} color={accentColor} />
        <h4 style={{ margin: 0, fontSize: '1rem', fontWeight: 700, color: '#f8fafc' }}>
          Live Tenant Branding Preview
        </h4>
      </div>

      <div
        style={{
          borderRadius: '12px',
          overflow: 'hidden',
          border: '1px solid rgba(255, 255, 255, 0.1)',
          backgroundColor: '#090d16',
        }}
      >
        {/* Header bar preview */}
        <div
          style={{
            backgroundColor: primaryColor,
            padding: '12px 18px',
            display: 'flex',
            justify: 'space-between',
            alignItems: 'center',
            color: '#ffffff',
          }}
        >
          <div style={{ fontWeight: 800, fontSize: '1.1rem', letterSpacing: '0.5px' }}>
            {portalTitle || 'University Portal'}
          </div>
          <div style={{ fontSize: '0.75rem', opacity: 0.8, backgroundColor: 'rgba(255,255,255,0.2)', padding: '2px 8px', borderRadius: '6px' }}>
            Tenant Mode
          </div>
        </div>

        {/* Hero banner preview */}
        <div
          style={{
            background: `linear-gradient(135deg, ${primaryColor} 0%, ${secondaryColor} 100%)`,
            padding: '1.5rem',
            color: '#ffffff',
          }}
        >
          <h3 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 700 }}>
            Welcome to {portalTitle}
          </h3>
          <p style={{ margin: '4px 0 12px 0', fontSize: '0.8rem', opacity: 0.9 }}>
            Multi-Tenant Campus Infrastructure System
          </p>
          <button
            style={{
              backgroundColor: accentColor,
              border: 'none',
              borderRadius: '8px',
              padding: '6px 14px',
              color: '#ffffff',
              fontWeight: 600,
              fontSize: '0.8rem',
              cursor: 'pointer',
            }}
          >
            Explore Dashboard
          </button>
        </div>

        <div style={{ padding: '1rem', fontSize: '0.8rem', color: '#94a3b8', display: 'flex', flexDirection: 'column', gap: '6px' }}>
          {customDomain && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Globe size={14} color="#38bdf8" />
              <span>Custom Domain: <strong style={{ color: '#f1f5f9' }}>{customDomain}</strong></span>
            </div>
          )}
          {supportEmail && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Mail size={14} color="#10b981" />
              <span>Support Contact: <strong style={{ color: '#f1f5f9' }}>{supportEmail}</strong></span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
