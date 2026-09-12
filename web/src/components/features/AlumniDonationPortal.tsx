import React, { useState } from 'react';
import { DollarSign, CheckCircle2, Heart } from 'lucide-react';

interface Donation {
  id: string;
  donorName: string;
  gradYear: number;
  company: string;
  amount: number;
  cause: 'Student Merit Scholarships' | 'AI Lab Hardware Upgrade' | 'Incubator Seed Fund';
}

export const AlumniDonationPortal: React.FC = () => {
  const [donations] = useState<Donation[]>([
    { id: 'don-1', donorName: 'Aditya Srivastava', gradYear: 2021, company: 'Microsoft', amount: 250000, cause: 'AI Lab Hardware Upgrade' },
    { id: 'don-2', donorName: 'Pooja Sundaram', gradYear: 2022, company: 'Meta AI', amount: 150000, cause: 'Student Merit Scholarships' },
  ]);

  const [donated, setDonated] = useState(false);

  const handleDonate = () => {
    setDonated(true);
    setTimeout(() => setDonated(false), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <Heart className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Alumni Endowment & Scholarship Sponsorship Portal</h3>
            <p className="text-xs text-gray-500">Alumni giving platform for sponsoring student scholarships & AI supercomputer labs</p>
          </div>
        </div>

        <button
          onClick={handleDonate}
          className="bg-rose-600 hover:bg-rose-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          {donated ? <CheckCircle2 className="w-4 h-4 text-white" /> : <DollarSign className="w-4 h-4" />}
          {donated ? 'Donation Received' : 'Sponsor a Cause'}
        </button>
      </div>

      <div className="space-y-3">
        {donations.map(d => (
          <div key={d.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div>
              <div className="flex items-center gap-2">
                <h4 className="font-bold text-xs text-gray-900">{d.donorName}</h4>
                <span className="text-[10px] text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-full font-semibold">
                  Class of {d.gradYear} ({d.company})
                </span>
              </div>
              <p className="text-xs text-gray-500 mt-0.5">Sponsored Cause: <strong>{d.cause}</strong></p>
            </div>

            <div className="font-bold text-sm text-emerald-700 font-mono shrink-0">
              ₹{d.amount.toLocaleString('en-IN')}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
