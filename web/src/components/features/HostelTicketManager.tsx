import React, { useState } from 'react';
import { Plus } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const HostelTicketManager: React.FC = () => {
  const { showToast } = useToast();
  const [tickets, setTickets] = useState([
    { id: 'TKT-101', issue: 'Wi-Fi Router Signal Weak in Room B-204', category: 'IT/Wi-Fi', status: 'In Progress' },
    { id: 'TKT-102', issue: 'Bathroom Plumbing Leak Inspection', category: 'Plumbing', status: 'Resolved' },
  ]);

  const handleNewTicket = () => {
    const newTkt = {
      id: `TKT-10${tickets.length + 1}`,
      issue: 'Air Conditioner Filter Cleaning Request',
      category: 'HVAC',
      status: 'Submitted',
    };
    setTickets([newTkt, ...tickets]);
    showToast('Submitted hostel maintenance ticket to Estate Office', 'success');
  };

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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Hostel Maintenance & Room Service Tickets
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Sunrise Hostel Room B-204 Helpdesk Requests
          </p>
        </div>

        <button
          onClick={handleNewTicket}
          style={{
            backgroundColor: 'rgba(56, 189, 248, 0.15)',
            border: '1px solid rgba(56, 189, 248, 0.3)',
            color: '#38bdf8',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.78rem',
            fontWeight: 700,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Plus size={14} /> New Ticket
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {tickets.map((t) => (
          <div
            key={t.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{t.issue}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
                Ticket ID: {t.id} • Category: {t.category}
              </div>
            </div>
            <span
              style={{
                backgroundColor: t.status === 'Resolved' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                color: t.status === 'Resolved' ? '#34d399' : '#f59e0b',
                fontSize: '0.72rem',
                fontWeight: 700,
                padding: '2px 8px',
                borderRadius: '6px',
              }}
            >
              {t.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
