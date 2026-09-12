import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useFetch } from '../../hooks/useFetch';
import { documentsApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { Document } from '../../types';
import { Upload, Download, ShieldCheck, Key, Smartphone, CreditCard, QrCode, CheckCircle, HeartPulse, Laptop, Shield } from 'lucide-react';

export const ProfilePage: React.FC = () => {
  const { user, updateUser } = useAuth();
  const { showToast } = useToast();

  const [fullName, setFullName] = useState(user?.full_name || user?.name || '');
  const [email, setEmail] = useState(user?.email || '');

  // Features State
  const [isMedicalModalOpen, setIsMedicalModalOpen] = useState(false);
  const [isSessionsModalOpen, setIsSessionsModalOpen] = useState(false);
  const [isBlockchainModalOpen, setIsBlockchainModalOpen] = useState(false);

  // Feature 10: Security Modal State
  const [isSecurityModalOpen, setIsSecurityModalOpen] = useState(false);
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [is2FAEnabled, setIs2FAEnabled] = useState(true);

  // Feature 20: Digital Campus ID Card Generator State
  const [isIdCardModalOpen, setIsIdCardModalOpen] = useState(false);

  const { data: documents = [] } = useFetch(documentsApi.getDocuments);

  const handleSaveProfile = (e: React.FormEvent) => {
    e.preventDefault();
    updateUser({ full_name: fullName, name: fullName, email });
    showToast('Profile information updated successfully!', 'success');
  };

  const handleChangePassword = (e: React.FormEvent) => {
    e.preventDefault();
    showToast('Security password updated successfully!', 'success');
    setIsSecurityModalOpen(false);
    setCurrentPassword('');
    setNewPassword('');
  };

  const documentColumns: Column<Document>[] = [
    { header: 'Title', accessorKey: 'title', cell: (r) => <strong>{r.title}</strong> },
    { header: 'Type', accessorKey: 'document_type', cell: (r) => <span style={{ color: '#38bdf8' }}>{r.document_type}</span> },
    { header: 'Uploaded Date', accessorKey: 'uploaded_at' },
    { header: 'Action', cell: () => <Button variant="outline" size="sm" icon={<Download size={14} />}>Download</Button> },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            User Profile & Document Vault
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 1 & Group 11 APIs (`/api/v1/users/{'{id}'}`, `/api/v1/documents/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="outline" icon={<Shield size={16} />} onClick={() => setIsBlockchainModalOpen(true)}>
            Blockchain Credential Hash
          </Button>
          <Button variant="outline" icon={<HeartPulse size={16} />} onClick={() => setIsMedicalModalOpen(true)}>
            Emergency Contact
          </Button>
          <Button variant="outline" icon={<Laptop size={16} />} onClick={() => setIsSessionsModalOpen(true)}>
            Active Sessions
          </Button>
          <Button variant="outline" icon={<CreditCard size={16} />} onClick={() => setIsIdCardModalOpen(true)}>
            Digital ID Pass
          </Button>
          <Button variant="secondary" icon={<ShieldCheck size={16} />} onClick={() => setIsSecurityModalOpen(true)}>
            Security Settings
          </Button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '1.5rem' }}>
        {/* User Card */}
        <Card title="Account Information">
          <form onSubmit={handleSaveProfile} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ textAlign: 'center', margin: '0.5rem 0' }}>
              <div
                style={{
                  width: '72px',
                  height: '72px',
                  borderRadius: '50%',
                  background: '#2563eb',
                  color: '#fff',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 800,
                  fontSize: '2rem',
                  margin: '0 auto 8px auto',
                }}
              >
                {fullName.charAt(0)}
              </div>
              <div style={{ fontSize: '0.8rem', color: '#38bdf8', fontWeight: 700 }}>
                {user?.studentId || 'FAC-2026-001'}
              </div>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Full Name</label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
              />
            </div>

            <Button type="submit" variant="primary" style={{ marginTop: '0.5rem' }}>
              Save Changes
            </Button>
          </form>
        </Card>

        {/* Document Vault */}
        <Card title="Document Vault" subtitle="Official university certificates, ID card, and receipts" action={<Button variant="outline" size="sm" icon={<Upload size={14} />}>Upload Document</Button>}>
          <DataTable columns={documentColumns} data={documents || []} searchPlaceholder="Search documents..." />
        </Card>
      </div>

      {/* Feature 10: Security Modal */}
      <Modal isOpen={isSecurityModalOpen} onClose={() => setIsSecurityModalOpen(false)} title="Account Security & Password Settings">
        <form onSubmit={handleChangePassword} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Current Password</label>
            <input
              type="password"
              required
              placeholder="••••••••"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>New Password</label>
            <input
              type="password"
              required
              placeholder="••••••••"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>

          <div style={{ padding: '0.75rem', background: 'rgba(16,185,129,0.1)', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.8rem', color: '#10b981' }}>
              <Smartphone size={16} /> Two-Factor Authentication (2FA)
            </div>
            <button
              type="button"
              onClick={() => {
                setIs2FAEnabled(!is2FAEnabled);
                showToast(`2FA status set to ${!is2FAEnabled ? 'Enabled' : 'Disabled'}`, 'info');
              }}
              style={{ padding: '4px 10px', background: is2FAEnabled ? '#10b981' : '#64748b', border: 'none', borderRadius: '12px', color: '#fff', fontSize: '0.75rem', cursor: 'pointer', fontWeight: 700 }}
            >
              {is2FAEnabled ? 'ACTIVE' : 'OFF'}
            </button>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsSecurityModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit" icon={<Key size={16} />}>Update Password</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 20: Digital Campus ID Badge Generator Modal */}
      <Modal
        isOpen={isIdCardModalOpen}
        onClose={() => setIsIdCardModalOpen(false)}
        title="Official UniSphere AI Digital Campus Pass"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem', alignItems: 'center' }}>
          {/* Smart Card Visual Container */}
          <div
            style={{
              width: '100%',
              maxWidth: '380px',
              padding: '1.5rem',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #1e1b4b, #312e81, #1e293b)',
              border: '1px solid rgba(168,85,247,0.4)',
              boxShadow: '0 10px 25px rgba(0,0,0,0.5)',
              position: 'relative',
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
              gap: '1rem',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '8px' }}>
              <div>
                <div style={{ fontSize: '0.9rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '0.5px' }}>UNISPHERE UNIVERSITY</div>
                <div style={{ fontSize: '0.65rem', color: '#c084fc', textTransform: 'uppercase', letterSpacing: '1px' }}>OFFICIAL DIGITAL IDENTITY BADGE</div>
              </div>
              <div style={{ width: '28px', height: '28px', borderRadius: '6px', background: '#a855f7', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '0.75rem', fontWeight: 800 }}>
                US
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
              <div
                style={{
                  width: '64px',
                  height: '64px',
                  borderRadius: '12px',
                  background: '#2563eb',
                  color: '#fff',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 800,
                  fontSize: '1.8rem',
                  border: '2px solid rgba(255,255,255,0.2)',
                }}
              >
                {fullName.charAt(0)}
              </div>
              <div>
                <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#fff' }}>{fullName}</div>
                <div style={{ fontSize: '0.8rem', color: '#38bdf8', fontWeight: 700 }}>{user?.role ? user.role.toUpperCase() : 'STUDENT'}</div>
                <div style={{ fontSize: '0.7rem', color: '#cbd5e1', marginTop: '2px' }}>ID: {user?.studentId || 'STD-2026-8890'}</div>
                <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Dept: Computer Science & AI</div>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(0,0,0,0.3)', padding: '10px 14px', borderRadius: '10px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#10b981', fontSize: '0.75rem', fontWeight: 700 }}>
                <CheckCircle size={14} /> ACTIVE ENROLLMENT
              </div>
              <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Valid: 2024–2028</div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#c084fc', fontSize: '0.75rem' }}>
                <QrCode size={28} />
                <span style={{ fontSize: '0.65rem', color: '#94a3b8', lineHeight: 1.2 }}>Encrypted RFID & QR Pass</span>
              </div>
              <span style={{ fontSize: '0.65rem', fontFamily: 'monospace', color: '#64748b' }}>● ● ● 9842</span>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px', marginTop: '0.5rem' }}>
            <Button variant="outline" icon={<Download size={16} />} onClick={() => showToast('Downloaded Digital Campus Badge PDF!', 'success')}>
              Save High-Res Badge
            </Button>
            <Button variant="primary" onClick={() => setIsIdCardModalOpen(false)}>Done</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 19: Emergency Contact & Medical Record Modal */}
      <Modal
        isOpen={isMedicalModalOpen}
        onClose={() => setIsMedicalModalOpen(false)}
        title="Campus Health & Emergency Contact Record"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Primary Emergency Contact Phone</label>
            <input type="text" defaultValue="+1 (555) 234-5678 (Parent / Guardian)" style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Blood Group & Medical Conditions</label>
            <input type="text" defaultValue="O+ Positive • No Known Drug Allergies" style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
            <Button variant="ghost" onClick={() => setIsMedicalModalOpen(false)}>Cancel</Button>
            <Button variant="primary" onClick={() => { showToast('Saved Emergency Health Record!', 'success'); setIsMedicalModalOpen(false); }}>Save Medical Data</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 20: Active Sessions Manager Modal */}
      <Modal
        isOpen={isSessionsModalOpen}
        onClose={() => setIsSessionsModalOpen(false)}
        title="Connected Devices & Active Login Sessions"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(16,185,129,0.1)', border: '1px solid rgba(16,185,129,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#10b981', fontSize: '0.9rem' }}>Chrome Browser (Windows 11) — CURRENT SESSION</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>IP: 192.168.1.42 • Active Now</div>
            </div>
          </div>
          <Button variant="outline" style={{ marginTop: '0.5rem' }} onClick={() => { showToast('Logged out of all other remote browser sessions!', 'success'); setIsSessionsModalOpen(false); }}>
            Revoke All Other Sessions
          </Button>
        </div>
      </Modal>

      {/* Feature 52: Blockchain Credential Hash Verification Modal */}
      <Modal
        isOpen={isBlockchainModalOpen}
        onClose={() => setIsBlockchainModalOpen(false)}
        title="UniSphere Blockchain Credential Verification"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(56,189,248,0.1)', borderRadius: '10px', border: '1px solid rgba(56,189,248,0.3)', fontFamily: 'monospace', fontSize: '0.75rem', color: '#38bdf8', wordBreak: 'break-all' }}>
            SHA-256 Hash: 0x9f8a3b4c1d2e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.8rem', color: '#cbd5e1' }}>
            <span>Network: Ethereum Mainnet Anchor</span>
            <span style={{ color: '#10b981', fontWeight: 700 }}>VERIFIED IMMUTABLE 🟢</span>
          </div>
          <Button variant="primary" onClick={() => setIsBlockchainModalOpen(false)}>Done</Button>
        </div>
      </Modal>
    </div>
  );
};
