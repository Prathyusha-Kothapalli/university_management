import React, { useState } from 'react';
import { QrCode, UserCheck, Shield, Calendar, Clock, CheckCircle } from 'lucide-react';

interface VisitorPass {
  id: string;
  visitorName: string;
  relation: string;
  visitDate: string;
  entryTime: string;
  purpose: string;
  status: 'Approved' | 'Pending Gate Approval' | 'Checked-In';
  qrCodeToken: string;
}

export const VisitorPassModal: React.FC = () => {
  const [passes, setPasses] = useState<VisitorPass[]>([
    {
      id: 'VP-991',
      visitorName: 'Rajesh Kothapalli (Parent)',
      relation: 'Father',
      visitDate: '2026-09-12',
      entryTime: '10:00 AM',
      purpose: 'Parent-Teacher Meeting & Hostel Inspection',
      status: 'Approved',
      qrCodeToken: 'QR-PASS-991-UNI'
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [visitorName, setVisitorName] = useState('');
  const [relation, setRelation] = useState('Parent');
  const [visitDate, setVisitDate] = useState('2026-09-15');
  const [purpose, setPurpose] = useState('');

  const handleRequestPass = (e: React.FormEvent) => {
    e.preventDefault();
    if (!visitorName || !purpose) return;

    const newPass: VisitorPass = {
      id: `VP-${Math.floor(100 + Math.random() * 900)}`,
      visitorName,
      relation,
      visitDate,
      entryTime: '11:00 AM',
      purpose,
      status: 'Approved',
      qrCodeToken: `QR-PASS-${Date.now()}`
    };

    setPasses([newPass, ...passes]);
    setShowModal(false);
    setVisitorName('');
    setPurpose('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-teal-50 text-teal-600 rounded-lg">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Campus Visitor Pass & Security Gate Check-In</h3>
            <p className="text-xs text-gray-500">Generate QR code gate passes for parents, corporate recruiters, and guests</p>
          </div>
        </div>
        <button
          onClick={() => setShowModal(true)}
          className="bg-teal-600 hover:bg-teal-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors"
        >
          <QrCode className="w-4 h-4" />
          Issue Gate Pass
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {passes.map(pass => (
          <div key={pass.id} className="p-4 rounded-xl border border-teal-100 bg-teal-50/30 relative flex gap-4 items-center">
            {/* Mock QR Code graphic */}
            <div className="w-16 h-16 bg-white border border-teal-200 rounded-lg p-1.5 flex flex-col items-center justify-center shrink-0">
              <QrCode className="w-10 h-10 text-gray-800" />
              <span className="text-[8px] font-mono text-gray-500 font-bold">{pass.id}</span>
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-center justify-between mb-1">
                <span className="text-xs font-bold text-gray-900 truncate">{pass.visitorName}</span>
                <span className="text-[10px] bg-emerald-100 text-emerald-800 font-semibold px-2 py-0.5 rounded-full flex items-center gap-0.5">
                  <CheckCircle className="w-3 h-3 text-emerald-600" />
                  {pass.status}
                </span>
              </div>
              <p className="text-xs text-gray-600 truncate mb-1">Purpose: {pass.purpose}</p>
              <div className="flex items-center gap-3 text-[11px] text-gray-500">
                <span className="flex items-center gap-1">
                  <Calendar className="w-3 h-3 text-teal-600" />
                  {pass.visitDate}
                </span>
                <span className="flex items-center gap-1">
                  <Clock className="w-3 h-3 text-teal-600" />
                  {pass.entryTime}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <div className="flex items-center gap-2">
              <UserCheck className="w-5 h-5 text-teal-600" />
              <h3 className="font-semibold text-gray-900 text-sm">Issue Security Gate Visitor Pass</h3>
            </div>

            <form onSubmit={handleRequestPass} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Visitor Full Name</label>
                <input
                  type="text"
                  placeholder="e.g. Ramesh Chandra"
                  value={visitorName}
                  onChange={e => setVisitorName(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-teal-500 focus:outline-none"
                  required
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Relation / Organization</label>
                  <select
                    value={relation}
                    onChange={e => setRelation(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-teal-500"
                  >
                    <option value="Parent">Parent / Guardian</option>
                    <option value="Corporate Recruiter">Corporate Recruiter</option>
                    <option value="Guest Lecturer">Guest Lecturer</option>
                    <option value="Vendor / Delivery">Vendor / Delivery</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Visit Date</label>
                  <input
                    type="date"
                    value={visitDate}
                    onChange={e => setVisitDate(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-teal-500 focus:outline-none"
                    required
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Visit Purpose</label>
                <input
                  type="text"
                  placeholder="e.g. Campus Visit, Placement Discussion"
                  value={purpose}
                  onChange={e => setPurpose(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-teal-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-teal-600 hover:bg-teal-700 text-white rounded-lg"
                >
                  Generate QR Gate Pass
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
