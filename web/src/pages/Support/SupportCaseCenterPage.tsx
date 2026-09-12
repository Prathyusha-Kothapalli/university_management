import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { MessageSquare, Ticket, Clock, CheckCircle, Plus, Send } from 'lucide-react';

export const SupportCaseCenterPage: React.FC = () => {
  const { showToast } = useToast();
  const [subject, setSubject] = useState('Course Registration Prerequisite Error');
  const [category, setCategory] = useState('ACADEMIC');
  const [description, setDescription] = useState('Unable to register for CS401 due to system prerequisite override flag.');
  const [submitting, setSubmitting] = useState(false);

  const [cases, setCases] = useState([
    { ticketNumber: 'TICK-2026-88A901', category: 'ACADEMIC', priority: 'HIGH', subject: 'Course Registration Prerequisite Error', status: 'IN_PROGRESS', date: '2026-09-10' },
  ]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/support-cases', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          student_id: '00000000-0000-0000-0000-000000000001',
          category,
          priority: 'MEDIUM',
          subject,
          description,
        }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Ticket creation failed');

      setCases([
        ...cases,
        {
          ticketNumber: data.ticket_number,
          category,
          priority: 'MEDIUM',
          subject,
          status: 'OPEN',
          date: new Date().toISOString().split('T')[0],
        },
      ]);
      showToast(`Support case ${data.ticket_number} created successfully!`, 'success');
    } catch (err: any) {
      showToast(err.message || 'Error creating ticket', 'error');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Student Support & Service Case Center
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Submit academic, IT, hostel, or bursar tickets with SLA tracking and live case chat.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <h3 style={{ color: '#f8fafc', marginTop: 0 }}>Create New Support Case</h3>
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Category</label>
              <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ width: '100%', padding: '8px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}>
                <option value="ACADEMIC" style={{ background: '#0f172a' }}>Academic Advising & Courses</option>
                <option value="FINANCIAL" style={{ background: '#0f172a' }}>Financial Aid & Fees</option>
                <option value="IT_SUPPORT" style={{ background: '#0f172a' }}>IT Portal & Account Access</option>
                <option value="HOSTEL" style={{ background: '#0f172a' }}>Hostel & Facilities</option>
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Subject</label>
              <input type="text" required value={subject} onChange={(e) => setSubject(e.target.value)} style={{ width: '100%', padding: '8px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Description</label>
              <textarea rows={4} required value={description} onChange={(e) => setDescription(e.target.value)} style={{ width: '100%', padding: '8px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
            </div>

            <Button type="submit" variant="primary" isLoading={submitting} style={{ width: '100%' }}>
              <Send size={16} style={{ marginRight: '6px' }} /> Dispatch Ticket
            </Button>
          </form>
        </Card>

        <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <h3 style={{ color: '#f8fafc', marginTop: 0 }}>My Open Support Tickets</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {cases.map((c, i) => (
              <div key={i} style={{ padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.06)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontWeight: 700, color: '#38bdf8', fontSize: '0.85rem' }}>{c.ticketNumber}</span>
                  <span style={{ padding: '2px 8px', borderRadius: '6px', background: 'rgba(37, 99, 235, 0.2)', color: '#38bdf8', fontSize: '0.75rem', fontWeight: 700 }}>
                    {c.status}
                  </span>
                </div>
                <h4 style={{ margin: '6px 0 2px 0', fontSize: '0.95rem', color: '#fff' }}>{c.subject}</h4>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Submitted on {c.date} • SLA: 24h</span>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
};
