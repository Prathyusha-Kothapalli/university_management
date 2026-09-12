import React, { useState } from 'react';
import { Palette, Check, Sparkles } from 'lucide-react';

interface ThemeColor {
  id: string;
  name: string;
  class: string;
  bgHex: string;
  ringClass: string;
}

export const ThemeAccentCustomizer: React.FC = () => {
  const [selectedTheme, setSelectedTheme] = useState<string>('indigo');

  const themes: ThemeColor[] = [
    { id: 'indigo', name: 'UniSphere Indigo', class: 'bg-indigo-600', bgHex: '#4f46e5', ringClass: 'ring-indigo-500' },
    { id: 'blue', name: 'Royal Blue', class: 'bg-blue-600', bgHex: '#2563eb', ringClass: 'ring-blue-500' },
    { id: 'emerald', name: 'Emerald Green', class: 'bg-emerald-600', bgHex: '#059669', ringClass: 'ring-emerald-500' },
    { id: 'purple', name: 'Deep Purple', class: 'bg-purple-600', bgHex: '#9333ea', ringClass: 'ring-purple-500' },
    { id: 'amber', name: 'Warm Amber', class: 'bg-amber-600', bgHex: '#d97706', ringClass: 'ring-amber-500' },
    { id: 'rose', name: 'Crimson Rose', class: 'bg-rose-600', bgHex: '#e11d48', ringClass: 'ring-rose-500' },
  ];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <Palette className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Dashboard Theme & Color Customizer</h3>
            <p className="text-xs text-gray-500">Personalize dashboard primary accent palette & high-contrast accessibility modes</p>
          </div>
        </div>
        <span className="text-xs text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-full font-semibold border border-indigo-100 flex items-center gap-1">
          <Sparkles className="w-3.5 h-3.5" /> Dynamic Theme
        </span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-3">
        {themes.map(t => (
          <button
            key={t.id}
            onClick={() => setSelectedTheme(t.id)}
            className={`p-3.5 rounded-xl border transition-all flex flex-col items-center gap-2 cursor-pointer ${
              selectedTheme === t.id
                ? `bg-gray-50 border-gray-300 ring-2 ${t.ringClass} shadow-sm`
                : 'bg-white border-gray-100 hover:border-gray-200'
            }`}
          >
            <div className={`w-8 h-8 rounded-full ${t.class} flex items-center justify-center text-white shadow-sm`}>
              {selectedTheme === t.id && <Check className="w-4 h-4" />}
            </div>
            <span className="text-xs font-semibold text-gray-800 text-center">{t.name}</span>
          </button>
        ))}
      </div>
    </div>
  );
};
