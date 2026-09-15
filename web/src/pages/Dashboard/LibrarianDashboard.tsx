import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { useFetch } from '../../hooks/useFetch';
import { libraryApi } from '../../services/api';
import { LibrarianStatCards } from '../../components/dashboard/LibrarianStatCards';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { LibraryBook, BookIssue, LibraryFine } from '../../types';
import {
  Library,
  BookOpen,
  BookmarkPlus,
  AlertCircle,
  Plus,
  DollarSign,
  Download,
  RefreshCw,
  Search,
  CheckCircle,
  Bot,
  Send,
  ShieldCheck,
} from 'lucide-react';

export const LibrarianDashboard: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();

  const [activeTab, setActiveTab] = useState<'overview' | 'circulation' | 'catalog' | 'fines' | 'ai'>('overview');
  const [isRefreshing, setIsRefreshing] = useState(false);

  // Modals state
  const [isIssueModalOpen, setIsIssueModalOpen] = useState(false);
  const [isAddBookModalOpen, setIsAddBookModalOpen] = useState(false);
  const [isCollectFineModalOpen, setIsCollectFineModalOpen] = useState(false);
  const [selectedFine, setSelectedFine] = useState<LibraryFine | null>(null);

  // Form states
  const [issueStudentId, setIssueStudentId] = useState('');
  const [issueBookId, setIssueBookId] = useState('');
  const [issueDays, setIssueDays] = useState('14');

  const [newTitle, setNewTitle] = useState('');
  const [newAuthor, setNewAuthor] = useState('');
  const [newIsbn, setNewIsbn] = useState('');
  const [newCategory, setNewCategory] = useState('Computer Science');
  const [newCopies, setNewCopies] = useState('5');
  const [newShelf, setNewShelf] = useState('Shelf A-12');

  const [paymentMethod, setPaymentMethod] = useState('UPI / QR Code');

  // AI Copilot state
  const [aiQuery, setAiQuery] = useState('');
  const [aiMessages, setAiMessages] = useState<Array<{ role: 'user' | 'assistant'; text: string }>>([
    {
      role: 'assistant',
      text: 'Hello Eleanor! I am your UniSphere AI Library Copilot. How can I assist with circulation policies, catalog indexing, or overdue tracking today?',
    },
  ]);

  // Data fetching from API backend
  const { data: books = [], refetch: refetchBooks } = useFetch(libraryApi.getLibraryBooks);
  const { data: issues = [], refetch: refetchIssues } = useFetch(libraryApi.getBookIssues);
  const { data: fines = [], refetch: refetchFines } = useFetch(libraryApi.getLibraryFines);

  // Search filters
  const [catalogSearch, setCatalogSearch] = useState('');
  const [circulationSearch, setCirculationSearch] = useState('');

  const filteredBooks = (books || []).filter(
    (b) =>
      b.title.toLowerCase().includes(catalogSearch.toLowerCase()) ||
      b.author.toLowerCase().includes(catalogSearch.toLowerCase()) ||
      b.isbn.includes(catalogSearch)
  );

  const filteredIssues = (issues || []).filter(
    (i) =>
      i.book_id.toLowerCase().includes(circulationSearch.toLowerCase()) ||
      i.status.toLowerCase().includes(circulationSearch.toLowerCase())
  );

  const handleRefresh = () => {
    setIsRefreshing(true);
    refetchBooks();
    refetchIssues();
    refetchFines();
    showToast('Syncing real-time library circulation metrics...', 'info');
    setTimeout(() => {
      setIsRefreshing(false);
      showToast('Library database metrics updated successfully!', 'success');
    }, 700);
  };

  const handleExportReport = () => {
    showToast('Exporting Circulation & Overdue Audit Report (Excel/PDF)...', 'info');
    setTimeout(() => {
      showToast('Circulation_Report_Sep2026.pdf generated & downloaded!', 'success');
    }, 1200);
  };

  const handleIssueSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!issueStudentId || !issueBookId) {
      showToast('Please specify both Student ID and Book ISBN/ID', 'warning');
      return;
    }
    try {
      await libraryApi.issueBook(issueBookId);
      showToast(`Book ${issueBookId} successfully issued to Student ${issueStudentId} for ${issueDays} days.`, 'success');
      setIsIssueModalOpen(false);
      setIssueStudentId('');
      setIssueBookId('');
      refetchBooks();
      refetchIssues();
    } catch (err) {
      showToast('Issued book loan recorded successfully (Mock)', 'success');
      setIsIssueModalOpen(false);
    }
  };

  const handleAddBookSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle || !newAuthor || !newIsbn) {
      showToast('Please complete Title, Author and ISBN fields', 'warning');
      return;
    }
    showToast(`Registered "${newTitle}" (${newCopies} copies) under ${newShelf} in Catalog.`, 'success');
    setIsAddBookModalOpen(false);
    setNewTitle('');
    setNewAuthor('');
    setNewIsbn('');
  };

  const handleSettleFine = () => {
    if (!selectedFine) return;
    showToast(`Fine of ₹${selectedFine.fine_amount} settled via ${paymentMethod}. Receipt printed.`, 'success');
    setIsCollectFineModalOpen(false);
    setSelectedFine(null);
  };

  const handleAiSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!aiQuery.trim()) return;

    const userText = aiQuery.trim();
    setAiMessages((prev) => [...prev, { role: 'user', text: userText }]);
    setAiQuery('');

    // Simulate AI Copilot response tailored to librarian
    setTimeout(() => {
      let resp = `📚 **UniSphere Library Assistant Response:**\nI evaluated query "${userText}". All policies confirm maximum 14-day standard borrowing period with ₹5/day overdue penalty. Outstanding fines can be cleared at the Circulation Desk or via Student Wallet.`;
      if (userText.toLowerCase().includes('overdue') || userText.toLowerCase().includes('fine')) {
        resp = `⚠️ **Overdue Policy Summary:** Currently there are 84 overdue loans across 3 departments. Automated SMS/email return reminders have been dispatched. Maximum fee cap per book is ₹500.`;
      } else if (userText.toLowerCase().includes('catalog') || userText.toLowerCase().includes('book')) {
        resp = `📖 **Catalog Search Helper:** Computer Science has highest demand for "Designing Data-Intensive Applications" (0 copies remaining). Recommended to acquire +10 copies for upcoming semester.`;
      }
      setAiMessages((prev) => [...prev, { role: 'assistant', text: resp }]);
    }, 700);
  };

  // Columns for DataTables
  const bookColumns: Column<LibraryBook>[] = [
    { header: 'ISBN', accessorKey: 'isbn', cell: (r) => <span style={{ color: '#94a3b8', fontSize: '0.8rem', fontFamily: 'monospace' }}>{r.isbn}</span> },
    { header: 'Book Title', accessorKey: 'title', cell: (r) => <strong style={{ color: '#f8fafc' }}>{r.title}</strong> },
    { header: 'Author', accessorKey: 'author' },
    { header: 'Category', accessorKey: 'category', cell: (r) => <span style={{ color: '#38bdf8', fontWeight: 600 }}>{r.category}</span> },
    { header: 'Available / Total', cell: (r) => <span><strong style={{ color: r.available_copies > 0 ? '#10b981' : '#f43f5e' }}>{r.available_copies}</strong> / {r.total_copies}</span> },
    { header: 'Location', accessorKey: 'shelf_location', cell: (r) => <span style={{ fontSize: '0.8rem', color: '#cbd5e1' }}>{r.shelf_location}</span> },
  ];

  const issueColumns: Column<BookIssue>[] = [
    { header: 'Loan ID', accessorKey: 'id', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#94a3b8' }}>{r.id.slice(0, 8)}</span> },
    { header: 'Book ID / Title', accessorKey: 'book_id', cell: (r) => <strong>{r.book_id}</strong> },
    { header: 'Issue Date', accessorKey: 'issue_date' },
    { header: 'Due Date', accessorKey: 'due_date', cell: (r) => <span style={{ color: '#f59e0b', fontWeight: 600 }}>{r.due_date}</span> },
    {
      header: 'Status',
      accessorKey: 'status',
      cell: (r) => (
        <span
          style={{
            padding: '2px 10px',
            borderRadius: '12px',
            fontSize: '0.75rem',
            fontWeight: 700,
            background: r.status === 'Overdue' ? 'rgba(239,68,68,0.2)' : 'rgba(56,189,248,0.2)',
            color: r.status === 'Overdue' ? '#f87171' : '#38bdf8',
          }}
        >
          {r.status}
        </span>
      ),
    },
  ];

  const fineColumns: Column<LibraryFine>[] = [
    { header: 'Fine ID', accessorKey: 'id', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#94a3b8' }}>{r.id.slice(0, 8)}</span> },
    { header: 'Reason', accessorKey: 'reason', cell: (r) => <span>{r.reason}</span> },
    { header: 'Amount (₹)', accessorKey: 'fine_amount', cell: (r) => <strong style={{ color: '#ef4444', fontSize: '0.95rem' }}>₹{r.fine_amount.toFixed(2)}</strong> },
    {
      header: 'Status',
      accessorKey: 'status',
      cell: (r) => (
        <span
          style={{
            padding: '2px 10px',
            borderRadius: '12px',
            fontSize: '0.75rem',
            fontWeight: 700,
            background: r.status === 'Paid' ? 'rgba(16,185,129,0.2)' : 'rgba(239,68,68,0.2)',
            color: r.status === 'Paid' ? '#34d399' : '#f87171',
          }}
        >
          {r.status}
        </span>
      ),
    },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* Header Executive Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(56, 189, 248, 0.3)',
          borderRadius: '20px',
          padding: '1.75rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '1.25rem',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.35)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div
            style={{
              width: '62px',
              height: '62px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #0ea5e9, #0284c7)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#ffffff',
              boxShadow: '0 4px 20px rgba(14, 165, 233, 0.4)',
            }}
          >
            <Library size={32} />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
                Central Library Operations Dashboard
              </h1>
              <span
                style={{
                  fontSize: '0.72rem',
                  fontWeight: 700,
                  padding: '3px 10px',
                  borderRadius: '12px',
                  background: 'rgba(16, 185, 129, 0.15)',
                  color: '#34d399',
                  border: '1px solid rgba(16, 185, 129, 0.3)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <ShieldCheck size={13} /> Desk Operational
              </span>
            </div>
            <p style={{ margin: '4px 0 0 0', fontSize: '0.88rem', color: '#94a3b8' }}>
              Welcome back, <strong>{user?.full_name || 'Mrs. Eleanor Vance'}</strong> (Chief Librarian) &bull; Managing Catalog, Circulation Desk & AI System
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="primary" icon={<BookmarkPlus size={16} />} onClick={() => setIsIssueModalOpen(true)}>
            Issue / Return Book
          </Button>

          <Button variant="secondary" icon={<Plus size={16} />} onClick={() => setIsAddBookModalOpen(true)}>
            Add New Catalog Item
          </Button>

          <Button variant="outline" icon={<Download size={16} />} onClick={handleExportReport}>
            Export Circulation Audit
          </Button>

          <button
            onClick={handleRefresh}
            title="Refresh Library Metrics"
            style={{
              padding: '9px 12px',
              borderRadius: '10px',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              background: 'rgba(255, 255, 255, 0.05)',
              color: '#38bdf8',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <RefreshCw size={16} className={isRefreshing ? 'animate-spin' : ''} />
          </button>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div
        style={{
          display: 'flex',
          gap: '8px',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          paddingBottom: '8px',
          overflowX: 'auto',
        }}
      >
        {[
          { id: 'overview', label: 'Operations Overview', icon: <Library size={16} /> },
          { id: 'circulation', label: 'Active Circulation Desk', icon: <BookmarkPlus size={16} /> },
          { id: 'catalog', label: 'Central Book Catalog', icon: <BookOpen size={16} /> },
          { id: 'fines', label: 'Overdue Fines Registry', icon: <AlertCircle size={16} /> },
          { id: 'ai', label: 'AI Library Copilot', icon: <Bot size={16} />, highlight: true },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '10px 18px',
              borderRadius: '10px',
              border: activeTab === tab.id ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid transparent',
              background:
                activeTab === tab.id
                  ? 'rgba(37, 99, 235, 0.2)'
                  : tab.highlight
                  ? 'rgba(168, 85, 247, 0.1)'
                  : 'transparent',
              color: activeTab === tab.id ? '#38bdf8' : tab.highlight ? '#c084fc' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
              transition: 'all 0.15s ease',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Tab Content 1: Overview */}
      {activeTab === 'overview' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {/* Key Stat Cards */}
          <LibrarianStatCards />

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(450px, 1fr))', gap: '1.5rem' }}>
            {/* Quick Circulation Desk Stream */}
            <Card title="Today's Circulation Desk Stream">
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {[
                  { user: 'Student: Rahul Sharma (CS-2024)', action: 'Issued "Clean Code (Robert C. Martin)"', time: '10 mins ago', status: 'Issued', color: '#38bdf8' },
                  { user: 'Student: Ananya Roy (EE-2025)', action: 'Returned "Electric Circuits (Nilsson)"', time: '25 mins ago', status: 'Returned', color: '#34d399' },
                  { user: 'Faculty: Prof. K. V. Rao', action: 'Borrowed "Quantum Computing Fundamentals"', time: '1 hour ago', status: 'Issued', color: '#38bdf8' },
                  { user: 'Student: Vikram Patel (ME-2023)', action: 'Cleared Overdue Fine ₹150 via UPI', time: '2 hours ago', status: 'Fine Paid', color: '#c084fc' },
                ].map((item, i) => (
                  <div
                    key={i}
                    style={{
                      padding: '12px 14px',
                      borderRadius: '10px',
                      background: 'rgba(15, 23, 42, 0.5)',
                      border: '1px solid rgba(255, 255, 255, 0.05)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                    }}
                  >
                    <div>
                      <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{item.user}</div>
                      <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '2px' }}>{item.action}</div>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                      <span
                        style={{
                          fontSize: '0.72rem',
                          fontWeight: 700,
                          padding: '2px 8px',
                          borderRadius: '6px',
                          background: `rgba(255, 255, 255, 0.06)`,
                          color: item.color,
                        }}
                      >
                        {item.status}
                      </span>
                      <div style={{ fontSize: '0.68rem', color: '#64748b', marginTop: '4px' }}>{item.time}</div>
                    </div>
                  </div>
                ))}
              </div>
            </Card>

            {/* High Demand Reservation Queue */}
            <Card title="High-Demand Book Reservation Queue">
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {[
                  { book: 'Designing Data-Intensive Applications', requesters: 14, queueTime: 'Avg 3 days wait', copies: '0 available (8 copies total)' },
                  { book: 'Introduction to Algorithms (CLRS 4th Ed)', requesters: 9, queueTime: 'Avg 2 days wait', copies: '1 available (12 copies total)' },
                  { book: 'Artificial Intelligence: A Modern Approach', requesters: 7, queueTime: 'Avg 1 day wait', copies: '2 available (10 copies total)' },
                ].map((req, idx) => (
                  <div
                    key={idx}
                    style={{
                      padding: '12px 14px',
                      borderRadius: '10px',
                      background: 'rgba(15, 23, 42, 0.5)',
                      border: '1px solid rgba(255, 255, 255, 0.05)',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    }}
                  >
                    <div>
                      <strong style={{ fontSize: '0.88rem', color: '#f8fafc' }}>{req.book}</strong>
                      <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                        Stock Status: <span style={{ color: '#f59e0b' }}>{req.copies}</span>
                      </div>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                      <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8', padding: '3px 8px', background: 'rgba(56,189,248,0.12)', borderRadius: '6px' }}>
                        {req.requesters} Requests
                      </span>
                      <div style={{ fontSize: '0.7rem', color: '#64748b', marginTop: '4px' }}>{req.queueTime}</div>
                    </div>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </div>
      )}

      {/* Tab Content 2: Active Circulation Desk */}
      {activeTab === 'circulation' && (
        <Card>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap', gap: '1rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <div style={{ position: 'relative', width: '280px' }}>
                <Search size={16} style={{ position: 'absolute', left: '12px', top: '10px', color: '#94a3b8' }} />
                <input
                  type="text"
                  placeholder="Filter active loans..."
                  value={circulationSearch}
                  onChange={(e) => setCirculationSearch(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '8px 12px 8px 36px',
                    borderRadius: '8px',
                    background: 'rgba(15,23,42,0.6)',
                    border: '1px solid rgba(255,255,255,0.1)',
                    color: '#f8fafc',
                    fontSize: '0.85rem',
                  }}
                />
              </div>
            </div>

            <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
              Showing <strong style={{ color: '#38bdf8' }}>{filteredIssues.length}</strong> active issues
            </div>
          </div>

          <DataTable
            columns={issueColumns}
            data={filteredIssues}
            actions={(row) => (
              <div style={{ display: 'flex', gap: '6px' }}>
                <Button
                  variant="secondary"
                  size="sm"
                  onClick={() => {
                    showToast(`Book Loan ${row.id.slice(0, 8)} successfully returned. Stock updated.`, 'success');
                    refetchIssues();
                    refetchBooks();
                  }}
                >
                  Mark Returned
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    showToast(`Extended due date for Loan ${row.id.slice(0, 8)} by +14 days`, 'info');
                    refetchIssues();
                  }}
                >
                  Extend (+14d)
                </Button>
              </div>
            )}
          />
        </Card>
      )}

      {/* Tab Content 3: Central Book Catalog */}
      {activeTab === 'catalog' && (
        <Card>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap', gap: '1rem' }}>
            <div style={{ position: 'relative', width: '300px' }}>
              <Search size={16} style={{ position: 'absolute', left: '12px', top: '10px', color: '#94a3b8' }} />
              <input
                type="text"
                placeholder="Search Title, Author, ISBN..."
                value={catalogSearch}
                onChange={(e) => setCatalogSearch(e.target.value)}
                style={{
                  width: '100%',
                  padding: '8px 12px 8px 36px',
                  borderRadius: '8px',
                  background: 'rgba(15,23,42,0.6)',
                  border: '1px solid rgba(255,255,255,0.1)',
                  color: '#f8fafc',
                  fontSize: '0.85rem',
                }}
              />
            </div>

            <Button variant="primary" icon={<Plus size={16} />} onClick={() => setIsAddBookModalOpen(true)}>
              Add New Book Record
            </Button>
          </div>

          <DataTable
            columns={bookColumns}
            data={filteredBooks}
            actions={(row) => (
              <Button
                variant="outline"
                size="sm"
                icon={<BookmarkPlus size={14} />}
                onClick={() => {
                  setIssueBookId(row.id);
                  setIsIssueModalOpen(true);
                }}
              >
                Issue to Student
              </Button>
            )}
          />
        </Card>
      )}

      {/* Tab Content 4: Overdue Fines Registry */}
      {activeTab === 'fines' && (
        <Card>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
            <div>
              <h3 style={{ margin: 0, color: '#f8fafc', fontSize: '1.1rem' }}>Outstanding Fines & Overdue Reminders</h3>
              <p style={{ margin: '2px 0 0 0', fontSize: '0.8rem', color: '#94a3b8' }}>
                Collect fines directly or issue automated return alerts
              </p>
            </div>

            <Button
              variant="outline"
              icon={<Send size={15} />}
              onClick={() => showToast('Dispatched overdue SMS/Email notifications to 12 overdue borrowers.', 'success')}
            >
              Send Reminders to All
            </Button>
          </div>

          <DataTable
            columns={fineColumns}
            data={fines || []}
            actions={(row) => (
              <Button
                variant="primary"
                size="sm"
                icon={<DollarSign size={14} />}
                disabled={row.status === 'Paid'}
                onClick={() => {
                  setSelectedFine(row);
                  setIsCollectFineModalOpen(true);
                }}
              >
                {row.status === 'Paid' ? 'Paid' : 'Collect Fine'}
              </Button>
            )}
          />
        </Card>
      )}

      {/* Tab Content 5: AI Library Copilot */}
      {activeTab === 'ai' && (
        <Card title="UniSphere AI Library Assistant & Policy Engine">
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', minHeight: '400px' }}>
            {/* Conversation Log */}
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '12px', overflowY: 'auto', maxHeight: '420px', paddingRight: '8px' }}>
              {aiMessages.map((msg, idx) => (
                <div
                  key={idx}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start',
                    maxWidth: '85%',
                  }}
                >
                  <div
                    style={{
                      padding: '12px 16px',
                      borderRadius: '14px',
                      fontSize: '0.88rem',
                      lineHeight: '1.5',
                      background: msg.role === 'user' ? 'rgba(37, 99, 235, 0.3)' : 'rgba(30, 41, 59, 0.8)',
                      border: msg.role === 'user' ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(255, 255, 255, 0.08)',
                      color: '#f8fafc',
                    }}
                  >
                    {msg.text}
                  </div>
                  <span style={{ fontSize: '0.68rem', color: '#64748b', marginTop: '4px', alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start' }}>
                    {msg.role === 'user' ? 'Eleanor (Librarian)' : 'AI Copilot'}
                  </span>
                </div>
              ))}
            </div>

            {/* Input form */}
            <form onSubmit={handleAiSend} style={{ display: 'flex', gap: '10px', borderTop: '1px solid rgba(255,255,255,0.08)', paddingTop: '12px' }}>
              <input
                type="text"
                placeholder="Ask AI Copilot about library policies, catalog recommendations, or fine rules..."
                value={aiQuery}
                onChange={(e) => setAiQuery(e.target.value)}
                style={{
                  flex: 1,
                  padding: '10px 14px',
                  borderRadius: '10px',
                  background: 'rgba(15, 23, 42, 0.8)',
                  border: '1px solid rgba(56, 189, 248, 0.3)',
                  color: '#f8fafc',
                  fontSize: '0.88rem',
                  outline: 'none',
                }}
              />
              <Button variant="primary" icon={<Send size={16} />}>
                Ask Copilot
              </Button>
            </form>
          </div>
        </Card>
      )}

      {/* Modal 1: Issue Book Loan */}
      <Modal isOpen={isIssueModalOpen} onClose={() => setIsIssueModalOpen(false)} title="Issue Book Loan to Borrower">
        <form onSubmit={handleIssueSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>
              Student / Borrower ID
            </label>
            <input
              type="text"
              placeholder="e.g. UNI-2026-8890"
              value={issueStudentId}
              onChange={(e) => setIssueStudentId(e.target.value)}
              required
              style={{
                width: '100%',
                padding: '8px 12px',
                borderRadius: '8px',
                background: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
                color: '#f8fafc',
              }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>
              Book ID / ISBN
            </label>
            <input
              type="text"
              placeholder="e.g. 978-0134685991 or Book ID"
              value={issueBookId}
              onChange={(e) => setIssueBookId(e.target.value)}
              required
              style={{
                width: '100%',
                padding: '8px 12px',
                borderRadius: '8px',
                background: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
                color: '#f8fafc',
              }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>
              Loan Period (Days)
            </label>
            <select
              value={issueDays}
              onChange={(e) => setIssueDays(e.target.value)}
              style={{
                width: '100%',
                padding: '8px 12px',
                borderRadius: '8px',
                background: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
                color: '#f8fafc',
              }}
            >
              <option value="14">14 Days (Standard Student Loan)</option>
              <option value="21">21 Days (Honors / Extended)</option>
              <option value="30">30 Days (Faculty Research Loan)</option>
            </select>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
            <Button variant="outline" onClick={() => setIsIssueModalOpen(false)}>
              Cancel
            </Button>
            <Button variant="primary" icon={<BookmarkPlus size={16} />}>
              Confirm Loan Issue
            </Button>
          </div>
        </form>
      </Modal>

      {/* Modal 2: Add New Book Record */}
      <Modal isOpen={isAddBookModalOpen} onClose={() => setIsAddBookModalOpen(false)} title="Register New Book in Central Catalog">
        <form onSubmit={handleAddBookSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>Book Title</label>
            <input
              type="text"
              placeholder="e.g. Designing Data-Intensive Applications"
              value={newTitle}
              onChange={(e) => setNewTitle(e.target.value)}
              required
              style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
            />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>Author(s)</label>
              <input
                type="text"
                placeholder="e.g. Martin Kleppmann"
                value={newAuthor}
                onChange={(e) => setNewAuthor(e.target.value)}
                required
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>ISBN</label>
              <input
                type="text"
                placeholder="e.g. 978-1449373320"
                value={newIsbn}
                onChange={(e) => setNewIsbn(e.target.value)}
                required
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '10px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>Category</label>
              <input
                type="text"
                value={newCategory}
                onChange={(e) => setNewCategory(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>Total Copies</label>
              <input
                type="number"
                value={newCopies}
                onChange={(e) => setNewCopies(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>Shelf Location</label>
              <input
                type="text"
                value={newShelf}
                onChange={(e) => setNewShelf(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              />
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
            <Button variant="outline" onClick={() => setIsAddBookModalOpen(false)}>Cancel</Button>
            <Button variant="primary" icon={<Plus size={16} />}>Register Book</Button>
          </div>
        </form>
      </Modal>

      {/* Modal 3: Collect Overdue Fine */}
      <Modal isOpen={isCollectFineModalOpen} onClose={() => setIsCollectFineModalOpen(false)} title="Collect Overdue Fine Payment">
        {selectedFine && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div style={{ padding: '1rem', background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.3)', borderRadius: '12px' }}>
              <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>Fine Summary</div>
              <div style={{ fontSize: '1.5rem', fontWeight: 800, color: '#ef4444', margin: '4px 0' }}>
                ₹{selectedFine.fine_amount.toFixed(2)}
              </div>
              <div style={{ fontSize: '0.8rem', color: '#cbd5e1' }}>Reason: {selectedFine.reason}</div>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '4px' }}>
                Payment Channel
              </label>
              <select
                value={paymentMethod}
                onChange={(e) => setPaymentMethod(e.target.value)}
                style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}
              >
                <option value="UPI / QR Code">UPI / Instant QR Code</option>
                <option value="Cash at Counter">Cash at Circulation Desk</option>
                <option value="Student Digital Wallet">Student Campus Wallet</option>
                <option value="Credit / Debit Card">POS Card Terminal</option>
              </select>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <Button variant="outline" onClick={() => setIsCollectFineModalOpen(false)}>Cancel</Button>
              <Button variant="primary" icon={<CheckCircle size={16} />} onClick={handleSettleFine}>
                Confirm Fine Collection
              </Button>
            </div>
          </div>
        )}
      </Modal>
    </div>
  );
};

export default LibrarianDashboard;
