import React, { useState } from 'react';
import { User } from '../types/auth';
import { mockStudentUser } from '../services/mockData';

interface ProfilePageProps {
  user?: User;
  onUpdateUser?: (updated: User) => void;
  onLogout?: () => void;
}

export const ProfilePage: React.FC<ProfilePageProps> = ({
  user = mockStudentUser,
  onUpdateUser = () => {},
  onLogout = () => {}
}) => {
  const [isEditing, setIsEditing] = useState(false);
  const [name, setName] = useState(user.name);
  const [phone, setPhone] = useState(user.phone || '');
  const [isConfirmingLogout, setIsConfirmingLogout] = useState(false);
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    onUpdateUser({
      ...user,
      name,
      phone,
    });
    setIsEditing(false);
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 3000);
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      {savedSuccess && (
        <div style={{
          padding: '12px 16px',
          backgroundColor: 'var(--color-success-bg)',
          color: '#34d399',
          border: '1px solid rgba(16, 185, 129, 0.3)',
          borderRadius: '12px',
          marginBottom: '1.5rem',
          fontWeight: 600,
          fontSize: '0.9rem',
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
        }}>
          <span>✅</span>
          <span>Profile changes saved successfully!</span>
        </div>
      )}

      {/* Profile Card Header */}
      <div className="glass-panel" style={{ padding: '2.5rem', textAlign: 'center', marginBottom: '1.5rem' }}>
        <div style={{
          width: '84px',
          height: '84px',
          borderRadius: '50%',
          background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
          margin: '0 auto 16px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '2.2rem',
          fontWeight: 800,
          color: '#ffffff',
          boxShadow: '0 8px 24px rgba(37, 99, 235, 0.45)',
        }}>
          {user.name.charAt(0)}
        </div>

        <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc' }}>
          {user.name}
        </h2>
        <p style={{ color: '#94a3b8', fontSize: '0.95rem', marginTop: '2px' }}>
          {user.email}
        </p>

        <div style={{ display: 'flex', justifyContent: 'center', gap: '8px', marginTop: '12px' }}>
          <span className={`badge ${user.role === 'student' ? 'badge-student' : 'badge-faculty'}`}>
            {user.role}
          </span>
          <span className="badge badge-success">
            Active Status
          </span>
        </div>

        <div style={{ marginTop: '1.75rem', display: 'flex', justifyContent: 'center', gap: '12px' }}>
          <button
            onClick={() => setIsEditing(true)}
            className="btn btn-primary"
            style={{ padding: '8px 22px' }}
          >
            ✏️ Edit Profile
          </button>
          <button
            onClick={() => setIsConfirmingLogout(true)}
            className="btn btn-danger"
            style={{ padding: '8px 22px' }}
          >
            Sign Out
          </button>
        </div>
      </div>

      {/* Details List */}
      <div className="glass-panel" style={{ padding: '1.5rem 2rem', marginBottom: '2rem' }}>
        <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', marginBottom: '1.25rem' }}>
          University Record Details
        </h3>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {[
            { label: 'University ID', value: user.studentId, icon: '🪪' },
            { label: 'Primary Contact Phone', value: user.phone || 'Not provided', icon: '📞' },
            { label: 'Department / Faculty', value: user.department, icon: '🏢' },
            { label: 'Academic Standing / Batch', value: user.enrolledYear || 'Class of 2028', icon: '🎓' },
            { label: 'Cumulative GPA', value: `${user.gpa.toFixed(2)} / 4.00`, icon: '📊' },
            { label: 'Attendance Rate', value: `${user.attendanceRate.toFixed(1)}%`, icon: '📈' },
          ].map((item, idx) => (
            <div key={idx} style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              paddingBottom: '12px',
              borderBottom: '1px solid rgba(255, 255, 255, 0.06)',
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{ fontSize: '1.2rem' }}>{item.icon}</span>
                <span style={{ fontSize: '0.9rem', color: '#94a3b8' }}>{item.label}</span>
              </div>
              <span style={{ fontSize: '0.95rem', fontWeight: 600, color: '#f8fafc' }}>
                {item.value}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Edit Profile Modal */}
      {isEditing && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 999,
          padding: '1rem',
        }}>
          <div className="glass-panel animate-fade-in" style={{
            maxWidth: '460px',
            width: '100%',
            padding: '2rem',
            backgroundColor: '#1c2541',
          }}>
            <h3 style={{ fontSize: '1.3rem', fontWeight: 800, color: '#f8fafc', marginBottom: '1.25rem' }}>
              Edit Profile Information
            </h3>

            <form onSubmit={handleSave}>
              <div className="form-group">
                <label className="form-label">Full Name</label>
                <input
                  type="text"
                  className="form-input"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label className="form-label">Phone Number</label>
                <input
                  type="tel"
                  className="form-input"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  required
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '1.5rem' }}>
                <button
                  type="button"
                  onClick={() => setIsEditing(false)}
                  className="btn btn-secondary"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn btn-primary"
                >
                  Save Changes
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Sign Out Confirmation Modal */}
      {isConfirmingLogout && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 999,
          padding: '1rem',
        }}>
          <div className="glass-panel animate-fade-in" style={{
            maxWidth: '400px',
            width: '100%',
            padding: '2rem',
            backgroundColor: '#1c2541',
            textAlign: 'center',
          }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '10px' }}>🚪</div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#f8fafc', marginBottom: '8px' }}>
              Confirm Sign Out
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginBottom: '1.5rem' }}>
              Are you sure you want to end your active session on UniSphere AI?
            </p>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '12px' }}>
              <button
                onClick={() => setIsConfirmingLogout(false)}
                className="btn btn-secondary"
              >
                Stay Logged In
              </button>
              <button
                onClick={onLogout}
                className="btn btn-danger"
              >
                Yes, Sign Out
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
