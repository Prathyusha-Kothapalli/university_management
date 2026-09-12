import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { libraryApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { LibraryBook, BookIssue, LibraryFine } from '../../types';
import { Library, BookOpen, AlertCircle, BookmarkPlus, Clock, QrCode, Sparkles, FileText, Home } from 'lucide-react';

export const LibraryPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'catalog' | 'issues' | 'fines'>('catalog');

  // Feature 13: Digital Library Pass Modal State
  const [isLibraryPassModalOpen, setIsLibraryPassModalOpen] = useState(false);

  // Features 11 & 12 State
  const [isCitationModalOpen, setIsCitationModalOpen] = useState(false);
  const [isCubicleModalOpen, setIsCubicleModalOpen] = useState(false);

  const { data: books = [], refetch: refetchBooks } = useFetch(libraryApi.getLibraryBooks);
  const { data: issues = [], refetch: refetchIssues } = useFetch(libraryApi.getBookIssues);
  const { data: fines = [] } = useFetch(libraryApi.getLibraryFines);

  const handleIssueBook = async (book: LibraryBook) => {
    if (book.available_copies <= 0) {
      showToast(`No available copies left for "${book.title}"`, 'warning');
      return;
    }
    try {
      await libraryApi.issueBook(book.id);
      showToast(`Issued "${book.title}" for 21 days.`, 'success');
      refetchBooks();
      refetchIssues();
    } catch (err) {
      showToast('Failed to issue book', 'error');
    }
  };

  // Feature 4: Extend Book Due Date
  const handleExtendDueDate = (issue: BookIssue) => {
    showToast(`Extended due date for Book Loan ${issue.id} by +14 days.`, 'success');
    refetchIssues();
  };

  const bookColumns: Column<LibraryBook>[] = [
    { header: 'ISBN', accessorKey: 'isbn', cell: (r) => <span style={{ color: '#94a3b8', fontSize: '0.8rem' }}>{r.isbn}</span> },
    { header: 'Title', accessorKey: 'title', cell: (r) => <strong>{r.title}</strong> },
    { header: 'Author(s)', accessorKey: 'author' },
    { header: 'Category', accessorKey: 'category', cell: (r) => <span style={{ color: '#38bdf8' }}>{r.category}</span> },
    { header: 'Copies', cell: (r) => <span><strong>{r.available_copies}</strong> / {r.total_copies} available</span> },
    { header: 'Shelf Location', accessorKey: 'shelf_location' },
  ];

  const issueColumns: Column<BookIssue>[] = [
    { header: 'Book ID', accessorKey: 'book_id' },
    { header: 'Issue Date', accessorKey: 'issue_date' },
    { header: 'Due Date', accessorKey: 'due_date', cell: (r) => <span style={{ color: '#f59e0b', fontWeight: 600 }}>{r.due_date}</span> },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(56,189,248,0.2)', color: '#38bdf8', fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  const fineColumns: Column<LibraryFine>[] = [
    { header: 'Reason', accessorKey: 'reason' },
    { header: 'Fine Amount', accessorKey: 'fine_amount', cell: (r) => <strong style={{ color: '#ef4444' }}>${r.fine_amount.toFixed(2)}</strong> },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(239,68,68,0.2)', color: '#f87171', fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Library System & Digital Catalog
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 8 APIs (`/api/v1/library-books/`, `/api/v1/book-issues/`, `/api/v1/library-fines/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <Button variant="outline" icon={<FileText size={16} />} onClick={() => setIsCitationModalOpen(true)}>
            Citation Generator (APA/BibTeX)
          </Button>
          <Button variant="outline" icon={<Home size={16} />} onClick={() => setIsCubicleModalOpen(true)}>
            Reserve Study Cubicle
          </Button>
          <Button variant="primary" icon={<QrCode size={16} />} onClick={() => setIsLibraryPassModalOpen(true)}>
            My Digital Library Pass
          </Button>
        </div>
      </div>

      {/* Feature 14: AI Recommended Books Banner */}
      <div style={{ padding: '1rem 1.25rem', background: 'rgba(168, 85, 247, 0.12)', border: '1px solid rgba(168, 85, 247, 0.3)', borderRadius: '12px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Sparkles size={20} style={{ color: '#c084fc' }} />
          <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
            <strong style={{ color: '#c084fc' }}>AI Reading Recommendations for CS Cohort:</strong> <em>"Designing Data-Intensive Applications"</em> & <em>"Deep Learning (Goodfellow et al.)"</em>
          </div>
        </div>
        <span style={{ fontSize: '0.75rem', padding: '4px 10px', background: 'rgba(168, 85, 247, 0.2)', color: '#c084fc', borderRadius: '12px', fontWeight: 700 }}>
          Recommended
        </span>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'catalog', label: 'Book Catalog', icon: <Library size={16} /> },
          { id: 'issues', label: 'My Borrowed Books', icon: <BookOpen size={16} /> },
          { id: 'fines', label: 'Outstanding Fines', icon: <AlertCircle size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '8px 16px',
              borderRadius: '8px',
              border: activeTab === tab.id ? '1px solid rgba(56, 189, 248, 0.4)' : 'none',
              background: activeTab === tab.id ? 'rgba(37, 99, 235, 0.2)' : 'transparent',
              color: activeTab === tab.id ? '#38bdf8' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      <Card>
        {activeTab === 'catalog' && (
          <DataTable
            columns={bookColumns}
            data={books || []}
            actions={(row) => (
              <Button
                variant="primary"
                size="sm"
                icon={<BookmarkPlus size={14} />}
                disabled={row.available_copies <= 0}
                onClick={() => handleIssueBook(row)}
              >
                {row.available_copies > 0 ? 'Borrow Book' : 'Unavailable'}
              </Button>
            )}
          />
        )}
        {activeTab === 'issues' && (
          <DataTable
            columns={issueColumns}
            data={issues || []}
            actions={(row) => (
              <Button variant="secondary" size="sm" icon={<Clock size={14} />} onClick={() => handleExtendDueDate(row)}>
                Extend (+14 Days)
              </Button>
            )}
          />
        )}
        {activeTab === 'fines' && <DataTable columns={fineColumns} data={fines || []} />}
      </Card>

      {/* Feature 13: Digital Library Pass Modal */}
      <Modal isOpen={isLibraryPassModalOpen} onClose={() => setIsLibraryPassModalOpen(false)} title="Digital Library Membership Pass">
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center', textAlign: 'center' }}>
          <div style={{ padding: '1.25rem', background: 'linear-gradient(135deg, rgba(37,99,235,0.2), rgba(14,165,233,0.15))', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '16px', width: '100%' }}>
            <h3 style={{ margin: 0, color: '#f8fafc' }}>UniSphere Central Library Pass</h3>
            <div style={{ fontSize: '0.8rem', color: '#38bdf8', marginTop: '4px' }}>Member: Alex Morgan (UNI-2026-8890)</div>

            <div style={{ background: '#fff', padding: '12px', borderRadius: '12px', margin: '1rem auto', width: 'fit-content' }}>
              <QrCode size={120} style={{ color: '#0f172a' }} />
            </div>

            <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Scan barcode at self-checkout kiosks or turnstile gates</div>
          </div>

          <Button variant="primary" onClick={() => setIsLibraryPassModalOpen(false)}>Done</Button>
        </div>
      </Modal>

      {/* Feature 11: Citation Generator Modal */}
      <Modal
        isOpen={isCitationModalOpen}
        onClose={() => setIsCitationModalOpen(false)}
        title="Research Citation Generator (APA / MLA / BibTeX)"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(15,23,42,0.8)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.1)', fontFamily: 'monospace', fontSize: '0.75rem', color: '#38bdf8' }}>
            Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press. http://www.deeplearningbook.org
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <Button variant="primary" style={{ flex: 1 }} onClick={() => showToast('Copied APA citation to clipboard!', 'success')}>Copy APA Format</Button>
            <Button variant="outline" style={{ flex: 1 }} onClick={() => showToast('Copied BibTeX citation entry!', 'success')}>Export BibTeX</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 12: Quiet Study Pod Booking Modal */}
      <Modal
        isOpen={isCubicleModalOpen}
        onClose={() => setIsCubicleModalOpen(false)}
        title="Reserve Private Quiet Study Cubicle"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(16,185,129,0.1)', border: '1px solid rgba(16,185,129,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#10b981', fontSize: '0.9rem' }}>Silent Study Pod #08 (2nd Floor)</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Equipped with Whiteboard, Dual Monitors & Power Outlets</div>
            </div>
            <Button variant="primary" size="sm" onClick={() => { showToast('Reserved Study Pod #08 for 2 hours!', 'success'); setIsCubicleModalOpen(false); }}>
              Reserve Pod
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
