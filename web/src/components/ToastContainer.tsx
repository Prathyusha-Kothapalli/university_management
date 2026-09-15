import React from 'react';
import { useToast } from '../hooks/useToast';
import { CheckCircle2, AlertTriangle, Info, XCircle, X } from 'lucide-react';

export const ToastContainer: React.FC = () => {
  const { toasts, removeToast } = useToast();

  if (toasts.length === 0) return null;

  return (
    <div
      style={{
        position: 'fixed',
        bottom: '24px',
        right: '24px',
        zIndex: 9999,
        display: 'flex',
        flexDirection: 'column',
        gap: '10px',
        maxWidth: '380px',
      }}
    >
      {toasts.map((toast) => {
        const getBgColor = () => {
          switch (toast.type) {
            case 'success':
              return 'linear-gradient(135deg, rgba(16, 185, 129, 0.95), rgba(5, 150, 105, 0.95))';
            case 'error':
              return 'linear-gradient(135deg, rgba(239, 68, 68, 0.95), rgba(220, 38, 38, 0.95))';
            case 'warning':
              return 'linear-gradient(135deg, rgba(245, 158, 11, 0.95), rgba(217, 119, 6, 0.95))';
            case 'info':
            default:
              return 'linear-gradient(135deg, rgba(37, 99, 235, 0.95), rgba(14, 165, 233, 0.95))';
          }
        };

        const getIcon = () => {
          switch (toast.type) {
            case 'success':
              return <CheckCircle2 size={18} />;
            case 'error':
              return <XCircle size={18} />;
            case 'warning':
              return <AlertTriangle size={18} />;
            case 'info':
            default:
              return <Info size={18} />;
          }
        };

        return (
          <div
            key={toast.id}
            style={{
              background: getBgColor(),
              color: '#ffffff',
              padding: '12px 16px',
              borderRadius: '10px',
              boxShadow: '0 10px 25px rgba(0,0,0,0.3)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              gap: '12px',
              fontSize: '0.875rem',
              fontWeight: 500,
              backdropFilter: 'blur(8px)',
              animation: 'slideIn 0.2s ease-out',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              {getIcon()}
              <span>{toast.message}</span>
            </div>
            <button
              onClick={() => removeToast(toast.id)}
              style={{
                background: 'transparent',
                border: 'none',
                color: '#ffffff',
                cursor: 'pointer',
                opacity: 0.8,
                padding: '2px',
                display: 'flex',
                alignItems: 'center',
              }}
            >
              <X size={14} />
            </button>
          </div>
        );
      })}
    </div>
  );
};
