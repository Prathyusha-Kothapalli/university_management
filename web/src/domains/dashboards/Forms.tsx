import React, { useState } from "react";

export const DashboardsFormModal1: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #1</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal2: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #2</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal3: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #3</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal4: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #4</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal5: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #5</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal6: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #6</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal7: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #7</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal8: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #8</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal9: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #9</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal10: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #10</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal11: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #11</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal12: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #12</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal13: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #13</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal14: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #14</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal15: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #15</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal16: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #16</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal17: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #17</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal18: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #18</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal19: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #19</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal20: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #20</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal21: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #21</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal22: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #22</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal23: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #23</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal24: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #24</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal25: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #25</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal26: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #26</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal27: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #27</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal28: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #28</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal29: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #29</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

export const DashboardsFormModal30: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Executive & Departmental Dashboards Form #30</h2>
        <div className="mb-4">
          <label className="block text-xs font-semibold text-slate-400 mb-1">Entity Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded text-sm text-white focus:outline-none focus:border-indigo-500"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 bg-slate-700 text-slate-300 rounded text-xs font-semibold">Cancel</button>
          <button onClick={onClose} className="px-4 py-2 bg-indigo-600 text-white rounded text-xs font-semibold">Save</button>
        </div>
      </div>
    </div>
  );
};

