import React, { ButtonHTMLAttributes } from 'react';

export type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'success' | 'outline' | 'ghost';
export type ButtonSize = 'sm' | 'md' | 'lg';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  isLoading?: boolean;
  icon?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  icon,
  className = '',
  disabled,
  style,
  ...props
}) => {
  const getVariantStyles = (): React.CSSProperties => {
    switch (variant) {
      case 'primary':
        return {
          background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
          color: '#ffffff',
          border: 'none',
          boxShadow: '0 4px 12px rgba(37, 99, 235, 0.3)',
        };
      case 'secondary':
        return {
          background: 'rgba(255, 255, 255, 0.08)',
          color: '#e2e8f0',
          border: '1px solid rgba(255, 255, 255, 0.12)',
        };
      case 'danger':
        return {
          background: 'linear-gradient(135deg, #ef4444, #dc2626)',
          color: '#ffffff',
          border: 'none',
          boxShadow: '0 4px 12px rgba(239, 68, 68, 0.3)',
        };
      case 'success':
        return {
          background: 'linear-gradient(135deg, #10b981, #059669)',
          color: '#ffffff',
          border: 'none',
          boxShadow: '0 4px 12px rgba(16, 185, 129, 0.3)',
        };
      case 'outline':
        return {
          background: 'transparent',
          color: '#38bdf8',
          border: '1px solid rgba(56, 189, 248, 0.4)',
        };
      case 'ghost':
        return {
          background: 'transparent',
          color: '#94a3b8',
          border: 'none',
        };
    }
  };

  const getSizeStyles = (): React.CSSProperties => {
    switch (size) {
      case 'sm':
        return { padding: '6px 12px', fontSize: '0.75rem', borderRadius: '6px' };
      case 'lg':
        return { padding: '12px 24px', fontSize: '1rem', borderRadius: '10px' };
      case 'md':
      default:
        return { padding: '8px 16px', fontSize: '0.875rem', borderRadius: '8px' };
    }
  };

  return (
    <button
      disabled={disabled || isLoading}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        fontWeight: 600,
        cursor: disabled || isLoading ? 'not-allowed' : 'pointer',
        opacity: disabled || isLoading ? 0.6 : 1,
        transition: 'all 0.15s ease-in-out',
        ...getVariantStyles(),
        ...getSizeStyles(),
        ...style,
      }}
      className={`unisphere-btn ${className}`}
      {...props}
    >
      {isLoading ? (
        <span style={{ display: 'inline-block', width: '14px', height: '14px', border: '2px solid currentColor', borderTopColor: 'transparent', borderRadius: '50%', animation: 'spin 0.8s linear infinite' }} />
      ) : (
        icon
      )}
      {children}
    </button>
  );
};
