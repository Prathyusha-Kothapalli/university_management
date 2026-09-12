import React, { useState } from 'react';
import { Rocket, PlusCircle, CheckCircle2 } from 'lucide-react';

interface Venture {
  id: string;
  name: string;
  category: 'AI / DeepTech' | 'CleanEnergy' | 'FinTech';
  fundingSanctioned: number;
  founders: string;
  incubationStage: 'Idea Proposal' | 'Prototypes & Seed Funded' | 'Incorporated Startup';
}

export const StartupIncubatorPortal: React.FC = () => {
  const [ventures, setVentures] = useState<Venture[]>([
    { id: 'vtr-101', name: 'NeuroDrone AI Labs', category: 'AI / DeepTech', fundingSanctioned: 500000, founders: 'Alex Morgan & Dr. Ananya Sharma', incubationStage: 'Prototypes & Seed Funded' },
    { id: 'vtr-102', name: 'SolarKinetic Grid Solutions', category: 'CleanEnergy', fundingSanctioned: 350000, founders: 'Vikram Mehta (Student)', incubationStage: 'Idea Proposal' },
  ]);

  const [showModal, setShowModal] = useState(false);
  const [name, setName] = useState('');
  const [category, setCategory] = useState<Venture['category']>('AI / DeepTech');
  const [founders, setFounders] = useState('');

  const handleApply = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !founders) return;

    const newVenture: Venture = {
      id: `vtr-${Math.floor(100 + Math.random() * 900)}`,
      name,
      category,
      fundingSanctioned: 250000,
      founders,
      incubationStage: 'Idea Proposal'
    };

    setVentures([newVenture, ...ventures]);
    setShowModal(false);
    setName('');
    setFounders('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-orange-50 text-orange-600 rounded-lg">
            <Rocket className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">University Startup Incubator & Seed Funding Portal</h3>
            <p className="text-xs text-gray-500">Submit student startup proposals, seed grant funding & mentor matching</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-orange-600 hover:bg-orange-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Apply for Seed Grant
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {ventures.map(v => (
          <div key={v.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold text-orange-700 bg-orange-100 px-2.5 py-0.5 rounded-full">
                {v.category}
              </span>
              <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-100 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> {v.incubationStage}
              </span>
            </div>

            <h4 className="font-bold text-xs text-gray-900">{v.name}</h4>
            <div className="text-xs text-gray-600">Founders: <strong>{v.founders}</strong></div>
            <div className="text-xs font-bold text-emerald-700 font-mono pt-1 border-t border-gray-100">
              Approved Seed Grant: ₹{v.fundingSanctioned.toLocaleString('en-IN')}
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Apply for University Startup Seed Grant</h3>
            <form onSubmit={handleApply} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Startup / Project Name</label>
                <input
                  type="text"
                  placeholder="e.g. HealthAI Assistant"
                  value={name}
                  onChange={e => setName(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-orange-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Domain Category</label>
                <select
                  value={category}
                  onChange={e => setCategory(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-orange-500"
                >
                  <option value="AI / DeepTech">AI / DeepTech / Robotics</option>
                  <option value="CleanEnergy">Clean Energy & Sustainability</option>
                  <option value="FinTech">FinTech & Web3</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Founder Names (Students/Faculty)</label>
                <input
                  type="text"
                  placeholder="e.g. Alex Morgan, Dr. Ananya Sharma"
                  value={founders}
                  onChange={e => setFounders(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-orange-500 focus:outline-none"
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
                  className="px-4 py-2 text-xs font-medium bg-orange-600 hover:bg-orange-700 text-white rounded-lg flex items-center gap-1"
                >
                  <Rocket className="w-3.5 h-3.5" /> Submit Proposal
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
