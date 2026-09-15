import React, { useState } from 'react';
import { CreditCard, ShieldCheck, X } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface ParentPaymentModalProps {
  isOpen: boolean;
  onClose: () => void;
  onPaymentSuccess?: (amount: number) => void;
}

export const ParentPaymentModal: React.FC<ParentPaymentModalProps> = ({
  isOpen,
  onClose,
  onPaymentSuccess,
}) => {
  const { showToast } = useToast();
  const [feeType, setFeeType] = useState('Tuition Fee (Inst. 3)');
  const [amount, setAmount] = useState('18500');
  const [paymentMethod, setPaymentMethod] = useState<'upi' | 'card' | 'netbanking'>('upi');
  const [isProcessing, setIsProcessing] = useState(false);

  if (!isOpen) return null;

  const handleProcessPayment = (e: React.FormEvent) => {
    e.preventDefault();
    setIsProcessing(true);
    showToast(`Processing payment of ₹${Number(amount).toLocaleString('en-IN')} via ${paymentMethod.toUpperCase()}...`, 'info');

    setTimeout(() => {
      setIsProcessing(false);
      showToast(`Payment of ₹${Number(amount).toLocaleString('en-IN')} successful! Receipt downloaded.`, 'success');
      if (onPaymentSuccess) {
        onPaymentSuccess(Number(amount));
      }
      onClose();
    }, 1200);
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(8px)',
        zIndex: 250,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '1rem',
      }}
    >
      <div
        style={{
          backgroundColor: '#0f172a',
          border: '1px solid rgba(56, 189, 248, 0.3)',
          borderRadius: '20px',
          padding: '1.75rem',
          maxWidth: '520px',
          width: '100%',
          boxShadow: '0 20px 60px rgba(0,0,0,0.6)',
          position: 'relative',
        }}
      >
        <button
          onClick={onClose}
          style={{
            position: 'absolute',
            right: '16px',
            top: '16px',
            backgroundColor: 'transparent',
            border: 'none',
            color: '#94a3b8',
            cursor: 'pointer',
          }}
        >
          <X size={20} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
          <div style={{ width: '40px', height: '40px', borderRadius: '10px', backgroundColor: 'rgba(56, 189, 248, 0.15)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <CreditCard size={20} color="#38bdf8" />
          </div>
          <div>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
              Online University Fee Gateway
            </h3>
            <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
              Secure Encrypted Payment Gateway for Rahul Kumar (STU-2026-001)
            </p>
          </div>
        </div>

        <form onSubmit={handleProcessPayment} style={{ display: 'flex', flexDirection: 'column', gap: '14px', marginTop: '1rem' }}>
          <div>
            <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Select Fee Category</label>
            <select
              value={feeType}
              onChange={(e) => {
                setFeeType(e.target.value);
                if (e.target.value.includes('Library')) setAmount('150');
                else setAmount('18500');
              }}
              style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.825rem' }}
            >
              <option value="Tuition Fee (Inst. 3)">Semester 5 Tuition Fee (Inst. 3) - ₹18,500</option>
              <option value="Library Overdue Fine">Library Overdue Fine - ₹150</option>
              <option value="Hostel & Dining Dues">Hostel & Dining Charges - ₹5,000</option>
            </select>
          </div>

          <div>
            <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Amount to Pay (₹)</label>
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.875rem', fontWeight: 700 }}
            />
          </div>

          <div>
            <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '6px' }}>Payment Method</label>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '8px' }}>
              <button
                type="button"
                onClick={() => setPaymentMethod('upi')}
                style={{
                  backgroundColor: paymentMethod === 'upi' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                  border: paymentMethod === 'upi' ? '1px solid rgba(56, 189, 248, 0.5)' : '1px solid rgba(255, 255, 255, 0.1)',
                  color: paymentMethod === 'upi' ? '#38bdf8' : '#94a3b8',
                  borderRadius: '8px',
                  padding: '8px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                UPI / GPay
              </button>
              <button
                type="button"
                onClick={() => setPaymentMethod('card')}
                style={{
                  backgroundColor: paymentMethod === 'card' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                  border: paymentMethod === 'card' ? '1px solid rgba(56, 189, 248, 0.5)' : '1px solid rgba(255, 255, 255, 0.1)',
                  color: paymentMethod === 'card' ? '#38bdf8' : '#94a3b8',
                  borderRadius: '8px',
                  padding: '8px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Debit/Credit Card
              </button>
              <button
                type="button"
                onClick={() => setPaymentMethod('netbanking')}
                style={{
                  backgroundColor: paymentMethod === 'netbanking' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                  border: paymentMethod === 'netbanking' ? '1px solid rgba(56, 189, 248, 0.5)' : '1px solid rgba(255, 255, 255, 0.1)',
                  color: paymentMethod === 'netbanking' ? '#38bdf8' : '#94a3b8',
                  borderRadius: '8px',
                  padding: '8px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Net Banking
              </button>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.72rem', color: '#34d399', backgroundColor: 'rgba(52, 211, 153, 0.1)', padding: '8px 10px', borderRadius: '8px' }}>
            <ShieldCheck size={14} /> 256-Bit SSL Encrypted University Financial Transaction
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
            <button
              type="button"
              onClick={onClose}
              style={{ backgroundColor: 'rgba(255, 255, 255, 0.05)', border: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8', borderRadius: '8px', padding: '8px 14px', fontSize: '0.825rem', cursor: 'pointer' }}
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isProcessing}
              style={{ backgroundColor: '#2563eb', border: 'none', color: '#ffffff', borderRadius: '8px', padding: '8px 18px', fontSize: '0.85rem', fontWeight: 700, cursor: 'pointer', boxShadow: '0 4px 14px rgba(37, 99, 235, 0.4)' }}
            >
              {isProcessing ? 'Processing Payment...' : `Pay ₹${Number(amount).toLocaleString('en-IN')} Now`}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
