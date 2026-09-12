import React, { useState } from 'react';
import { FeeSummary } from '../../components/dashboard/FeeSummary';
import { ParentPaymentModal } from '../../components/dashboard/ParentPaymentModal';
import { CreditCard, Download } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const ParentFinanceView: React.FC = () => {
  const { showToast } = useToast();
  const [isPaymentModalOpen, setIsPaymentModalOpen] = useState(false);

  const handleDownloadReceipt = () => {
    showToast('Downloading latest fee payment receipt (PDF)...', 'info');
  };

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Fee Structures, Dues & Payment Gateway
          </h1>
          <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
            Official university tuition fees, hostel charges, payment history, and receipt downloads
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <button
            onClick={handleDownloadReceipt}
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.05)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              color: '#e2e8f0',
              borderRadius: '10px',
              padding: '8px 14px',
              fontSize: '0.825rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
            }}
          >
            <Download size={15} /> Download Receipt
          </button>
          <button
            onClick={() => setIsPaymentModalOpen(true)}
            style={{
              backgroundColor: '#2563eb',
              border: 'none',
              color: '#ffffff',
              borderRadius: '10px',
              padding: '8px 16px',
              fontSize: '0.85rem',
              fontWeight: 700,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              boxShadow: '0 4px 14px rgba(37, 99, 235, 0.4)',
            }}
          >
            <CreditCard size={15} /> Pay Dues Now
          </button>
        </div>
      </div>

      <FeeSummary />

      <ParentPaymentModal
        isOpen={isPaymentModalOpen}
        onClose={() => setIsPaymentModalOpen(false)}
      />
    </div>
  );
};
