import React from 'react';
import { ISportsSubModule15State } from './types';

export const SportsSubWidget15: React.FC<{ data?: ISportsSubModule15State }> = ({ data }) => {
  return (
    <div className="p-4 bg-slate-800 rounded-lg border border-slate-700 mb-4">
      <h4 className="text-md font-semibold text-indigo-300">Sports & Extracurricular Activities Sub-Component #15</h4>
      <p className="text-xs text-slate-400 mt-1">Ref: {data?.reference_number || 'REF-15-DEFAULT'}</p>
      <div className="mt-3 flex justify-between text-xs text-slate-300">
        <span>Priority: {data?.priority || 15}</span>
        <span className="text-emerald-400">Active</span>
      </div>
    </div>
  );
};

export default SportsSubWidget15;
