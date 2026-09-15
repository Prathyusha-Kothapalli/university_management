import React, { useState } from 'react';
import { Settings, Shield, HardDrive, ToggleRight, Save, Check } from 'lucide-react';
import { StorageUsageChart } from '../../components/tenants/StorageUsageChart';
import { FeatureFlagToggleTable, FeatureFlagItem } from '../../components/tenants/FeatureFlagToggleTable';
import { Button } from '../../components/Button';

export const TenantSettingsPage: React.FC = () => {
  const [flags, setFlags] = useState<FeatureFlagItem[]>([
    { feature_key: 'ai_copilot', is_enabled: true, description: 'AI study copilot and natural-language query engine' },
    { feature_key: 'qr_attendance', is_enabled: true, description: 'Dynamic QR token classroom attendance tracking' },
    { feature_key: 'obe_curriculum', is_enabled: true, description: 'Outcome-Based Education (OBE) outcome mapping' },
    { feature_key: 'online_exams', is_enabled: true, description: 'Online proctored exam & paper generator engine' },
    { feature_key: 'placement_portal', is_enabled: true, description: 'Corporate placement drive & career recruitment hub' },
    { feature_key: 'hostel_management', is_enabled: false, description: 'Hostel room allocation & complaint ticket system' },
    { feature_key: 'transport_tracking', is_enabled: true, description: 'Transport route planning & GPS vehicle telemetry' },
  ]);

  const [saved, setSaved] = useState(false);

  const handleToggleFlag = (key: string, currentStatus: boolean) => {
    setFlags((prev) =>
      prev.map((f) => (f.feature_key === key ? { ...f, is_enabled: !currentStatus } : f))
    );
  };

  const handleSaveSettings = () => {
    setSaved(true);
    setTimeout(() => setSaved(false), 2500);
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1200px', margin: '0 auto', color: '#f8fafc' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.8rem', fontWeight: 800 }}>
            Tenant Configuration & Settings
          </h1>
          <p style={{ margin: '6px 0 0 0', color: '#94a3b8', fontSize: '0.9rem' }}>
            Manage storage quotas, activate modular feature flags, and configure security policies for this tenant.
          </p>
        </div>
        <Button variant="primary" onClick={handleSaveSettings} style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          {saved ? <Check size={16} /> : <Save size={16} />}
          {saved ? 'Settings Saved' : 'Save Tenant Settings'}
        </Button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', marginBottom: '2rem' }}>
        <StorageUsageChart
          usedBytes={28470000000} // ~28.47 GB
          quotaBytes={107374182400} // 100 GB
          documentCount={14250}
        />

        <div
          style={{
            backgroundColor: 'rgba(15, 23, 42, 0.6)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            borderRadius: '16px',
            padding: '1.5rem',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '1rem' }}>
            <Shield size={20} color="#38bdf8" />
            <h4 style={{ margin: 0, fontSize: '1.05rem', fontWeight: 700 }}>
              Tenant Security & Password Policy
            </h4>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', fontSize: '0.85rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span>Minimum Password Length</span>
              <input type="number" defaultValue={8} style={{ width: '70px', padding: '6px', borderRadius: '6px', backgroundColor: 'rgba(0,0,0,0.4)', border: '1px solid rgba(255,255,255,0.1)', color: '#ffffff', textAlign: 'center' }} />
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span>Max Failed Login Lockout Attempts</span>
              <input type="number" defaultValue={5} style={{ width: '70px', padding: '6px', borderRadius: '6px', backgroundColor: 'rgba(0,0,0,0.4)', border: '1px solid rgba(255,255,255,0.1)', color: '#ffffff', textAlign: 'center' }} />
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span>Session Idle Timeout (Minutes)</span>
              <input type="number" defaultValue={30} style={{ width: '70px', padding: '6px', borderRadius: '6px', backgroundColor: 'rgba(0,0,0,0.4)', border: '1px solid rgba(255,255,255,0.1)', color: '#ffffff', textAlign: 'center' }} />
            </div>
          </div>
        </div>
      </div>

      <FeatureFlagToggleTable flags={flags} onToggle={handleToggleFlag} />
    </div>
  );
};
