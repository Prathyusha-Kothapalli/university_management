import React from 'react';
import { Leaf, Sun, Droplets, Zap } from 'lucide-react';

export const SustainabilityDashboard: React.FC = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Leaf className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Eco-Campus Sustainability & Energy Dashboard</h3>
            <p className="text-xs text-gray-500">Real-time solar rooftop generation, water recycling & carbon footprint reduction metrics</p>
          </div>
        </div>

        <span className="text-xs font-bold text-emerald-800 bg-emerald-100 px-3 py-1 rounded-full border border-emerald-200">
          🌱 Net-Zero Target 2030
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div className="p-4 rounded-xl border border-gray-100 bg-emerald-50/30 flex items-center gap-3">
          <div className="p-2.5 bg-amber-100 text-amber-600 rounded-xl">
            <Sun className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-gray-500 font-semibold">Solar Rooftop Power</div>
            <div className="font-extrabold text-base text-gray-900 font-mono">420 kW/h</div>
            <div className="text-[11px] text-emerald-600 font-medium mt-0.5">64% of campus load</div>
          </div>
        </div>

        <div className="p-4 rounded-xl border border-gray-100 bg-emerald-50/30 flex items-center gap-3">
          <div className="p-2.5 bg-blue-100 text-blue-600 rounded-xl">
            <Droplets className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-gray-500 font-semibold">Recycled Water Use</div>
            <div className="font-extrabold text-base text-gray-900 font-mono">18,500 Liters/day</div>
            <div className="text-[11px] text-emerald-600 font-medium mt-0.5">Hostels & Lawns</div>
          </div>
        </div>

        <div className="p-4 rounded-xl border border-gray-100 bg-emerald-50/30 flex items-center gap-3">
          <div className="p-2.5 bg-emerald-100 text-emerald-600 rounded-xl">
            <Zap className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-gray-500 font-semibold">Carbon Offset</div>
            <div className="font-extrabold text-base text-gray-900 font-mono">14.2 Tons CO₂</div>
            <div className="text-[11px] text-emerald-600 font-medium mt-0.5">Saved this semester</div>
          </div>
        </div>
      </div>
    </div>
  );
};
