import React, { useState, useEffect } from "react";
import { IAcademicsItem1 } from "./types";

export const ResearchDashboardView: React.FC = () => {
  const [activeTab, setActiveTab] = useState<number>(1);
  const [search, setSearch] = useState<string>("");

  return (
    <div className="p-8 bg-slate-900 text-slate-100 min-h-screen font-sans">
      <header className="mb-8 border-b border-slate-800 pb-4">
        <h1 className="text-4xl font-extrabold text-indigo-400">Research, Grants & Lab Inventory</h1>
        <p className="text-slate-400 mt-2">Research project tracking, grant applications, lab equipment booking, patent filings, journal publication records, peer review management.</p>
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
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #1</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-1 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #2</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-2 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #3</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-3 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #4</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-4 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #5</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-5 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #6</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-6 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #7</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-7 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #8</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-8 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #9</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-9 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #10</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-10 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #11</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-11 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #12</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-12 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #13</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-13 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #14</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-14 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #15</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-15 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #16</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-16 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #17</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-17 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #18</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-18 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #19</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-19 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #20</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-20 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #21</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-21 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #22</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-22 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #23</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-23 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #24</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-24 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #25</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-25 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #26</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-26 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #27</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-27 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #28</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-28 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #29</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-29 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #30</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-30 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #31</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-31 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #32</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-32 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #33</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-33 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #34</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-34 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #35</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-35 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #36</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-36 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #37</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-37 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #38</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-38 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #39</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-39 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #40</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-40 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #41</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-41 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #42</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-42 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #43</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-43 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #44</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-44 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #45</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-45 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #46</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-46 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #47</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-47 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #48</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-48 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #49</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-49 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #50</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-50 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #51</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-51 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #52</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-52 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #53</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-53 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #54</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-54 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #55</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-55 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #56</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-56 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #57</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-57 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #58</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-58 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #59</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-59 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #60</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-60 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #61</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-61 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #62</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-62 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #63</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-63 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #64</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-64 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #65</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-65 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #66</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-66 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #67</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-67 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #68</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-68 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #69</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-69 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #70</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-70 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #71</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-71 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #72</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-72 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #73</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-73 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #74</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-74 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #75</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-75 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #76</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-76 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #77</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-77 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #78</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-78 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #79</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-79 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #80</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-80 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #81</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-81 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #82</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-82 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #83</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-83 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #84</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-84 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #85</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-85 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #86</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-86 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #87</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-87 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #88</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-88 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #89</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-89 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #90</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-90 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #91</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-91 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #92</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-92 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #93</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-93 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #94</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-94 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #95</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-95 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #96</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-96 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #97</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-97 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #98</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-98 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #99</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-99 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #100</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-100 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #101</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-101 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #102</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-102 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #103</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-103 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #104</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-104 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #105</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-105 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #106</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-106 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #107</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-107 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #108</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-108 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Research, Grants & Lab Inventory Record #109</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: RESEARCH-REC-109 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
      </div>
    </div>
  );
};

export default DashboardView;
