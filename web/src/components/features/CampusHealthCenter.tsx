import React, { useState } from 'react';
import { HeartPulse, Calendar, Clock, PlusCircle, CheckCircle2 } from 'lucide-react';

interface Appointment {
  id: string;
  doctorName: string;
  specialty: string;
  dateTime: string;
  status: 'Confirmed' | 'Completed';
  prescriptionAvailable: boolean;
}

export const CampusHealthCenter: React.FC = () => {
  const [appointments, setAppointments] = useState<Appointment[]>([
    {
      id: 'MED-901',
      doctorName: 'Dr. Suresh Kumar (MD General Physician)',
      specialty: 'Campus Wellness & OPD Clinic',
      dateTime: 'Tomorrow, 10:30 AM',
      status: 'Confirmed',
      prescriptionAvailable: true
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [doctorName, setDoctorName] = useState('Dr. Suresh Kumar (MD General Physician)');
  const [dateTime, setDateTime] = useState('Friday, 11:00 AM');

  const handleBook = (e: React.FormEvent) => {
    e.preventDefault();
    const newApp: Appointment = {
      id: `MED-${Math.floor(100 + Math.random() * 900)}`,
      doctorName,
      specialty: 'Campus Wellness Clinic',
      dateTime,
      status: 'Confirmed',
      prescriptionAvailable: false
    };

    setAppointments([newApp, ...appointments]);
    setShowModal(false);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <HeartPulse className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Campus Health Center & Digital OPD Vault</h3>
            <p className="text-xs text-gray-500">Book campus doctor appointments & view digital prescriptions/medical leave certificates</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-rose-600 hover:bg-rose-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Book OPD Appointment
        </button>
      </div>

      <div className="space-y-3">
        {appointments.map(app => (
          <div key={app.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <h4 className="font-bold text-xs text-gray-900">{app.doctorName}</h4>
                <span className="text-[10px] font-bold text-rose-700 bg-rose-100 px-2 py-0.5 rounded">
                  {app.specialty}
                </span>
              </div>
              <div className="flex items-center gap-3 text-xs text-gray-500">
                <span className="flex items-center gap-1">
                  <Calendar className="w-3.5 h-3.5 text-rose-600" /> {app.dateTime}
                </span>
              </div>
            </div>

            <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1.5 rounded-lg flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> {app.status}
            </span>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Schedule Campus Clinic Consultation</h3>
            <form onSubmit={handleBook} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Select Campus Medical Officer</label>
                <select
                  value={doctorName}
                  onChange={e => setDoctorName(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-rose-500"
                >
                  <option value="Dr. Suresh Kumar (MD General Physician)">Dr. Suresh Kumar (MD General Physician)</option>
                  <option value="Dr. Meenakshi Sundaram (Psychiatrist / Wellness Counsellor)">Dr. Meenakshi Sundaram (Wellness Counsellor)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Preferred Slot</label>
                <input
                  type="text"
                  value={dateTime}
                  onChange={e => setDateTime(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-rose-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-rose-600 hover:bg-rose-700 text-white rounded-lg flex items-center gap-1"
                >
                  <Clock className="w-3.5 h-3.5" /> Confirm Appointment
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
