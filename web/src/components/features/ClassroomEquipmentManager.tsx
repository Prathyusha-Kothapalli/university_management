import React, { useState } from 'react';
import { Wrench, PlusCircle, CheckCircle2, Clock, AlertTriangle } from 'lucide-react';

interface MaintenanceTicket {
  id: string;
  room: string;
  equipment: 'Projector & HDMI' | 'Smart Board / Stylus' | 'Air Conditioning' | 'Sound System';
  issueDescription: string;
  status: 'Technician Assigned' | 'Repaired & Verified';
}

export const ClassroomEquipmentManager: React.FC = () => {
  const [tickets, setTickets] = useState<MaintenanceTicket[]>([
    { id: 'EQ-401', room: 'Turing Hall (ATH-302)', equipment: 'Projector & HDMI', issueDescription: 'HDMI signal flicker during lecture presentation', status: 'Technician Assigned' },
    { id: 'EQ-402', room: 'Ada Lovelace Lab (ALB-105)', equipment: 'Air Conditioning', issueDescription: 'AC temperature control thermostat malfunction', status: 'Repaired & Verified' },
  ]);

  const [showModal, setShowModal] = useState(false);
  const [room, setRoom] = useState('');
  const [equipment, setEquipment] = useState<MaintenanceTicket['equipment']>('Projector & HDMI');
  const [issueDescription, setIssueDescription] = useState('');

  const handleReport = (e: React.FormEvent) => {
    e.preventDefault();
    if (!room || !issueDescription) return;

    const newTicket: MaintenanceTicket = {
      id: `EQ-${Math.floor(100 + Math.random() * 900)}`,
      room,
      equipment,
      issueDescription,
      status: 'Technician Assigned'
    };

    setTickets([newTicket, ...tickets]);
    setShowModal(false);
    setRoom('');
    setIssueDescription('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-amber-50 text-amber-600 rounded-lg">
            <Wrench className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Classroom AV & Smart Board Equipment Maintenance</h3>
            <p className="text-xs text-gray-500">Rapid fault reporting for lecture hall projectors, smart boards & AV systems</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Report Equipment Issue
        </button>
      </div>

      <div className="space-y-3">
        {tickets.map(t => (
          <div key={t.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="font-bold text-xs text-gray-900">{t.room}</span>
                <span className="text-[10px] font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded">
                  {t.equipment}
                </span>
              </div>
              <p className="text-xs text-gray-700">{t.issueDescription}</p>
            </div>

            <span className={`text-xs font-semibold px-3 py-1.5 rounded-lg flex items-center gap-1 shrink-0 ${
              t.status === 'Repaired & Verified' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-amber-50 text-amber-700 border border-amber-200'
            }`}>
              {t.status === 'Repaired & Verified' ? <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> : <Clock className="w-3.5 h-3.5 text-amber-600" />}
              {t.status}
            </span>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Report Classroom AV / Equipment Issue</h3>
            <form onSubmit={handleReport} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Lecture Hall / Lab Room</label>
                <input
                  type="text"
                  placeholder="e.g. ATH-302, Lab-3"
                  value={room}
                  onChange={e => setRoom(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Equipment Category</label>
                <select
                  value={equipment}
                  onChange={e => setEquipment(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-amber-500"
                >
                  <option value="Projector & HDMI">Projector & HDMI Cable</option>
                  <option value="Smart Board / Stylus">Smart Board / Stylus Pen</option>
                  <option value="Air Conditioning">Air Conditioning / HVAC</option>
                  <option value="Sound System">Mic & Speaker Sound System</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Issue Description</label>
                <input
                  type="text"
                  placeholder="Describe fault (e.g. No display output)"
                  value={issueDescription}
                  onChange={e => setIssueDescription(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-amber-600 hover:bg-amber-700 text-white rounded-lg flex items-center gap-1"
                >
                  <AlertTriangle className="w-3.5 h-3.5" /> Dispatch Technician
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
