import React from "react";

export interface FundItem {
  id: string;
  fund_name: string;
  target_amount_usd: number;
  current_amount_usd: number;
  category: string;
}

interface EndowmentFundTrackerProps {
  funds: FundItem[];
}

export const EndowmentFundTracker: React.FC<EndowmentFundTrackerProps> = ({ funds }) => {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Institutional Endowment & Scholarship Funds</h3>
          <p className="text-sm text-slate-400">Track alumni contributions, target funding milestones, and active campaigns.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {funds.map((f) => {
          const progressPct = Math.min((f.current_amount_usd / f.target_amount_usd) * 100, 100);
          return (
            <div key={f.id} className="p-5 bg-slate-900/60 border border-slate-700/60 rounded-lg space-y-3">
              <div className="flex justify-between items-start">
                <div>
                  <span className="text-xs font-semibold uppercase tracking-wider text-indigo-400">{f.category}</span>
                  <h4 className="text-base font-semibold text-slate-100 mt-1">{f.fund_name}</h4>
                </div>
                <span className="px-2.5 py-0.5 text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full font-mono">
                  {progressPct.toFixed(1)}%
                </span>
              </div>

              {/* Progress bar */}
              <div className="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                <div
                  className="bg-gradient-to-r from-indigo-500 to-emerald-400 h-full transition-all duration-500"
                  style={{ width: `${progressPct}%` }}
                />
              </div>

              <div className="flex justify-between items-center text-xs font-mono">
                <span className="text-slate-400">Raised: <strong className="text-slate-100">${f.current_amount_usd.toLocaleString()}</strong></span>
                <span className="text-slate-400">Target: <strong className="text-indigo-300">${f.target_amount_usd.toLocaleString()}</strong></span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
