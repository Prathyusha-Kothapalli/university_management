import React from 'react';
import { ToggleLeft, ToggleRight, Info } from 'lucide-react';

export interface FeatureFlagItem {
  feature_key: string;
  is_enabled: boolean;
  description?: string;
}

interface FeatureFlagToggleTableProps {
  flags: FeatureFlagItem[];
  onToggle: (key: string, currentStatus: boolean) => void;
}

export const FeatureFlagToggleTable: React.FC<FeatureFlagToggleTableProps> = ({ flags, onToggle }) => {
  return (
    <div
      style={{
        backgroundColor: 'rgba(15, 23, 42, 0.6)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: '16px',
        overflow: 'hidden',
      }}
    >
      <div style={{ padding: '1.25rem', borderBottom: '1px solid rgba(255, 255, 255, 0.08)' }}>
        <h4 style={{ margin: 0, fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc' }}>
          Tenant Modular Feature Activation Flags
        </h4>
        <p style={{ margin: '4px 0 0 0', fontSize: '0.8rem', color: '#94a3b8' }}>
          Enable or disable specific campus modules dynamically for this university tenant.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column' }}>
        {flags.map((flag) => (
          <div
            key={flag.feature_key}
            style={{
              padding: '12px 18px',
              borderBottom: '1px solid rgba(255, 255, 255, 0.05)',
              display: 'flex',
              justify: 'space-between',
              alignItems: 'center',
            }}
          >
            <div>
              <div style={{ fontWeight: 600, fontSize: '0.9rem', color: '#f1f5f9', fontFamily: 'monospace' }}>
                {flag.feature_key}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', display: 'flex', alignItems: 'center', gap: '4px', marginTop: '2px' }}>
                <Info size={12} /> {flag.description || 'System feature flag'}
              </div>
            </div>

            <button
              onClick={() => onToggle(flag.feature_key, flag.is_enabled)}
              style={{
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                color: flag.is_enabled ? '#10b981' : '#64748b',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                fontSize: '0.85rem',
                fontWeight: 600,
              }}
            >
              {flag.is_enabled ? (
                <>
                  <ToggleRight size={28} />
                  <span style={{ color: '#10b981' }}>Active</span>
                </>
              ) : (
                <>
                  <ToggleLeft size={28} />
                  <span style={{ color: '#64748b' }}>Disabled</span>
                </>
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
