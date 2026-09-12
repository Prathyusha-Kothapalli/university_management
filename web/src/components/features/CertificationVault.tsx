import React, { useState } from 'react';
import { Award, CheckCircle, ExternalLink, PlusCircle, ShieldCheck } from 'lucide-react';

interface Cert {
  id: string;
  title: string;
  provider: 'AWS' | 'NPTEL' | 'Coursera' | 'Google Cloud' | 'Oracle';
  issuedDate: string;
  credentialUrl: string;
  verified: boolean;
}

export const CertificationVault: React.FC = () => {
  const [certs, setCerts] = useState<Cert[]>([
    {
      id: 'CRT-901',
      title: 'AWS Certified Solutions Architect – Associate',
      provider: 'AWS',
      issuedDate: '2026-06-15',
      credentialUrl: 'https://aws.amazon.com/verification',
      verified: true
    },
    {
      id: 'CRT-902',
      title: 'Deep Learning & Neural Networks Specialization',
      provider: 'Coursera',
      issuedDate: '2026-04-10',
      credentialUrl: 'https://coursera.org/verify/DL-992',
      verified: true
    },
    {
      id: 'CRT-903',
      title: 'NPTEL Elite Gold: Machine Learning for Engineering',
      provider: 'NPTEL',
      issuedDate: '2025-11-20',
      credentialUrl: 'https://nptel.ac.in/noc/E-certificate',
      verified: true
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [title, setTitle] = useState('');
  const [provider, setProvider] = useState<Cert['provider']>('AWS');
  const [credentialUrl, setCredentialUrl] = useState('');

  const handleUpload = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title) return;

    const newCert: Cert = {
      id: `CRT-${Math.floor(100 + Math.random() * 900)}`,
      title,
      provider,
      issuedDate: new Date().toISOString().split('T')[0],
      credentialUrl: credentialUrl || 'https://verification.unisphere.ai',
      verified: true
    };

    setCerts([newCert, ...certs]);
    setShowModal(false);
    setTitle('');
    setCredentialUrl('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-amber-50 text-amber-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Skill Certification & Micro-Credential Vault</h3>
            <p className="text-xs text-gray-500">Upload & verify AWS, NPTEL, Coursera industry certifications for placement portfolio</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Upload Certificate
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {certs.map(cert => (
          <div key={cert.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex flex-col justify-between space-y-3">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold text-amber-700 bg-amber-100/60 px-2.5 py-0.5 rounded-full">
                  {cert.provider}
                </span>
                <span className="text-emerald-600 text-[11px] font-semibold flex items-center gap-0.5">
                  <ShieldCheck className="w-3.5 h-3.5" /> Verified
                </span>
              </div>
              <h4 className="font-semibold text-xs text-gray-900 line-clamp-2 mb-1">{cert.title}</h4>
              <p className="text-[11px] text-gray-400">Issued: {cert.issuedDate}</p>
            </div>

            <div className="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span className="font-mono text-[10px] text-gray-400">{cert.id}</span>
              <a
                href={cert.credentialUrl}
                target="_blank"
                rel="noreferrer"
                className="text-xs font-semibold text-amber-600 hover:text-amber-700 flex items-center gap-1"
              >
                View Credential <ExternalLink className="w-3 h-3" />
              </a>
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Upload Industry Certification</h3>
            <form onSubmit={handleUpload} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Certificate Title</label>
                <input
                  type="text"
                  placeholder="e.g. AWS Solutions Architect, NPTEL Data Mining"
                  value={title}
                  onChange={e => setTitle(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Certification Provider</label>
                <select
                  value={provider}
                  onChange={e => setProvider(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-amber-500"
                >
                  <option value="AWS">Amazon Web Services (AWS)</option>
                  <option value="Coursera">Coursera / Industry Specialization</option>
                  <option value="NPTEL">NPTEL / SWAYAM Govt Portal</option>
                  <option value="Google Cloud">Google Cloud (GCP)</option>
                  <option value="Oracle">Oracle Certified Professional</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Verification Link / ID</label>
                <input
                  type="url"
                  placeholder="https://coursera.org/verify/..."
                  value={credentialUrl}
                  onChange={e => setCredentialUrl(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-amber-600 hover:bg-amber-700 text-white rounded-lg flex items-center gap-1"
                >
                  <CheckCircle className="w-3.5 h-3.5" />
                  Save to Portfolio
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
