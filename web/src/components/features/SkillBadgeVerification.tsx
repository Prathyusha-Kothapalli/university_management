import React, { useState } from 'react';
import { Award, Share2, CheckCircle2, ShieldCheck } from 'lucide-react';

interface Badge {
  id: string;
  badgeName: string;
  issuer: string;
  issueDate: string;
  badgeHash: string;
  sharedToLinkedin: boolean;
}

export const SkillBadgeVerification: React.FC = () => {
  const [badges, setBadges] = useState<Badge[]>([
    { id: 'bdg-1', badgeName: 'UniSphere Certified AI System Engineer', issuer: 'UniSphere AI & Google Cloud Partner', issueDate: '2026-08-20', badgeHash: '0xBDG9921A', sharedToLinkedin: true },
    { id: 'bdg-2', badgeName: 'Kubernetes Microservices Specialist', issuer: 'Cloud Native Computing Foundation (CNCF)', issueDate: '2026-09-01', badgeHash: '0xBDG7741C', sharedToLinkedin: false },
  ]);

  const toggleShare = (id: string) => {
    setBadges(badges.map(b => b.id === id ? { ...b, sharedToLinkedin: true } : b));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Verifiable Digital Skill Badge Vault (OpenBadge 2.0)</h3>
            <p className="text-xs text-gray-500">Cryptographically verifiable OpenBadge skill certificates with instant LinkedIn sharing</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {badges.map(b => (
          <div key={b.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-[10px] font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded flex items-center gap-0.5">
                  <ShieldCheck className="w-3 h-3 text-blue-600" /> OpenBadge 2.0 Verified
                </span>
                <span className="text-[10px] font-mono text-gray-400">{b.badgeHash}</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{b.badgeName}</h4>
              <p className="text-xs text-gray-500">{b.issuer}</p>
              <div className="text-[11px] text-gray-400 mt-1">Issued on: {b.issueDate}</div>
            </div>

            <button
              onClick={() => toggleShare(b.id)}
              className={`w-full py-1.5 text-xs font-semibold rounded-lg flex items-center justify-center gap-1.5 transition-all mt-2 ${
                b.sharedToLinkedin
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-sm'
              }`}
            >
              {b.sharedToLinkedin ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Shared on LinkedIn Profile
                </>
              ) : (
                <>
                  <Share2 className="w-3.5 h-3.5" /> Share to LinkedIn
                </>
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
