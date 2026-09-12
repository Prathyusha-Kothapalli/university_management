import React from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { CreditCard, DollarSign, Award, FileText, CheckCircle2, Calendar } from 'lucide-react';

export const FinancialProfilePage: React.FC = () => {
  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Unified Student Financial Profile & Statement
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Overview of semester tuition fees, awarded scholarships, installment plans, and receipts.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1.25rem', marginBottom: '1.5rem' }}>
        <Card style={{ padding: '1.25rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Total Semester Tuition</span>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#fff', marginTop: '4px' }}>$12,500.00</div>
        </Card>
        <Card style={{ padding: '1.25rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Scholarship & Grants Deducted</span>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#10b981', marginTop: '4px' }}>-$6,000.00</div>
        </Card>
        <Card style={{ padding: '1.25rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Net Outstanding Balance</span>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#38bdf8', marginTop: '4px' }}>$6,500.00</div>
        </Card>
      </div>

      <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px' }}>
        <h3 style={{ color: '#f8fafc', marginTop: 0 }}>Active Installment Payment Schedule</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', padding: '10px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', fontSize: '0.85rem' }}>
            <span>Installment #1 (Due Sep 15, 2026)</span>
            <span style={{ color: '#10b981', fontWeight: 700 }}>$3,250.00 — PAID</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', padding: '10px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', fontSize: '0.85rem' }}>
            <span>Installment #2 (Due Nov 15, 2026)</span>
            <span style={{ color: '#38bdf8', fontWeight: 700 }}>$3,250.00 — PENDING</span>
          </div>
        </div>
      </Card>
    </div>
  );
};
