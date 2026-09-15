import React, { useState } from 'react';
import { UserCheck, Calendar, MapPin, CheckCircle } from 'lucide-react';

interface GuestLecture {
  id: string;
  topic: string;
  speaker: string;
  organization: string;
  dateTime: string;
  venue: string;
  status: 'Confirmed' | 'Completed';
}

export const GuestLectureManager: React.FC = () => {
  const [lectures] = useState<GuestLecture[]>([
    {
      id: 'GL-101',
      topic: 'Architecting Scalable LLM Pipelines in Production',
      speaker: 'Dr. Rahul Deshmukh',
      organization: 'Principal Scientist @ NVIDIA AI',
      dateTime: 'March 22, 2026 • 03:00 PM',
      venue: 'Main Auditorium',
      status: 'Confirmed'
    },
    {
      id: 'GL-102',
      topic: 'Quantum Computing Foundations & Qiskit Programming',
      speaker: 'Pooja Sundaram',
      organization: 'Staff Researcher @ IBM Quantum',
      dateTime: 'April 05, 2026 • 02:00 PM',
      venue: 'Turing Hall ATH-302',
      status: 'Confirmed'
    }
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-teal-50 text-teal-600 rounded-lg">
            <UserCheck className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Industry Guest Lecture & Tech Talk Manager</h3>
            <p className="text-xs text-gray-500">Industry leader keynotes, honorarium processing & student attendance logs</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {lectures.map(lec => (
          <div key={lec.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-teal-700 bg-teal-100 px-2.5 py-0.5 rounded-full">
                  {lec.organization}
                </span>
                <h4 className="font-bold text-xs text-gray-900">{lec.topic}</h4>
              </div>
              <span className="text-xs font-semibold text-teal-700 bg-teal-50 px-2.5 py-1 rounded-full border border-teal-100 flex items-center gap-1">
                <CheckCircle className="w-3.5 h-3.5 text-teal-600" /> {lec.status}
              </span>
            </div>

            <div className="text-xs text-gray-700">
              Keynote Speaker: <strong>{lec.speaker}</strong>
            </div>

            <div className="flex items-center gap-4 text-xs text-gray-500 pt-1 border-t border-gray-100">
              <span className="flex items-center gap-1">
                <Calendar className="w-3.5 h-3.5 text-teal-600" /> {lec.dateTime}
              </span>
              <span className="flex items-center gap-1">
                <MapPin className="w-3.5 h-3.5 text-teal-600" /> {lec.venue}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
