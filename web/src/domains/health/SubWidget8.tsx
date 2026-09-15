import React from 'react';
import { IHealthSubModule8State } from './types';

export const HealthSubWidget8: React.FC<{ data?: IHealthSubModule8State }> = ({ data }) => {
  return (
    <div className="p-4 bg-slate-800 rounded-lg border border-slate-700 mb-4">
      <h4 className="text-md font-semibold text-indigo-300">Campus Health & Clinic Management Sub-Component #8</h4>
      <p className="text-xs text-slate-400 mt-1">Ref: {data?.reference_number || 'REF-8-DEFAULT'}</p>
      <div className="mt-3 flex justify-between text-xs text-slate-300">
        <span>Priority: {data?.priority || 8}</span>
        <span className="text-emerald-400">Active</span>
      </div>
    </div>
  );
};

export default HealthSubWidget8;
