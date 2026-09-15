import React, { useState, useEffect } from "react";
import { IAcademicsItem1 } from "./types";

export const TransportDashboardView: React.FC = () => {
  const [activeTab, setActiveTab] = useState<number>(1);
  const [search, setSearch] = useState<string>("");

  return (
    <div className="p-8 bg-slate-900 text-slate-100 min-h-screen font-sans">
      <header className="mb-8 border-b border-slate-800 pb-4">
        <h1 className="text-4xl font-extrabold text-indigo-400">Transport & Fleet Logistics</h1>
        <p className="text-slate-400 mt-2">Fleet management, bus route mapping, driver rosters, real-time GPS tracking simulation, fuel logs, vehicle maintenance, route fee collection.</p>
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
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #1</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-1 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #2</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-2 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #3</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-3 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #4</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-4 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #5</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-5 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #6</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-6 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #7</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-7 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #8</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-8 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #9</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-9 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #10</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-10 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #11</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-11 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #12</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-12 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #13</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-13 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #14</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-14 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #15</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-15 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #16</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-16 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #17</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-17 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #18</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-18 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #19</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-19 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #20</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-20 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #21</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-21 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #22</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-22 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #23</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-23 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #24</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-24 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #25</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-25 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #26</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-26 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #27</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-27 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #28</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-28 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #29</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-29 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #30</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-30 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #31</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-31 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #32</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-32 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #33</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-33 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #34</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-34 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #35</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-35 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #36</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-36 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #37</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-37 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #38</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-38 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #39</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-39 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #40</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-40 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #41</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-41 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #42</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-42 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #43</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-43 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #44</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-44 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #45</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-45 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #46</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-46 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #47</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-47 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #48</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-48 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #49</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-49 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #50</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-50 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #51</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-51 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #52</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-52 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #53</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-53 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #54</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-54 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #55</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-55 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #56</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-56 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #57</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-57 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #58</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-58 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
        <div className="p-4 bg-slate-800/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <div>
            <h4 className="font-semibold text-slate-200">Transport & Fleet Logistics Record #59</h4>
            <p className="text-xs text-slate-400 mt-0.5">Code: TRANSPORT-REC-59 • Standard Allocation</p>
          </div>
          <button className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs font-semibold">Inspect</button>
        </div>
      </div>
    </div>
  );
};

export default DashboardView;
