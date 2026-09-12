import React, { useState, useEffect } from 'react';
import { User, Announcement } from '../types/auth';
import { getStoredAnnouncements, deleteAnnouncement } from '../services/announcementStore';
import { PostAnnouncementModal } from '../components/PostAnnouncementModal';

interface AnnouncementsPageProps {
  user: User | null;
}

export const AnnouncementsPage: React.FC<AnnouncementsPageProps> = ({ user }) => {
  const [announcements, setAnnouncements] = useState<Announcement[]>(() => getStoredAnnouncements());
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [modalOpen, setModalOpen] = useState(false);

  const isFaculty = user?.role === 'faculty';

  const reloadAnnouncements = () => {
    setAnnouncements(getStoredAnnouncements());
  };

  useEffect(() => {
    const handleUpdate = () => reloadAnnouncements();
    window.addEventListener('unisphere_announcements_updated', handleUpdate);
    return () => window.removeEventListener('unisphere_announcements_updated', handleUpdate);
  }, []);

  const categories = ['All', 'Academic', 'Placement', 'Exam', 'Campus', 'Faculty'];

  const filtered = announcements.filter((ann) => {
    // Role filter: if student, exclude faculty-only announcements
    if (user?.role === 'student' && ann.targetRole === 'faculty') {
      return false;
    }
    // Category filter
    if (selectedCategory !== 'All' && ann.category !== selectedCategory) {
      return false;
    }
    // Search query filter
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      return ann.title.toLowerCase().includes(q) || ann.content.toLowerCase().includes(q);
    }
    return true;
  });

  const getCategoryColor = (cat: Announcement['category']) => {
    switch (cat) {
      case 'Placement':
        return { bg: 'rgba(16, 185, 129, 0.15)', text: '#34d399', border: 'rgba(16, 185, 129, 0.3)' };
      case 'Exam':
        return { bg: 'rgba(245, 158, 11, 0.15)', text: '#fbbf24', border: 'rgba(245, 158, 11, 0.3)' };
      case 'Faculty':
        return { bg: 'rgba(139, 92, 246, 0.15)', text: '#c084fc', border: 'rgba(139, 92, 246, 0.3)' };
      case 'Campus':
        return { bg: 'rgba(236, 72, 153, 0.15)', text: '#f472b6', border: 'rgba(236, 72, 153, 0.3)' };
      default:
        return { bg: 'rgba(14, 165, 233, 0.15)', text: '#38bdf8', border: 'rgba(14, 165, 233, 0.3)' };
    }
  };

  const handleDelete = (id: string) => {
    if (window.confirm('Delete this announcement?')) {
      deleteAnnouncement(id);
      reloadAnnouncements();
    }
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      {/* Header with Title and Faculty Post Button */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '2rem',
      }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span style={{ fontSize: '2rem' }}>📢</span>
            <h1 style={{ fontSize: '2rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
              Campus Announcements & Bulletins
            </h1>
          </div>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem', marginTop: '6px' }}>
            Official notices, academic memos, placement drives, and campus alerts for {user?.role === 'faculty' ? 'Faculty & Staff' : 'Students'}
          </p>
        </div>

        {isFaculty && (
          <button
            onClick={() => setModalOpen(true)}
            className="btn btn-primary"
            style={{
              padding: '10px 20px',
              fontSize: '0.925rem',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              boxShadow: '0 4px 14px rgba(37, 99, 235, 0.4)',
            }}
          >
            <span>➕</span>
            <span>Post New Announcement</span>
          </button>
        )}
      </div>

      {/* Filter and Search Bar */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '1.75rem',
      }}>
        {/* Categories */}
        <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '4px' }}>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              style={{
                padding: '7px 16px',
                borderRadius: '10px',
                border: selectedCategory === cat ? '1.5px solid #38bdf8' : '1px solid var(--color-border)',
                backgroundColor: selectedCategory === cat ? 'rgba(56, 189, 248, 0.2)' : 'rgba(28, 37, 65, 0.6)',
                color: selectedCategory === cat ? '#38bdf8' : '#94a3b8',
                fontWeight: 700,
                fontSize: '0.85rem',
                cursor: 'pointer',
                transition: 'all 0.2s',
              }}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Search input */}
        <div style={{ position: 'relative', minWidth: '260px' }}>
          <input
            type="text"
            className="form-input"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="🔍 Search announcements..."
            style={{ padding: '8px 14px', fontSize: '0.875rem' }}
          />
        </div>
      </div>

      {/* Announcements List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {filtered.length > 0 ? (
          filtered.map((ann) => {
            const style = getCategoryColor(ann.category);
            return (
              <div
                key={ann.id}
                className="glass-panel"
                style={{
                  padding: '1.5rem',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '8px',
                  position: 'relative',
                  borderLeft: `4px solid ${style.text}`,
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{
                      padding: '3px 10px',
                      borderRadius: '8px',
                      backgroundColor: style.bg,
                      color: style.text,
                      border: `1px solid ${style.border}`,
                      fontSize: '0.75rem',
                      fontWeight: 700,
                      textTransform: 'uppercase',
                      letterSpacing: '0.5px',
                    }}>
                      {ann.category}
                    </span>

                    {ann.targetRole === 'faculty' && (
                      <span style={{
                        padding: '3px 8px',
                        borderRadius: '8px',
                        backgroundColor: 'rgba(139, 92, 246, 0.2)',
                        color: '#c084fc',
                        fontSize: '0.72rem',
                        fontWeight: 700,
                      }}>
                        🔒 Faculty Restricted
                      </span>
                    )}

                    <span style={{ fontSize: '0.8rem', color: '#64748b' }}>
                      📅 {ann.date}
                    </span>
                  </div>

                  {isFaculty && (
                    <button
                      onClick={() => handleDelete(ann.id)}
                      style={{
                        background: 'none',
                        border: 'none',
                        color: '#ef4444',
                        cursor: 'pointer',
                        fontSize: '0.85rem',
                        opacity: 0.7,
                      }}
                      title="Delete this notice"
                    >
                      🗑️ Remove
                    </button>
                  )}
                </div>

                <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', marginTop: '2px' }}>
                  {ann.title}
                </h3>

                <p style={{ fontSize: '0.9rem', color: '#cbd5e1', lineHeight: '1.55' }}>
                  {ann.content}
                </p>

                {ann.author && (
                  <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '6px' }}>
                    Issued by: <strong style={{ color: '#e2e8f0' }}>{ann.author}</strong>
                  </div>
                )}
              </div>
            );
          })
        ) : (
          <div className="glass-panel" style={{ padding: '3.5rem', textAlign: 'center', color: '#94a3b8' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '8px' }}>📭</div>
            <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#f8fafc' }}>
              No Announcements Found
            </div>
            <p style={{ fontSize: '0.85rem', marginTop: '4px' }}>
              {searchQuery ? 'Try clearing your search query.' : 'There are no active notices matching this category.'}
            </p>
          </div>
        )}
      </div>

      {/* Post Announcement Modal for Faculty */}
      {isFaculty && (
        <PostAnnouncementModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onAnnouncementCreated={reloadAnnouncements}
          authorName={user?.name || 'Prof. Arthur Vance'}
        />
      )}
    </div>
  );
};
