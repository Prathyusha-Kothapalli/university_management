import React, { useState } from 'react';
import { Calculator, DollarSign, Calendar, ShieldCheck, CheckCircle2 } from 'lucide-react';

export const FeeInstallmentCalculator: React.FC = () => {
  const [totalFee, setTotalFee] = useState<number>(75000);
  const [planType, setPlanType] = useState<'2-step' | '3-step' | '4-step'>('3-step');
  const [agreed, setAgreed] = useState(false);
  const [applied, setApplied] = useState(false);

  const getInstallments = () => {
    let count = 3;
    if (planType === '2-step') count = 2;
    if (planType === '4-step') count = 4;

    const baseAmount = Math.round(totalFee / count);
    const result = [];
    const now = new Date();

    for (let i = 0; i < count; i++) {
      const dueDate = new Date(now.getFullYear(), now.getMonth() + i * 2, 15);
      result.push({
        installmentNo: i + 1,
        dueDate: dueDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        amount: i === count - 1 ? totalFee - baseAmount * (count - 1) : baseAmount,
        status: i === 0 ? 'Upcoming (15 Days)' : 'Scheduled'
      });
    }
    return result;
  };

  const installments = getInstallments();

  const handleApplyPlan = (e: React.FormEvent) => {
    e.preventDefault();
    setApplied(true);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Calculator className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Custom Fee Installment Calculator</h3>
            <p className="text-xs text-gray-500">Calculate customized bi-monthly & quarterly tuition payment schedules</p>
          </div>
        </div>
        <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-100 px-3 py-1 rounded-full">
          0% Interest Policy
        </span>
      </div>

      {applied ? (
        <div className="p-5 bg-emerald-50 border border-emerald-200 rounded-xl text-center space-y-3">
          <CheckCircle2 className="w-10 h-10 text-emerald-600 mx-auto" />
          <h4 className="font-bold text-gray-900">Installment Plan Approved!</h4>
          <p className="text-xs text-gray-600 max-w-md mx-auto">
            Your custom {planType} payment schedule of ₹{totalFee.toLocaleString('en-IN')} has been registered. Reminders will be dispatched 7 days prior to each due date.
          </p>
          <button
            onClick={() => setApplied(false)}
            className="text-xs text-emerald-700 font-semibold underline hover:text-emerald-800"
          >
            Modify Installment Setup
          </button>
        </div>
      ) : (
        <form onSubmit={handleApplyPlan} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Total Outstanding Fee (₹)</label>
              <div className="relative">
                <DollarSign className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
                <input
                  type="number"
                  value={totalFee}
                  onChange={e => setTotalFee(Number(e.target.value))}
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-none"
                  min="10000"
                  max="500000"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Preferred Installment Breakdown</label>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: '2-step', label: '2 Parts (50/50)' },
                  { id: '3-step', label: '3 Parts (33% ea)' },
                  { id: '4-step', label: '4 Parts (25% ea)' },
                ].map(p => (
                  <button
                    type="button"
                    key={p.id}
                    onClick={() => setPlanType(p.id as any)}
                    className={`py-2 px-1 text-xs font-medium rounded-lg border transition-all ${
                      planType === p.id
                        ? 'bg-emerald-50 text-emerald-700 border-emerald-300 shadow-sm font-semibold'
                        : 'bg-white text-gray-600 border-gray-200 hover:bg-gray-50'
                    }`}
                  >
                    {p.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Breakdown Preview Table */}
          <div className="border border-gray-100 rounded-xl overflow-hidden bg-gray-50/50">
            <div className="bg-gray-100/70 px-4 py-2 text-xs font-semibold text-gray-700 flex justify-between">
              <span>Installment #</span>
              <span>Due Date</span>
              <span>Amount (₹)</span>
              <span>Status</span>
            </div>
            <div className="divide-y divide-gray-100">
              {installments.map(inst => (
                <div key={inst.installmentNo} className="px-4 py-2.5 text-xs flex justify-between items-center bg-white">
                  <span className="font-semibold text-gray-800">Part {inst.installmentNo}</span>
                  <span className="text-gray-600 flex items-center gap-1">
                    <Calendar className="w-3.5 h-3.5 text-gray-400" />
                    {inst.dueDate}
                  </span>
                  <span className="font-bold text-gray-900 font-mono">₹{inst.amount.toLocaleString('en-IN')}</span>
                  <span className="bg-blue-50 text-blue-700 text-[11px] font-medium px-2 py-0.5 rounded-full">
                    {inst.status}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex items-center justify-between pt-2">
            <label className="flex items-center gap-2 text-xs text-gray-600 cursor-pointer">
              <input
                type="checkbox"
                checked={agreed}
                onChange={e => setAgreed(e.target.checked)}
                className="rounded border-gray-300 text-emerald-600 focus:ring-emerald-500"
              />
              <span className="flex items-center gap-1">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                I agree to adhere to the auto-generated installment payment schedule.
              </span>
            </label>

            <button
              type="submit"
              disabled={!agreed}
              className={`text-xs font-medium px-5 py-2 rounded-lg transition-all ${
                agreed
                  ? 'bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm'
                  : 'bg-gray-200 text-gray-400 cursor-not-allowed'
              }`}
            >
              Submit Installment Plan
            </button>
          </div>
        </form>
      )}
    </div>
  );
};
