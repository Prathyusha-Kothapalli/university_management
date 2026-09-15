import React, { useState } from 'react';
import { CreditCard, ArrowDownLeft, PlusCircle, CheckCircle, Clock } from 'lucide-react';

interface RefundClaim {
  id: string;
  category: 'Library Caution Deposit' | 'Hostel Security Refund' | 'Excess Tuition Credit' | 'Event Registration Refund';
  amount: number;
  requestDate: string;
  status: 'Approved' | 'Under Review' | 'Disbursed';
  bankRef?: string;
}

export const ExpenditureRefundTracker: React.FC = () => {
  const [claims, setClaims] = useState<RefundClaim[]>([
    { id: 'REF-801', category: 'Library Caution Deposit', amount: 3000, requestDate: '2026-08-15', status: 'Disbursed', bankRef: 'TXN9928104' },
    { id: 'REF-802', category: 'Hostel Security Refund', amount: 5000, requestDate: '2026-09-02', status: 'Under Review' },
    { id: 'REF-803', category: 'Excess Tuition Credit', amount: 1200, requestDate: '2026-09-08', status: 'Approved' }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [category, setCategory] = useState<RefundClaim['category']>('Library Caution Deposit');
  const [amount, setAmount] = useState<number>(2000);

  const handleClaimSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newClaim: RefundClaim = {
      id: `REF-${Math.floor(100 + Math.random() * 900)}`,
      category,
      amount,
      requestDate: new Date().toISOString().split('T')[0],
      status: 'Under Review'
    };
    setClaims([newClaim, ...claims]);
    setShowModal(false);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-purple-50 text-purple-600 rounded-lg">
            <CreditCard className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Financial Refund & Caution Deposit Tracker</h3>
            <p className="text-xs text-gray-500">Track security deposit refunds, library caution money & tuition credits</p>
          </div>
        </div>
        <button
          onClick={() => setShowModal(true)}
          className="bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-colors"
        >
          <PlusCircle className="w-4 h-4" />
          Request Refund
        </button>
      </div>

      <div className="divide-y divide-gray-100 border border-gray-100 rounded-xl overflow-hidden">
        {claims.map(claim => (
          <div key={claim.id} className="p-3.5 bg-white flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-purple-50 text-purple-600 rounded-lg">
                <ArrowDownLeft className="w-4 h-4" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-semibold text-xs text-gray-900">{claim.category}</span>
                  <span className="font-mono text-[11px] text-gray-400">#{claim.id}</span>
                </div>
                <span className="text-[11px] text-gray-500">Requested on: {claim.requestDate}</span>
              </div>
            </div>

            <div className="text-right">
              <div className="font-bold text-sm text-gray-900 font-mono">₹{claim.amount.toLocaleString('en-IN')}</div>
              <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-full inline-flex items-center gap-1 ${
                claim.status === 'Disbursed' ? 'bg-emerald-50 text-emerald-700' :
                claim.status === 'Approved' ? 'bg-blue-50 text-blue-700' :
                'bg-amber-50 text-amber-700'
              }`}>
                {claim.status === 'Disbursed' && <CheckCircle className="w-3 h-3 text-emerald-600" />}
                {claim.status === 'Under Review' && <Clock className="w-3 h-3 text-amber-600" />}
                {claim.status}
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* Claim Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Submit Refund Claim</h3>
            <form onSubmit={handleClaimSubmit} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Claim Category</label>
                <select
                  value={category}
                  onChange={e => setCategory(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-purple-500"
                >
                  <option value="Library Caution Deposit">Library Caution Deposit</option>
                  <option value="Hostel Security Refund">Hostel Security Refund</option>
                  <option value="Excess Tuition Credit">Excess Tuition Credit</option>
                  <option value="Event Registration Refund">Event Registration Refund</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Refund Amount (₹)</label>
                <input
                  type="number"
                  value={amount}
                  onChange={e => setAmount(Number(e.target.value))}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-purple-500 font-semibold"
                  min="500"
                  required
                />
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-xs text-gray-600 hover:bg-gray-100 rounded-lg"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-medium bg-purple-600 hover:bg-purple-700 text-white rounded-lg"
                >
                  Submit Claim
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
