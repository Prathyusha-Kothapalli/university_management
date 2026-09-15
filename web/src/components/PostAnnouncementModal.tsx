import React, { useState } from 'react';
import { Announcement } from '../types/auth';
import { addAnnouncement } from '../services/announcementStore';

interface PostAnnouncementModalProps {
  isOpen: boolean;
  onClose: () => void;
  onAnnouncementCreated: () => void;
  authorName: string;
}

export const PostAnnouncementModal: React.FC<PostAnnouncementModalProps> = ({
  isOpen,
  onClose,
  onAnnouncementCreated,
  authorName,
}) => {
  const [title, setTitle] = useState('');
  const [category, setCategory] = useState<Announcement['category']>('Academic');
  const [targetRole, setTargetRole] = useState<'all' | 'student' | 'faculty'>('all');
  const [content, setContent] = useState('');

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) {
      alert('Please fill out the title and content.');
      return;
    }

    addAnnouncement({
      title: title.trim(),
      category,
      targetRole,
      content: content.trim(),
      author: authorName,
    });

    onAnnouncementCreated();
    setTitle('');
    setContent('');
    onClose();
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(8px)',
      zIndex: 9999,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '1rem',
    }}>
      <div style={{
        background: '#1c2541',
        border: '1px solid var(--color-border)',
        borderRadius: '20px',
        width: '100%',
        maxWidth: '540px',
        boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6)',
        overflow: 'hidden',
        animation: 'fadeIn 0.2s ease-out',
      }}>
        {/* Modal Header */}
        <div style={{
          padding: '1.25rem 1.5rem',
          background: 'linear-gradient(135deg, #4338ca, #6366f1)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          color: '#ffffff',
        }}>
          <div>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 800 }}>
              📢 Broadcast Campus Announcement
            </h3>
            <p style={{ fontSize: '0.8rem', opacity: 0.9, marginTop: '2px' }}>
              Author: {authorName} (Faculty / Dept Admin)
            </p>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'rgba(255, 255, 255, 0.2)',
              border: 'none',
              color: '#ffffff',
              borderRadius: '50%',
              width: '32px',
              height: '32px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontWeight: 700,
              fontSize: '1rem',
            }}
          >
            ✕
          </button>
        </div>

        {/* Modal Form */}
        <form onSubmit={handleSubmit} style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
          <div className="form-group" style={{ marginBottom: 0 }}>
            <label className="form-label">Announcement Title</label>
            <input
              type="text"
              className="form-input"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Schedule Change for CS-401 Lab / Hackathon Registration"
              required
            />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Category</label>
              <select
                className="form-input"
                value={category}
                onChange={(e) => setCategory(e.target.value as Announcement['category'])}
                style={{ cursor: 'pointer' }}
              >
                <option value="Academic">Academic</option>
                <option value="Placement">Placement</option>
                <option value="Exam">Exam</option>
                <option value="Campus">Campus & Events</option>
                <option value="Faculty">Faculty & Staff</option>
                <option value="Fee">Tuition & Fee</option>
              </select>
            </div>

            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Target Audience</label>
              <select
                className="form-input"
                value={targetRole}
                onChange={(e) => setTargetRole(e.target.value as 'all' | 'student' | 'faculty')}
                style={{ cursor: 'pointer' }}
              >
                <option value="all">Everyone (Students & Faculty)</option>
                <option value="student">Students Only</option>
                <option value="faculty">Faculty & Staff Only</option>
              </select>
            </div>
          </div>

          <div className="form-group" style={{ marginBottom: 0 }}>
            <label className="form-label">Announcement Notice Details</label>
            <textarea
              className="form-input"
              rows={4}
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="Write the full announcement text, instructions, and deadlines here..."
              required
              style={{ resize: 'vertical' }}
            />
          </div>

          {/* Form Actions */}
          <div style={{
            display: 'flex',
            justifyContent: 'flex-end',
            gap: '10px',
            marginTop: '10px',
            paddingTop: '12px',
            borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          }}>
            <button
              type="button"
              onClick={onClose}
              className="btn btn-secondary"
              style={{ fontSize: '0.85rem' }}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn btn-primary"
              style={{ fontSize: '0.85rem' }}
            >
              📢 Publish Announcement
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
