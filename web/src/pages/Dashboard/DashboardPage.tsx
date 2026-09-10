import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { useNavigate } from 'react-router-dom';
import {
  GraduationCap,
  Users,
  BookOpen,
  Calendar,
  Sparkles,
  ArrowUpRight,
  Clock,
  TrendingUp,
  Award,
  CheckCircle2,
  CreditCard,
  Ticket,
} from 'lucide-react';

import { HODDashboard } from './HODDashboard';
import { ParentDashboard } from './ParentDashboard';

export const DashboardPage: React.FC = () => {
  const { user, role } = useAuth();
  const { showToast } = useToast();
  const navigate = useNavigate();

  // Features State
  const [isEventModalOpen, setIsEventModalOpen] = useState(false);
  const [isQuickPayOpen, setIsQuickPayOpen] = useState(false);

  if (role === 'hod') {
    return <HODDashboard />;
  }

  if (role === 'parent') {
    return <ParentDashboard />;
  }

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      {/* Top Welcome Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(37, 99, 235, 0.25), rgba(14, 165, 233, 0.15))',
          border: '1px solid rgba(56, 189, 248, 0.25)',
          borderRadius: '18px',
          padding: '1.75rem 2rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          backdropFilter: 'blur(12px)',
        }}
      >
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
            <span style={{ fontSize: '0.75rem', fontWeight: 700, background: 'rgba(56, 189, 248, 0.2)', color: '#38bdf8', padding: '2px 8px', borderRadius: '12px', border: '1px solid rgba(56, 189, 248, 0.3)' }}>
              Spring Semester 2026
            </span>
            <span style={{ color: '#94a3b8', fontSize: '0.8rem' }}>• {user?.department || 'Computer Science'}</span>
          </div>
          <h1 style={{ margin: 0, fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc' }}>
            Welcome back, {user?.full_name || user?.name || 'Alex Morgan'} 👋
          </h1>
          <p style={{ margin: '6px 0 0 0', color: '#cbd5e1', fontSize: '0.9rem' }}>
            {role === 'student'
              ? 'You have 2 upcoming lectures today and 1 assignment due this week.'
              : role === 'faculty'
              ? 'You are instructing 2 course sections today. 14 assignment submissions pending review.'
              : 'System overview: 46 Database Tables synchronized, 1,240 active students, 98% service uptime.'}
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <Button variant="outline" icon={<Ticket size={16} />} onClick={() => setIsEventModalOpen(true)}>
            Campus Events & Hackathons
          </Button>
          <Button variant="secondary" icon={<CreditCard size={16} />} onClick={() => setIsQuickPayOpen(true)}>
            Quick Fee Gateway
          </Button>
          <Button variant="primary" icon={<Sparkles size={16} />} onClick={() => navigate('/ai')}>
            Ask AI Copilot
          </Button>
        </div>
      </div>

      {/* Feature 1: Graduation Eligibility & Credit Tracker Banner for Students */}
      {role === 'student' && (
        <Card title="Graduation Degree Progress Tracker" subtitle="Requirement progress for B.Tech Computer Science Degree">
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '1.5rem', alignItems: 'center' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '1rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '14px' }}>
              <div style={{ fontSize: '2.4rem', fontWeight: 800, color: '#38bdf8' }}>63.3%</div>
              <div style={{ fontSize: '0.8rem', color: '#cbd5e1', marginTop: '2px' }}>76 of 120 Total Credits Completed</div>
              <div style={{ width: '100%', backgroundColor: 'rgba(255,255,255,0.1)', height: '8px', borderRadius: '4px', marginTop: '12px', overflow: 'hidden' }}>
                <div style={{ width: '63.3%', height: '100%', background: 'linear-gradient(90deg, #2563eb, #38bdf8)', borderRadius: '4px' }} />
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.85rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#e2e8f0' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><CheckCircle2 size={14} style={{ color: '#10b981' }} /> Core Computer Science Courses</span>
                <strong>48 / 60 Credits</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#e2e8f0' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><CheckCircle2 size={14} style={{ color: '#10b981' }} /> Mathematics & Natural Sciences</span>
                <strong>18 / 20 Credits</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#e2e8f0' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><CheckCircle2 size={14} style={{ color: '#a855f7' }} /> AI & Data Science Electives</span>
                <strong>10 / 40 Credits (In Progress)</strong>
              </div>
            </div>
          </div>
        </Card>
      )}

      {/* KPI Stats Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.25rem' }}>
        {role === 'student' ? (
          <>
            <Card style={{ background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8))' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Cumulative GPA</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#38bdf8', marginTop: '4px' }}>3.84 / 4.0</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(56, 189, 248, 0.15)', color: '#38bdf8' }}>
                  <Award size={20} />
                </div>
              </div>
              <div style={{ fontSize: '0.75rem', color: '#10b981', marginTop: '8px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                <TrendingUp size={14} /> Top 5% of CSE Cohort
              </div>
            </Card>

            <Card style={{ background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8))' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Attendance Rate</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#10b981', marginTop: '4px' }}>94.5%</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(16, 185, 129, 0.15)', color: '#10b981' }}>
                  <Clock size={20} />
                </div>
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '8px' }}>
                18 of 19 Sessions Attended
              </div>
            </Card>

            <Card style={{ background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8))' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Credits Completed</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#a855f7', marginTop: '4px' }}>76 / 120</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(168, 85, 247, 0.15)', color: '#a855f7' }}>
                  <GraduationCap size={20} />
                </div>
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '8px' }}>
                Semester 6 (Senior Year)
              </div>
            </Card>
          </>
        ) : (
          <>
            <Card>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Total Enrolled Students</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#38bdf8', marginTop: '4px' }}>1,240</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(56, 189, 248, 0.15)', color: '#38bdf8' }}>
                  <Users size={20} />
                </div>
              </div>
            </Card>
            <Card>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Active Courses Offered</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#10b981', marginTop: '4px' }}>48</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(16, 185, 129, 0.15)', color: '#10b981' }}>
                  <BookOpen size={20} />
                </div>
              </div>
            </Card>
            <Card>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8', fontWeight: 600 }}>Hostel Occupancy</div>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f59e0b', marginTop: '4px' }}>88%</div>
                </div>
                <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(245, 158, 11, 0.15)', color: '#f59e0b' }}>
                  <Calendar size={20} />
                </div>
              </div>
            </Card>
          </>
        )}
      </div>

      {/* Main Section Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
        {/* Left Column: Quick Enrolled Courses / Schedule */}
        <Card title="Today's Academic Schedule" subtitle="Live classes & room locations">
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '12px 16px',
                backgroundColor: 'rgba(37, 99, 235, 0.12)',
                borderLeft: '4px solid #2563eb',
                borderRadius: '8px',
              }}
            >
              <div>
                <div style={{ fontWeight: 700, color: '#f8fafc', fontSize: '0.95rem' }}>
                  CS301: Advanced Machine Learning
                </div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginTop: '2px' }}>
                  09:00 AM - 10:30 AM • Alan Turing Hall (ATH-302)
                </div>
              </div>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, padding: '4px 10px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.2)', color: '#10b981' }}>
                Ongoing Now
              </span>
            </div>

            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '12px 16px',
                backgroundColor: 'rgba(255, 255, 255, 0.03)',
                borderLeft: '4px solid #0ea5e9',
                borderRadius: '8px',
              }}
            >
              <div>
                <div style={{ fontWeight: 700, color: '#f8fafc', fontSize: '0.95rem' }}>
                  CS402: Distributed Systems & Cloud
                </div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginTop: '2px' }}>
                  02:00 PM - 03:30 PM • Ada Lovelace Lab (ALB-105)
                </div>
              </div>
              <span style={{ fontSize: '0.75rem', fontWeight: 600, padding: '4px 10px', borderRadius: '12px', background: 'rgba(255, 255, 255, 0.06)', color: '#94a3b8' }}>
                Upcoming
              </span>
            </div>
          </div>
        </Card>

        {/* Right Column: Quick Links & Tools */}
        <Card title="Quick Domain Access" subtitle="Navigate system modules">
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {[
              { label: 'Courses & Curriculum', path: '/academics', color: '#38bdf8' },
              { label: 'Assignments & Notes', path: '/learning', color: '#10b981' },
              { label: 'Exam Schedules & Marks', path: '/exams', color: '#a855f7' },
              { label: 'Fee Payment & Receipt', path: '/finance', color: '#f59e0b' },
              { label: 'Library Catalog Search', path: '/library', color: '#ec4899' },
              { label: 'Hostel & Bus Allocations', path: '/facilities', color: '#6366f1' },
              { label: 'Placement Drives Directory', path: '/placements', color: '#14b8a6' },
            ].map((item, idx) => (
              <button
                key={idx}
                onClick={() => navigate(item.path)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  backgroundColor: 'rgba(255, 255, 255, 0.04)',
                  border: '1px solid rgba(255, 255, 255, 0.08)',
                  borderRadius: '10px',
                  color: '#e2e8f0',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  textAlign: 'left',
                  transition: 'all 0.15s ease',
                }}
              >
                <span>{item.label}</span>
                <ArrowUpRight size={16} style={{ color: item.color }} />
              </button>
            ))}
          </div>
        </Card>
      </div>

      {/* Feature 1: Campus Events RSVP Modal */}
      <Modal
        isOpen={isEventModalOpen}
        onClose={() => setIsEventModalOpen(false)}
        title="Upcoming Campus Tech Talks & Hackathons"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#38bdf8', fontSize: '0.9rem' }}>UniSphere AI Annual Hackathon 2026</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>March 24 • Innovation Hub Auditorium • 48-Hour Challenge</div>
            </div>
            <Button variant="primary" size="sm" onClick={() => showToast('Registered for UniSphere AI Hackathon!', 'success')}>
              Register
            </Button>
          </div>

          <div style={{ padding: '0.85rem 1rem', background: 'rgba(168,85,247,0.1)', border: '1px solid rgba(168,85,247,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#c084fc', fontSize: '0.9rem' }}>Keynote: Generative AI in Higher Education</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>March 18 • Turing Hall • Speaker: Dr. Elena Rostova</div>
            </div>
            <Button variant="outline" size="sm" onClick={() => showToast('RSVP confirmed for AI Keynote!', 'success')}>
              RSVP
            </Button>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <Button variant="primary" onClick={() => setIsEventModalOpen(false)}>Done</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 3: Quick Fee Gateway Modal */}
      <Modal
        isOpen={isQuickPayOpen}
        onClose={() => setIsQuickPayOpen(false)}
        title="Instant Fee Payment Gateway"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(16,185,129,0.1)', borderRadius: '10px', border: '1px solid rgba(16,185,129,0.3)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Spring Semester Balance</div>
              <strong style={{ fontSize: '1.4rem', color: '#10b981' }}>$1,800.00 USD</strong>
            </div>
            <span style={{ padding: '4px 10px', background: '#10b981', color: '#fff', borderRadius: '12px', fontSize: '0.75rem', fontWeight: 700 }}>
              DUE IN 12 DAYS
            </span>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <Button variant="primary" style={{ flex: 1 }} onClick={() => { showToast('Processing $1,800 instant card payment...', 'success'); setIsQuickPayOpen(false); }}>
              Pay via Credit Card
            </Button>
            <Button variant="outline" style={{ flex: 1 }} onClick={() => { showToast('Processing $1,800 UPI payment...', 'success'); setIsQuickPayOpen(false); }}>
              Pay via Instant UPI
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
