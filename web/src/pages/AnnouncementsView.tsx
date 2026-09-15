import React, { useState, useEffect } from 'react';
import { User, Announcement } from '../types/auth';
import { getStoredAnnouncements } from '../services/announcementStore';
import { PostAnnouncementModal } from '../components/PostAnnouncementModal';

interface AnnouncementsViewProps {
  user: User | null;
}

export const AnnouncementsView: React.FC<AnnouncementsViewProps> = ({ user }) => {
  const [announcements, setAnnouncements] = useState<Announcement[]>(() => getStoredAnnouncements());
  const [filter, setFilter] = useState('All');
  const [modalOpen, setModalOpen] = useState(false);

  const isFaculty = user?.role === 'faculty';

  const reload = () => {
    setAnnouncements(getStoredAnnouncements());
  };

  useEffect(() => {
    const handleUpdate = () => reload();
    window.addEventListener('unisphere_announcements_updated', handleUpdate);
    return () => window.removeEventListener('unisphere_announcements_updated', handleUpdate);
  }, []);

  const categories = ['All', 'Placement', 'Exam', 'Academic', 'Campus'];

  const filtered = announcements.filter((ann) => {
    if (user?.role === 'student' && ann.targetRole === 'faculty') return false;
    if (filter !== 'All' && ann.category !== filter) return false;
    return true;
  });

  return (
    <div style={{ padding: '1.25rem' }}>
      {/* Header with Post button for faculty */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
        <div>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 800, color: '#f8fafc' }}>
            Campus Bulletins
          </h3>
          <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>
            Official notices & updates
          </span>
        </div>

        {isFaculty && (
          <button
            onClick={() => setModalOpen(true)}
            className="btn btn-primary"
            style={{ padding: '4px 10px', fontSize: '0.75rem', borderRadius: '8px' }}
          >
            ➕ Post Notice
          </button>
        )}
      </div>

      {/* Categories chips */}
      <div style={{ display: 'flex', gap: '6px', overflowX: 'auto', paddingBottom: '8px', marginBottom: '12px' }}>
        {categories.map((c) => (
          <button
            key={c}
            onClick={() => setFilter(c)}
            style={{
              padding: '4px 12px',
              borderRadius: '8px',
              border: filter === c ? '1.5px solid #38bdf8' : '1px solid var(--color-border)',
              backgroundColor: filter === c ? 'rgba(56, 189, 248, 0.2)' : 'rgba(28, 37, 65, 0.6)',
              color: filter === c ? '#38bdf8' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.72rem',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            {c}
          </button>
        ))}
      </div>

      {/* Notices Feed */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {filtered.map((ann) => (
          <div key={ann.id} className="glass-panel" style={{ padding: '1rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
              <span style={{
                fontSize: '0.68rem',
                fontWeight: 700,
                color: ann.category === 'Placement' ? '#34d399' : ann.category === 'Exam' ? '#fbbf24' : '#38bdf8',
                background: 'rgba(255, 255, 255, 0.08)',
                padding: '2px 6px',
                borderRadius: '4px',
                textTransform: 'uppercase',
              }}>
                {ann.category}
              </span>
              <span style={{ fontSize: '0.7rem', color: '#64748b' }}>
                📅 {ann.date}
              </span>
            </div>

            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: '#f8fafc', marginTop: '2px' }}>
              {ann.title}
            </div>

            <p style={{ fontSize: '0.78rem', color: '#cbd5e1', marginTop: '4px', lineHeight: 1.4 }}>
              {ann.content}
            </p>

            {ann.author && (
              <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '6px' }}>
                By: {ann.author}
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Post Modal for Faculty */}
      {isFaculty && (
        <PostAnnouncementModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onAnnouncementCreated={reload}
          authorName={user?.name || 'Prof. Arthur Vance'}
        />
      )}
    </div>
  );
};
