import React, { useState } from 'react';
import { Award, FileText, CheckCircle2, Clock, PlusCircle } from 'lucide-react';

interface Patent {
  id: string;
  title: string;
  applicationNo: string;
  inventors: string;
  filingDate: string;
  status: 'Published in Patent Journal' | 'FER Examination' | 'Granted';
}

export const PatentFilingManager: React.FC = () => {
  const [patents, setPatents] = useState<Patent[]>([
    {
      id: 'PAT-2026-01',
      title: 'Edge-AI System for Real-Time Traffic Density Optimization using Distributed Cameras',
      applicationNo: '202641098271 A',
      inventors: 'Dr. Ananya Sharma, Alex Morgan (Student)',
      filingDate: '2026-02-14',
      status: 'Published in Patent Journal'
    },
    {
      id: 'PAT-2025-08',
      title: 'Low-Power IoT Sensor Node with Solar Kinetic Energy Harvesting',
      applicationNo: '202541088192 A',
      inventors: 'Dr. Rajesh Verma, Vikram Mehta',
      filingDate: '2025-10-10',
      status: 'FER Examination'
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [title, setTitle] = useState('');
  const [inventors, setInventors] = useState('');

  const handleFilePatent = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !inventors) return;

    const newPatent: Patent = {
      id: `PAT-2026-0${patents.length + 2}`,
      title,
      applicationNo: `2026410${Math.floor(1000 + Math.random() * 9000)} A`,
      inventors,
      filingDate: new Date().toISOString().split('T')[0],
      status: 'Published in Patent Journal'
    };

    setPatents([newPatent, ...patents]);
    setShowModal(false);
    setTitle('');
    setInventors('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-purple-50 text-purple-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">University Intellectual Property & Patent Manager</h3>
            <p className="text-xs text-gray-500">Track patent disclosures, Indian Patent Office filings & commercialization</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          File Patent Disclosure
        </button>
      </div>

      <div className="space-y-3">
        {patents.map(p => (
          <div key={p.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-mono text-xs font-bold text-purple-700 bg-purple-100 px-2.5 py-0.5 rounded">
                App No: {p.applicationNo}
              </span>
              <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full flex items-center gap-1 ${
                p.status === 'Granted' ? 'bg-emerald-50 text-emerald-700' : 'bg-purple-50 text-purple-700'
              }`}>
                {p.status === 'Granted' ? <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> : <Clock className="w-3.5 h-3.5 text-purple-600" />}
                {p.status}
              </span>
            </div>

            <h4 className="font-bold text-xs text-gray-900">{p.title}</h4>
            <div className="flex items-center justify-between text-xs text-gray-500 pt-1 border-t border-gray-100">
              <span>Inventors: <strong>{p.inventors}</strong></span>
              <span className="text-[11px] text-gray-400">Filed: {p.filingDate}</span>
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">File Invention Disclosure Form</h3>
            <form onSubmit={handleFilePatent} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Invention Title</label>
                <input
                  type="text"
                  placeholder="e.g. Novel Machine Learning Algorithm for Cyber Attack Detection"
                  value={title}
                  onChange={e => setTitle(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-purple-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Co-Inventors (Faculty & Students)</label>
                <input
                  type="text"
                  placeholder="e.g. Dr. Ananya Sharma, Alex Morgan"
                  value={inventors}
                  onChange={e => setInventors(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-purple-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-purple-600 hover:bg-purple-700 text-white rounded-lg flex items-center gap-1"
                >
                  <FileText className="w-3.5 h-3.5" /> Submit IP Disclosure
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
