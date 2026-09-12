import React, { useEffect, useState } from 'react';

interface SplashScreenProps {
  onFinish: () => void;
}

export const SplashScreen: React.FC<SplashScreenProps> = ({ onFinish }) => {
  const [fade, setFade] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setFade(true);
      setTimeout(onFinish, 300);
    }, 1400);

    return () => clearTimeout(timer);
  }, [onFinish]);

  return (
    <div
      onClick={onFinish}
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: '#0b132b',
        backgroundImage: 'radial-gradient(circle at 50% 40%, rgba(37, 99, 235, 0.25) 0%, transparent 65%)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 99999,
        cursor: 'pointer',
        opacity: fade ? 0 : 1,
        transition: 'opacity 0.3s ease-out',
      }}
    >
      {/* Animated Glowing Logo */}
      <div
        style={{
          width: '90px',
          height: '90px',
          borderRadius: '26px',
          background: 'linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 0 45px rgba(37, 99, 235, 0.55)',
          animation: 'pulseGlow 2s infinite',
          marginBottom: '24px',
        }}
      >
        <span style={{ fontSize: '3rem', fontWeight: 900, color: '#ffffff', letterSpacing: '-1px' }}>
          U
        </span>
      </div>

      {/* App Branding */}
      <h1 style={{ fontSize: '2rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
        UniSphere <span style={{ color: '#38bdf8' }}>Mobile</span>
      </h1>
      <p style={{ fontSize: '0.9rem', color: '#94a3b8', marginTop: '6px', letterSpacing: '0.5px' }}>
        AI-Powered University Campus App
      </p>

      {/* Loading Indicator */}
      <div style={{ marginTop: '40px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '12px' }}>
        <div style={{
          width: '140px',
          height: '4px',
          backgroundColor: 'rgba(255, 255, 255, 0.1)',
          borderRadius: '4px',
          overflow: 'hidden',
        }}>
          <div style={{
            width: '60%',
            height: '100%',
            background: 'linear-gradient(90deg, #2563eb, #38bdf8)',
            borderRadius: '4px',
            animation: 'pulseGlow 1s infinite alternate',
          }} />
        </div>
        <span style={{ fontSize: '0.75rem', color: '#64748b' }}>
          Initializing offline cache & Python API...
        </span>
      </div>
    </div>
  );
};
