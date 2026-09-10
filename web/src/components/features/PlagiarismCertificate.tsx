import React, { useState } from 'react';
import { Award, Download, CheckCircle2, ShieldCheck } from 'lucide-react';

interface CertRecord {
  id: string;
  title: string;
  author: string;
  similarityPct: number;
  issuedDate: string;
  certHash: string;
}

export const PlagiarismCertificate: React.FC = () => {
  const [certs] = useState<CertRecord[]>([
    {
      id: 'PLG-CERT-901',
      title: 'B.Tech Capstone Thesis: Deep Reinforcement Learning for Drone Swarms',
      author: 'Alex Morgan (22CSE104)',
      similarityPct: 4.2,
      issuedDate: '2026-09-05',
      certHash: '0x9928a1f87b32c0a91e'
    }
  ]);

  const [downloading, setDownloading] = useState(false);

  const handleDownload = () => {
    setDownloading(true);
    setTimeout(() => setDownloading(false), 1500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Official Plagiarism Clearance Certificate Exporter</h3>
            <p className="text-xs text-gray-500">Download verified Turnitin/iThenticate similarity clearance certificate for thesis submission</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {certs.map(c => (
          <div key={c.id} className="p-4 rounded-xl border border-emerald-100 bg-emerald-50/30 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-emerald-800 bg-emerald-100 px-2.5 py-0.5 rounded-full flex items-center gap-0.5">
                  <ShieldCheck className="w-3 h-3 text-emerald-600" /> Clearance Passed ({c.similarityPct}% Match)
                </span>
                <span className="font-mono text-[11px] text-gray-400">ID: {c.id}</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{c.title}</h4>
              <div className="text-xs text-gray-600">
                Author: <strong>{c.author}</strong> • Issued: {c.issuedDate}
              </div>
              <div className="text-[10px] font-mono text-gray-400">Digital Signature: {c.certHash}</div>
            </div>

            <button
              onClick={handleDownload}
              disabled={downloading}
              className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm shrink-0"
            >
              {downloading ? (
                <CheckCircle2 className="w-4 h-4 text-white animate-spin" />
              ) : (
                <Download className="w-4 h-4" />
              )}
              Download Clearance PDF
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
