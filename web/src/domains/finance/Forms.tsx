import React, { useState } from "react";

export const FinanceFormModal1: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #1</h2>
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

export const FinanceFormModal2: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #2</h2>
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

export const FinanceFormModal3: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #3</h2>
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

export const FinanceFormModal4: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #4</h2>
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

export const FinanceFormModal5: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #5</h2>
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

export const FinanceFormModal6: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #6</h2>
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

export const FinanceFormModal7: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #7</h2>
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

export const FinanceFormModal8: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #8</h2>
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

export const FinanceFormModal9: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #9</h2>
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

export const FinanceFormModal10: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #10</h2>
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

export const FinanceFormModal11: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #11</h2>
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

export const FinanceFormModal12: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #12</h2>
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

export const FinanceFormModal13: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #13</h2>
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

export const FinanceFormModal14: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #14</h2>
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

export const FinanceFormModal15: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #15</h2>
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

export const FinanceFormModal16: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #16</h2>
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

export const FinanceFormModal17: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #17</h2>
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

export const FinanceFormModal18: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #18</h2>
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

export const FinanceFormModal19: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #19</h2>
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

export const FinanceFormModal20: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #20</h2>
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

export const FinanceFormModal21: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #21</h2>
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

export const FinanceFormModal22: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #22</h2>
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

export const FinanceFormModal23: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #23</h2>
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

export const FinanceFormModal24: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #24</h2>
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

export const FinanceFormModal25: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #25</h2>
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

export const FinanceFormModal26: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #26</h2>
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

export const FinanceFormModal27: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #27</h2>
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

export const FinanceFormModal28: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #28</h2>
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

export const FinanceFormModal29: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #29</h2>
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

export const FinanceFormModal30: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Finance, Billing & Payroll Form #30</h2>
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

