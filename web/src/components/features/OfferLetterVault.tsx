import React, { useState } from 'react';
import { FileText, CheckCircle2, ShieldCheck, PlusCircle } from 'lucide-react';

interface OfferLetter {
  id: string;
  company: string;
  role: string;
  ctc: string;
  joiningDate: string;
  verificationStatus: 'Verified by TPO Cell' | 'Pending Dual-Offer Scrutiny';
}

export const OfferLetterVault: React.FC = () => {
  const [offers, setOffers] = useState<OfferLetter[]>([
    {
      id: 'OFF-101',
      company: 'Microsoft India',
      role: 'Software Development Engineer (SDE-1)',
      ctc: '₹44.0 LPA',
      joiningDate: '2026-07-15',
      verificationStatus: 'Verified by TPO Cell'
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [company, setCompany] = useState('');
  const [role, setRole] = useState('');
  const [ctc, setCtc] = useState('₹32.0 LPA');

  const handleUpload = (e: React.FormEvent) => {
    e.preventDefault();
    if (!company || !role) return;

    const newOffer: OfferLetter = {
      id: `OFF-${Math.floor(100 + Math.random() * 900)}`,
      company,
      role,
      ctc,
      joiningDate: '2026-08-01',
      verificationStatus: 'Verified by TPO Cell'
    };

    setOffers([newOffer, ...offers]);
    setShowModal(false);
    setCompany('');
    setRole('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <FileText className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Placement Offer Letter Vault & Dual-Offer Scrutiny</h3>
            <p className="text-xs text-gray-500">Upload corporate placement offer letters for CTC breakdown analysis & TPO verification</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Upload Offer Letter
        </button>
      </div>

      <div className="space-y-3">
        {offers.map(off => (
          <div key={off.id} className="p-4 rounded-xl border border-emerald-100 bg-emerald-50/30 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <h4 className="font-bold text-xs text-gray-900">{off.company}</h4>
                <span className="font-mono text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">
                  {off.ctc}
                </span>
              </div>
              <p className="text-xs text-gray-700 font-medium">{off.role}</p>
              <div className="text-[11px] text-gray-400">Joining Date: {off.joiningDate}</div>
            </div>

            <span className="text-xs font-semibold text-emerald-700 bg-white border border-emerald-200 px-3 py-1.5 rounded-lg flex items-center gap-1">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" /> {off.verificationStatus}
            </span>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Upload Placement Offer Letter</h3>
            <form onSubmit={handleUpload} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Company Name</label>
                <input
                  type="text"
                  placeholder="e.g. Google India, Microsoft"
                  value={company}
                  onChange={e => setCompany(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-emerald-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Job Role Title</label>
                <input
                  type="text"
                  placeholder="e.g. SDE-1, Cloud Engineer"
                  value={role}
                  onChange={e => setRole(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-emerald-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Total CTC Package</label>
                <input
                  type="text"
                  placeholder="e.g. ₹28.5 LPA"
                  value={ctc}
                  onChange={e => setCtc(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-emerald-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg flex items-center gap-1"
                >
                  <CheckCircle2 className="w-3.5 h-3.5" /> Submit to TPO
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
