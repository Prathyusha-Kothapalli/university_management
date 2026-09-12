import React from 'react';
import { CreditCard } from 'lucide-react';

export const FeeSummary: React.FC = () => {
  const history = [
    { date: '02 Aug 2026', amount: '₹25,000', description: 'Semester 5 Tuition Fee (Inst. 2)', status: 'Paid' },
    { date: '10 Jul 2026', amount: '₹20,000', description: 'Hostel & Dining Charges', status: 'Paid' },
    { date: '15 Jan 2026', amount: '₹21,500', description: 'Semester 4 Tuition Fee', status: 'Paid' },
  ];

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Fee Structure & Payment History
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Total Annual Fee: <strong style={{ color: '#f8fafc' }}>₹85,000</strong> | Paid: <strong style={{ color: '#34d399' }}>₹66,500</strong> | Outstanding: <strong style={{ color: '#f59e0b' }}>₹18,500</strong> (Due: 20 Sep 2026)
          </p>
        </div>
        <CreditCard size={20} color="#f59e0b" />
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.825rem' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#64748b', textAlign: 'left' }}>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Payment Date</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Description</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Amount</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {history.map((h, i) => (
              <tr key={i} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', color: '#e2e8f0' }}>
                <td style={{ padding: '10px 10px', color: '#94a3b8' }}>{h.date}</td>
                <td style={{ padding: '10px 10px', fontWeight: 600, color: '#f8fafc' }}>{h.description}</td>
                <td style={{ padding: '10px 10px', fontWeight: 700, color: '#34d399' }}>{h.amount}</td>
                <td style={{ padding: '10px 10px' }}>
                  <span
                    style={{
                      padding: '2px 8px',
                      borderRadius: '6px',
                      fontSize: '0.72rem',
                      fontWeight: 700,
                      backgroundColor: 'rgba(52, 211, 153, 0.15)',
                      color: '#34d399',
                    }}
                  >
                    {h.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
