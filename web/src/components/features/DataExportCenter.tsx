import React, { useState } from 'react';
import { Download, FileSpreadsheet, FileText, RefreshCw } from 'lucide-react';

interface ExportDataset {
  id: string;
  name: string;
  category: 'Academic' | 'Financial' | 'Placements' | 'Administrative';
  recordCount: number;
  lastUpdated: string;
}

export const DataExportCenter: React.FC = () => {
  const [downloadingId, setDownloadingId] = useState<string | null>(null);

  const datasets: ExportDataset[] = [
    { id: 'ds-1', name: 'Student Grade & Semester Results Dataset', category: 'Academic', recordCount: 1420, lastUpdated: 'Today, 10:00 AM' },
    { id: 'ds-2', name: 'Tuition Fee Payment & Ledger Summary', category: 'Financial', recordCount: 1850, lastUpdated: 'Yesterday' },
    { id: 'ds-3', name: 'Campus Placement & Company Recruiter Drives', category: 'Placements', recordCount: 340, lastUpdated: '3 days ago' },
    { id: 'ds-4', name: 'Department Faculty Workload & Attendance Audit', category: 'Administrative', recordCount: 120, lastUpdated: 'Today' },
  ];

  const handleExport = (id: string, format: 'PDF' | 'Excel') => {
    setDownloadingId(`${id}-${format}`);
    setTimeout(() => {
      setDownloadingId(null);
    }, 1500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Download className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Comprehensive Data Export & Reporting Center</h3>
            <p className="text-xs text-gray-500">One-click PDF/Excel dataset generator for all university entities</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {datasets.map(ds => (
          <div key={ds.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-emerald-100/60 text-emerald-700 rounded-lg">
                <FileSpreadsheet className="w-5 h-5" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h4 className="font-semibold text-xs text-gray-900">{ds.name}</h4>
                  <span className="text-[10px] bg-gray-200/60 text-gray-700 px-2 py-0.5 rounded font-medium">
                    {ds.category}
                  </span>
                </div>
                <div className="text-[11px] text-gray-400 mt-0.5">
                  {ds.recordCount.toLocaleString()} Records • Last updated: {ds.lastUpdated}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => handleExport(ds.id, 'PDF')}
                disabled={downloadingId === `${ds.id}-PDF`}
                className="text-xs font-semibold px-3 py-1.5 rounded-lg border border-gray-200 bg-white hover:bg-gray-50 text-gray-700 flex items-center gap-1 transition-colors"
              >
                {downloadingId === `${ds.id}-PDF` ? (
                  <RefreshCw className="w-3.5 h-3.5 animate-spin text-emerald-600" />
                ) : (
                  <FileText className="w-3.5 h-3.5 text-rose-500" />
                )}
                Export PDF
              </button>

              <button
                onClick={() => handleExport(ds.id, 'Excel')}
                disabled={downloadingId === `${ds.id}-Excel`}
                className="text-xs font-semibold px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white flex items-center gap-1 transition-colors shadow-sm"
              >
                {downloadingId === `${ds.id}-Excel` ? (
                  <RefreshCw className="w-3.5 h-3.5 animate-spin text-white" />
                ) : (
                  <FileSpreadsheet className="w-3.5 h-3.5" />
                )}
                Export Excel (.xlsx)
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
