import React from 'react';

export const App: React.FC = () => {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '100vh',
      padding: '2rem',
      backgroundColor: '#0f172a',
      color: '#f8fafc',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      <div style={{
        backgroundColor: '#1e293b',
        padding: '3rem',
        borderRadius: '1rem',
        boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.3)',
        maxWidth: '600px',
        textAlign: 'center',
        border: '1px solid #334155'
      }}>
        <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#38bdf8' }}>
          UniSphere AI
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#94a3b8', marginBottom: '1.5rem' }}>
          Multi-Tenant University Management Platform
        </p>
        <div style={{
          padding: '0.75rem 1.5rem',
          backgroundColor: '#0369a1',
          color: '#ffffff',
          borderRadius: '0.5rem',
          display: 'inline-block',
          fontWeight: 600,
          fontSize: '0.9rem'
        }}>
          Web Frontend Foundation Ready
        </div>
      </div>
    </div>
  );
};

export default App;
