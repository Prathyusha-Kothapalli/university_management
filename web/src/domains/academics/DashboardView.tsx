import React, { useState, useEffect } from 'react';
import { IAcademicsCoreEntity } from './types';

export const AcademicsDashboardView: React.FC = () => {
  const [entities, setEntities] = useState<IAcademicsCoreEntity[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [filter, setFilter] = useState<string>('');

  useEffect(() => {
    // Simulated data fetch for Academic & Curriculum Management
    setTimeout(() => {
      setEntities([
        {
          id: 1,
          entity_code: 'ACADEMICS_101',
          name: 'Primary Academic & Curriculum Management Entity',
          category: 'Core',
          description: 'Course catalog, syllabi, prerequisite trees, credit transfers, course scheduling, department catalogs, degree requirements, academic advisement.',
          status: 'ACTIVE',
          is_deleted: false,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        },
        {
          id: 2,
          entity_code: 'ACADEMICS_102',
          name: 'Secondary Academic & Curriculum Management Operations',
          category: 'Secondary',
          description: 'Operational tracking instance',
          status: 'ACTIVE',
          is_deleted: false,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        }
      ]);
      setLoading(false);
    }, 200);
  }, []);

  return (
    <div className="p-6 bg-slate-900 text-slate-100 min-h-screen">
      <header className="mb-8 flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-3xl font-bold text-indigo-400">Academic & Curriculum Management Command Center</h1>
          <p className="text-slate-400 text-sm mt-1">Course catalog, syllabi, prerequisite trees, credit transfers, course scheduling, department catalogs, degree requirements, academic advisement.</p>
        </div>
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Search records..."
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
            className="px-4 py-2 bg-slate-800 border border-slate-700 rounded-lg text-sm text-slate-200 focus:outline-none focus:border-indigo-500"
          />
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-sm font-medium transition-colors">
            + Add Academics Record
          </button>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-slate-800/80 border border-slate-700/50 p-5 rounded-xl">
          <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Total Entities</span>
          <h2 className="text-2xl font-bold text-white mt-2">{entities.length}</h2>
        </div>
        <div className="bg-slate-800/80 border border-slate-700/50 p-5 rounded-xl">
          <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Operational Status</span>
          <h2 className="text-2xl font-bold text-emerald-400 mt-2">100% Active</h2>
        </div>
        <div className="bg-slate-800/80 border border-slate-700/50 p-5 rounded-xl">
          <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Health Metric</span>
          <h2 className="text-2xl font-bold text-amber-400 mt-2">99.8%</h2>
        </div>
        <div className="bg-slate-800/80 border border-slate-700/50 p-5 rounded-xl">
          <span className="text-xs uppercase tracking-wider text-slate-400 font-semibold">Audit Events</span>
          <h2 className="text-2xl font-bold text-indigo-400 mt-2">1,240</h2>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #90</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-90 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #91</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-91 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #92</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-92 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #93</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-93 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #94</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-94 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #95</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-95 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #96</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-96 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #97</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-97 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #98</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-98 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #99</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-99 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #100</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-100 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #101</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-101 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #102</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-102 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #103</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-103 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #104</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-104 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #105</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-105 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #106</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-106 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #107</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-107 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #108</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-108 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Academic & Curriculum Management Record #109</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: ACADEMICS-REC-109 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-12 text-slate-400">Loading Academic & Curriculum Management data...</div>
      ) : (
        <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl overflow-hidden">
          <table className="w-full text-left text-sm text-slate-300">
            <thead className="bg-slate-800 text-slate-400 uppercase text-xs font-semibold">
              <tr>
                <th className="px-6 py-4">Code</th>
                <th className="px-6 py-4">Name</th>
                <th className="px-6 py-4">Category</th>
                <th className="px-6 py-4">Status</th>
                <th className="px-6 py-4">Created</th>
                <th className="px-6 py-4 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-700/50">
              {entities.map((item) => (
                <tr key={item.id} className="hover:bg-slate-800/80 transition-colors">
                  <td className="px-6 py-4 font-mono text-indigo-300 font-medium">{item.entity_code}</td>
                  <td className="px-6 py-4 font-semibold text-white">{item.name}</td>
                  <td className="px-6 py-4">{item.category}</td>
                  <td className="px-6 py-4">
                    <span className="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-full text-xs font-medium">
                      {item.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-slate-400">{new Date(item.created_at).toLocaleDateString()}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="text-indigo-400 hover:text-indigo-300 text-xs font-semibold">View Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default AcademicsDashboardView;
