import React, { useState } from 'react';
import { QrCode, ShieldCheck, CheckCircle2 } from 'lucide-react';

export const CertificateVerificationQR: React.FC = () => {
  const [certId, setCertId] = useState('DEG-2026-BTECH-CSE-104');
  const [verified, setVerified] = useState(true);

  const handleVerify = (e: React.FormEvent) => {
    e.preventDefault();
    setVerified(true);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <QrCode className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Digital Degree & Transcript QR Verification Portal</h3>
            <p className="text-xs text-gray-500">Employer verification portal for authenticating degree transcripts & certificates</p>
          </div>
        </div>
      </div>

      <form onSubmit={handleVerify} className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Enter Degree Certificate ID (e.g. DEG-2026-BTECH-CSE-104)..."
          value={certId}
          onChange={e => setCertId(e.target.value)}
          className="flex-1 text-xs border border-gray-200 rounded-lg px-3 py-2 focus:ring-2 focus:ring-emerald-500 focus:outline-none font-mono"
          required
        />
        <button
          type="submit"
          className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <ShieldCheck className="w-4 h-4" /> Verify Document
        </button>
      </form>

      {verified && (
        <div className="p-4 rounded-xl border border-emerald-200 bg-emerald-50/40 space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-emerald-800 bg-emerald-100 px-2.5 py-0.5 rounded-full flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Authenticity Verified by Registrar
            </span>
            <span className="text-xs font-mono text-gray-400">Hash: 0x9928A1F7</span>
          </div>
          <h4 className="font-bold text-xs text-gray-900">B.Tech in Computer Science & Engineering (Honors in AI)</h4>
          <div className="text-xs text-gray-700">
            Graduate: <strong>Alex Morgan</strong> • CGPA: <strong>3.84 / 4.0</strong> • Year: <strong>2026</strong>
          </div>
        </div>
      )}
    </div>
  );
};
