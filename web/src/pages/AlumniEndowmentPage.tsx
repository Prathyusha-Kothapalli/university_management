import React, { useState } from "react";
import { EndowmentFundTracker, FundItem } from "../components/Alumni/EndowmentFundTracker";

export const AlumniEndowmentPage: React.FC = () => {
  const [funds] = useState<FundItem[]>([
    { id: "f1", fund_name: "AI & Quantum Computing Research Chair", target_amount_usd: 500000, current_amount_usd: 345000, category: "RESEARCH_CHAIR" },
    { id: "f2", fund_name: "Need-Based Merit Scholarship 2026", target_amount_usd: 200000, current_amount_usd: 185000, category: "SCHOLARSHIP" },
  ]);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Alumni Network & Endowment Funds</h1>
          <p className="text-slate-400 mt-1">Connect with alumni mentors, track endowment campaigns, and process donor gifts.</p>
        </div>
      </div>

      <EndowmentFundTracker funds={funds} />
    </div>
  );
};
