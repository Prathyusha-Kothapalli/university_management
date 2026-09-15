import React, { useState, useEffect } from "react";
import { IAcademicsItem1 } from "./types";

export const PlacementsDashboardView: React.FC = () => {
  const [activeTab, setActiveTab] = useState<number>(1);
  const [search, setSearch] = useState<string>("");

  return (
    <div className="p-8 bg-slate-900 text-slate-100 min-h-screen font-sans">
      <header className="mb-8 border-b border-slate-800 pb-4">
        <h1 className="text-4xl font-extrabold text-indigo-400">Placements & Alumni Network</h1>
        <p className="text-slate-400 mt-2">Company job postings, campus drive scheduling, student resume builder, interview feedback, placement metrics, alumni mentorship, donation portal.</p>
      </header>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl shadow-lg">
          <h3 className="text-xs uppercase font-semibold text-slate-400">Metric 1</h3>
          <p className="text-3xl font-bold text-indigo-300 mt-2">1,420</p>
        </div>
        <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl shadow-lg">
          <h3 className="text-xs uppercase font-semibold text-slate-400">Metric 2</h3>
          <p className="text-3xl font-bold text-indigo-300 mt-2">2,840</p>
        </div>
        <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl shadow-lg">
          <h3 className="text-xs uppercase font-semibold text-slate-400">Metric 3</h3>
          <p className="text-3xl font-bold text-indigo-300 mt-2">4,260</p>
        </div>
        <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl shadow-lg">
          <h3 className="text-xs uppercase font-semibold text-slate-400">Metric 4</h3>
          <p className="text-3xl font-bold text-indigo-300 mt-2">5,680</p>
        </div>
      </div>
      <div className="space-y-4">
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #1</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-1 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #2</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-2 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #3</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-3 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #4</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-4 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #5</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-5 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #6</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-6 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #7</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-7 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #8</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-8 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #9</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-9 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #10</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-10 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #11</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-11 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #12</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-12 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #13</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-13 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #14</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-14 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #15</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-15 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #16</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-16 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #17</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-17 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #18</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-18 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #19</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-19 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #20</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-20 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #21</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-21 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #22</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-22 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #23</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-23 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #24</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-24 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #25</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-25 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #26</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-26 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #27</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-27 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #28</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-28 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #29</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-29 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #30</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-30 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #31</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-31 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #32</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-32 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #33</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-33 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Placements & Alumni Network Record #34</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: PLACEMENTS-REC-34 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
      </div>
    </div>
  );
};

export default DashboardView;
