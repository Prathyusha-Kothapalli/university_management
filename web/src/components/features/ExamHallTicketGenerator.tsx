import React, { useState } from 'react';
import { Download, QrCode, ShieldCheck, CheckCircle2 } from 'lucide-react';

export const ExamHallTicketGenerator: React.FC = () => {
  const [hallTicket] = useState({
    ticketNo: 'HT-2026-CSE-104',
    studentName: 'Alex Morgan',
    rollNo: '22CSE104',
    semester: 'Semester VI (Spring 2026)',
    attendanceClearance: 'Cleared (94.5%)',
    feeDues: 'Zero Outstanding',
    examCenter: 'Block B - Ada Lovelace Examination Complex',
    seatNo: 'Desk B-42'
  });

  const [downloading, setDownloading] = useState(false);

  const handleDownload = () => {
    setDownloading(true);
    setTimeout(() => setDownloading(false), 1500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-purple-50 text-purple-600 rounded-lg">
            <QrCode className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Semester Exam Hall Ticket & Seat Allocation Portal</h3>
            <p className="text-xs text-gray-500">Download official exam admittance pass with QR security verification & seat allocation</p>
          </div>
        </div>
      </div>

      <div className="p-4 rounded-xl border border-purple-100 bg-purple-50/30 space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <span className="text-[10px] font-bold text-purple-800 bg-purple-100 px-2.5 py-0.5 rounded-full">
              {hallTicket.semester}
            </span>
            <h4 className="font-bold text-xs text-gray-900 mt-1">{hallTicket.studentName} ({hallTicket.rollNo})</h4>
          </div>
          <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200 flex items-center gap-1">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" /> {hallTicket.attendanceClearance}
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs bg-white p-3 rounded-lg border border-gray-100">
          <div>
            <span className="text-gray-400">Exam Center:</span>
            <div className="font-semibold text-gray-800">{hallTicket.examCenter}</div>
          </div>
          <div>
            <span className="text-gray-400">Allocated Seat:</span>
            <div className="font-bold text-purple-700 font-mono">{hallTicket.seatNo}</div>
          </div>
        </div>

        <div className="flex items-center justify-between pt-1 border-t border-purple-100">
          <span className="font-mono text-[11px] text-gray-400">Hall Ticket ID: {hallTicket.ticketNo}</span>
          <button
            onClick={handleDownload}
            disabled={downloading}
            className="bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
          >
            {downloading ? <CheckCircle2 className="w-4 h-4 animate-spin" /> : <Download className="w-4 h-4" />}
            Download Hall Ticket PDF
          </button>
        </div>
      </div>
    </div>
  );
};
