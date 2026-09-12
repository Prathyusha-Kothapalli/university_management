import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { GraduationCap, FileCheck, CheckCircle2, Upload, Send, Clock, Award } from 'lucide-react';

export const AdmissionPortalPage: React.FC = () => {
  const { showToast } = useToast();
  const [applicantName, setApplicantName] = useState('Taylor Swift');
  const [email, setEmail] = useState('taylor.applicant@gmail.com');
  const [phone, setPhone] = useState('+1 (555) 392-1049');
  const [gpa, setGpa] = useState('3.85');
  const [submitting, setSubmitting] = useState(false);
  const [submittedApp, setSubmittedApp] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/admissions/applications', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          applicant_name: applicantName,
          email,
          phone,
          program_id: '00000000-0000-0000-0000-000000000001',
          university_id: '00000000-0000-0000-0000-000000000001',
          gpa_score: parseFloat(gpa),
        }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Submission failed');

      setSubmittedApp(data.application);
      showToast('Admission application submitted successfully!', 'success');
    } catch (err: any) {
      showToast(err.message || 'Error submitting application', 'error');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1000px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          UniSphere Online Student Admission Portal
        </h1>
        <p style={{ color: '#94a3b8', margin: '6px 0 0 0', fontSize: '0.9rem' }}>
          Apply for undergraduate & graduate degree programs for Academic Year 2026-2027
        </p>
      </div>

      {!submittedApp ? (
        <Card style={{ padding: '2rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>Applicant Full Name</label>
                <input
                  type="text"
                  required
                  value={applicantName}
                  onChange={(e) => setApplicantName(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>Contact Email</label>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>Phone Number</label>
                <input
                  type="tel"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '6px' }}>High School / Prior GPA</label>
                <input
                  type="number"
                  step="0.01"
                  required
                  value={gpa}
                  onChange={(e) => setGpa(e.target.value)}
                  style={{ width: '100%', padding: '10px 12px', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
                />
              </div>
            </div>

            <Button type="submit" variant="primary" size="lg" isLoading={submitting} style={{ width: '100%', marginTop: '1rem' }}>
              <Send size={18} style={{ marginRight: '8px' }} /> Submit Admission Application
            </Button>
          </form>
        </Card>
      ) : (
        <Card style={{ padding: '2rem', textAlign: 'center', backgroundColor: 'rgba(16, 185, 129, 0.08)', border: '1px solid rgba(16, 185, 129, 0.3)' }}>
          <CheckCircle2 size={48} color="#10b981" style={{ margin: '0 auto 1rem auto' }} />
          <h2 style={{ color: '#10b981', margin: 0 }}>Application Successfully Submitted!</h2>
          <p style={{ color: '#cbd5e1', fontSize: '0.9rem', margin: '8px 0 1.5rem 0' }}>
            Application ID: <code>{submittedApp.id}</code> • Status: <strong>{submittedApp.status}</strong>
          </p>
          <Button onClick={() => setSubmittedApp(null)} variant="secondary">
            Submit Another Application
          </Button>
        </Card>
      )}
    </div>
  );
};
