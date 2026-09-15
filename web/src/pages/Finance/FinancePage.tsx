import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { financeApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { FeeStructure, StudentFee, Payment } from '../../types';
import { CreditCard, DollarSign, Receipt, CheckCircle, Printer, QrCode, Award, Calendar } from 'lucide-react';

export const FinancePage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'status' | 'structures' | 'payments'>('status');
  const [isPayModalOpen, setIsPayModalOpen] = useState(false);
  const [payAmount, setPayAmount] = useState('1800');
  const [payMethod, setPayMethod] = useState('UPI');

  // Feature 8: Scholarship Modal State
  const [isScholarshipModalOpen, setIsScholarshipModalOpen] = useState(false);
  const [scholarshipType, setScholarshipType] = useState('Merit-Based Academic Scholarship (50% Tuition)');
  const [scholarshipReason, setScholarshipReason] = useState('');

  // Feature 11: Installment Plan Modal State
  const [isInstallmentModalOpen, setIsInstallmentModalOpen] = useState(false);
  const [installmentMonths, setInstallmentMonths] = useState(3);

  // Feature 12: Payment Filter State
  const [paymentFilterMethod, setPaymentFilterMethod] = useState<string>('All');

  // Receipt Modal
  const [selectedPayment, setSelectedPayment] = useState<Payment | null>(null);

  const { data: structures = [] } = useFetch(financeApi.getFeeStructures);
  const { data: studentFees = [], refetch: refetchFees } = useFetch(financeApi.getStudentFees);
  const { data: payments = [], refetch: refetchPayments } = useFetch(financeApi.getPayments);

  const handleMakePayment = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await financeApi.createPayment({
        amount: Number(payAmount),
        payment_method: payMethod,
      });
      showToast(`Payment of $${payAmount} processed successfully!`, 'success');
      setIsPayModalOpen(false);
      refetchFees();
      refetchPayments();
    } catch (err) {
      showToast('Payment processing failed', 'error');
    }
  };

  const handleApplyScholarship = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Submitted application for "${scholarshipType}"`, 'success');
    setIsScholarshipModalOpen(false);
    setScholarshipReason('');
  };

  const handleConfirmInstallmentPlan = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Approved ${installmentMonths}-Month Fee Installment Schedule ($${(1800 / installmentMonths).toFixed(2)}/mo)`, 'success');
    setIsInstallmentModalOpen(false);
  };

  const handlePrintReceipt = () => {
    window.print();
    showToast('Printing official tax receipt...', 'info');
  };

  const filteredPayments = (payments || []).filter(
    (p) => paymentFilterMethod === 'All' || p.payment_method === paymentFilterMethod
  );

  const feeColumns: Column<StudentFee>[] = [
    { header: 'Fee ID', accessorKey: 'id', cell: (r) => <span style={{ color: '#38bdf8' }}>{r.id}</span> },
    { header: 'Total Fee', accessorKey: 'total_amount', cell: (r) => <span>${r.total_amount}</span> },
    { header: 'Amount Paid', accessorKey: 'amount_paid', cell: (r) => <span style={{ color: '#10b981' }}>${r.amount_paid}</span> },
    { header: 'Due Amount', accessorKey: 'due_amount', cell: (r) => <span style={{ color: '#f59e0b' }}>${r.due_amount}</span> },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: r.status === 'Paid' ? 'rgba(16,185,129,0.2)' : 'rgba(245,158,11,0.2)', color: r.status === 'Paid' ? '#10b981' : '#f59e0b', fontSize: '0.75rem', fontWeight: 600 }}>{r.status}</span> },
  ];

  const paymentColumns: Column<Payment>[] = [
    { header: 'Ref TXN', accessorKey: 'transaction_reference', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.transaction_reference}</strong> },
    { header: 'Date', accessorKey: 'payment_date', cell: (r) => <span>{new Date(r.payment_date).toLocaleDateString()}</span> },
    { header: 'Amount', accessorKey: 'amount', cell: (r) => <strong>${r.amount}</strong> },
    { header: 'Method', accessorKey: 'payment_method' },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#10b981', fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  const structureColumns: Column<FeeStructure>[] = [
    { header: 'Program ID', accessorKey: 'program_id' },
    { header: 'Tuition Fee', accessorKey: 'tuition_fee', cell: (r) => <span>${r.tuition_fee}</span> },
    { header: 'Library Fee', accessorKey: 'library_fee', cell: (r) => <span>${r.library_fee}</span> },
    { header: 'Hostel Fee', accessorKey: 'hostel_fee', cell: (r) => <span>${r.hostel_fee}</span> },
    { header: 'Total Package', accessorKey: 'total_amount', cell: (r) => <strong style={{ color: '#10b981' }}>${r.total_amount}</strong> },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Fee Management & Payment Gateway
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 7 APIs (`/api/v1/fee-structures/`, `/api/v1/student-fees/`, `/api/v1/payments/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <Button variant="secondary" icon={<Calendar size={16} />} onClick={() => setIsInstallmentModalOpen(true)}>
            Installment Plan
          </Button>
          <Button variant="secondary" icon={<Award size={16} />} onClick={() => setIsScholarshipModalOpen(true)}>
            Apply for Merit Scholarship
          </Button>
          <Button variant="primary" icon={<CreditCard size={16} />} onClick={() => setIsPayModalOpen(true)}>
            Pay Remaining Balance
          </Button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'status', label: 'Student Fee Balance', icon: <DollarSign size={16} /> },
          { id: 'payments', label: 'Payment History & Receipts', icon: <Receipt size={16} /> },
          { id: 'structures', label: 'Fee Structures', icon: <CreditCard size={16} /> },
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
        {activeTab === 'status' && <DataTable columns={feeColumns} data={studentFees || []} />}
        {activeTab === 'payments' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {/* Feature 12: Payment Method Filter Bar */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '0.8rem', color: '#cbd5e1' }}>
              <span>Filter by Method:</span>
              {['All', 'UPI', 'Card', 'Bank Transfer'].map((m) => (
                <button
                  key={m}
                  onClick={() => setPaymentFilterMethod(m)}
                  style={{
                    padding: '4px 10px',
                    borderRadius: '12px',
                    border: paymentFilterMethod === m ? '1px solid #38bdf8' : '1px solid transparent',
                    background: paymentFilterMethod === m ? 'rgba(56,189,248,0.2)' : 'rgba(255,255,255,0.05)',
                    color: paymentFilterMethod === m ? '#38bdf8' : '#94a3b8',
                    cursor: 'pointer',
                    fontSize: '0.75rem',
                    fontWeight: 600,
                  }}
                >
                  {m}
                </button>
              ))}
            </div>

            <DataTable
              columns={paymentColumns}
              data={filteredPayments}
              actions={(row) => (
                <Button variant="outline" size="sm" icon={<Receipt size={14} />} onClick={() => setSelectedPayment(row)}>
                  View Receipt
                </Button>
              )}
            />
          </div>
        )}
        {activeTab === 'structures' && <DataTable columns={structureColumns} data={structures || []} />}
      </Card>

      {/* Feature 11: Installment Plan Modal */}
      <Modal isOpen={isInstallmentModalOpen} onClose={() => setIsInstallmentModalOpen(false)} title="Fee Installment Plan Schedule">
        <form onSubmit={handleConfirmInstallmentPlan} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Select Number of Monthly Installments</label>
            <select
              value={installmentMonths}
              onChange={(e) => setInstallmentMonths(Number(e.target.value))}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            >
              <option value={2}>2 Monthly Installments ($900.00 / month)</option>
              <option value={3}>3 Monthly Installments ($600.00 / month)</option>
              <option value={4}>4 Monthly Installments ($450.00 / month)</option>
            </select>
          </div>

          <div style={{ padding: '1rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '10px' }}>
            <div style={{ fontSize: '0.85rem', color: '#38bdf8', fontWeight: 700 }}>Installment Breakdown (${(1800 / installmentMonths).toFixed(2)} x {installmentMonths}):</div>
            <div style={{ fontSize: '0.8rem', color: '#cbd5e1', marginTop: '6px' }}>
              • Installment 1: Due Oct 15, 2026 (${(1800 / installmentMonths).toFixed(2)})
              <br />
              • Installment 2: Due Nov 15, 2026 (${(1800 / installmentMonths).toFixed(2)})
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsInstallmentModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Activate Installment Plan</Button>
          </div>
        </form>
      </Modal>

      {/* Pay Modal */}
      <Modal isOpen={isPayModalOpen} onClose={() => setIsPayModalOpen(false)} title="Process Fee Payment">
        <form onSubmit={handleMakePayment} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Payment Amount ($ USD)</label>
            <input
              type="number"
              required
              value={payAmount}
              onChange={(e) => setPayAmount(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Payment Method</label>
            <select
              value={payMethod}
              onChange={(e) => setPayMethod(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            >
              <option value="UPI">UPI / Instant Bank Transfer</option>
              <option value="Card">Credit / Debit Card</option>
              <option value="Bank Transfer">Net Banking / Wire Transfer</option>
            </select>
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsPayModalOpen(false)}>Cancel</Button>
            <Button variant="success" type="submit" icon={<CheckCircle size={16} />}>Confirm & Pay</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 8: Scholarship Application Modal */}
      <Modal isOpen={isScholarshipModalOpen} onClose={() => setIsScholarshipModalOpen(false)} title="Apply for Fee Exemption / Merit Scholarship">
        <form onSubmit={handleApplyScholarship} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Scholarship Program</label>
            <select
              value={scholarshipType}
              onChange={(e) => setScholarshipType(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            >
              <option value="Merit-Based Academic Scholarship (50% Tuition)">Merit-Based Academic Excellence (CGPA &gt; 3.8)</option>
              <option value="Dean Research Assistantship Grant">Dean Research Assistantship Grant</option>
              <option value="Need-Based Financial Assistance">Need-Based Financial Assistance</option>
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Statement of Purpose / Justification</label>
            <textarea
              required
              rows={3}
              placeholder="Briefly state your academic accomplishments..."
              value={scholarshipReason}
              onChange={(e) => setScholarshipReason(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsScholarshipModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Submit Application</Button>
          </div>
        </form>
      </Modal>

      {/* Official Tax Receipt Modal */}
      <Modal isOpen={!!selectedPayment} onClose={() => setSelectedPayment(null)} title="Official Payment Receipt">
        {selectedPayment && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '12px' }}>
              <div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Transaction Reference</div>
                <strong style={{ fontSize: '1.1rem', color: '#38bdf8' }}>{selectedPayment.transaction_reference}</strong>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Status</div>
                <span style={{ fontSize: '0.85rem', color: '#10b981', fontWeight: 700 }}>VERIFIED COMPLETED</span>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', fontSize: '0.85rem' }}>
              <div>
                <span style={{ color: '#94a3b8' }}>Payment Date:</span>
                <div style={{ color: '#fff', fontWeight: 600 }}>{new Date(selectedPayment.payment_date).toLocaleString()}</div>
              </div>
              <div>
                <span style={{ color: '#94a3b8' }}>Payment Method:</span>
                <div style={{ color: '#fff', fontWeight: 600 }}>{selectedPayment.payment_method}</div>
              </div>
              <div>
                <span style={{ color: '#94a3b8' }}>Amount Paid:</span>
                <div style={{ color: '#10b981', fontSize: '1.2rem', fontWeight: 800 }}>${selectedPayment.amount}</div>
              </div>
              <div>
                <span style={{ color: '#94a3b8' }}>Issued By:</span>
                <div style={{ color: '#fff', fontWeight: 600 }}>UniSphere Bursar Office</div>
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '16px', padding: '1rem', background: 'rgba(255,255,255,0.03)', borderRadius: '10px' }}>
              <QrCode size={48} style={{ color: '#38bdf8' }} />
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>
                Digital signature hash: <code>sha256-e981f72a4bc0011928374a...</code>
                <br />
                Scan QR code to verify receipt validity with UniSphere Registrar.
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <Button variant="ghost" onClick={() => setSelectedPayment(null)}>Close</Button>
              <Button variant="primary" icon={<Printer size={16} />} onClick={handlePrintReceipt}>Print Receipt</Button>
            </div>
          </div>
        )}
      </Modal>
    </div>
  );
};
