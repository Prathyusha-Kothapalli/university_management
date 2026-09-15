import React, { useState } from "react";

export const SportsFormModal1: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #1</h2>
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

export const SportsFormModal2: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #2</h2>
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

export const SportsFormModal3: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #3</h2>
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

export const SportsFormModal4: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #4</h2>
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

export const SportsFormModal5: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #5</h2>
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

export const SportsFormModal6: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #6</h2>
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

export const SportsFormModal7: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #7</h2>
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

export const SportsFormModal8: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #8</h2>
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

export const SportsFormModal9: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #9</h2>
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

export const SportsFormModal10: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #10</h2>
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

export const SportsFormModal11: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #11</h2>
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

export const SportsFormModal12: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #12</h2>
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

export const SportsFormModal13: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #13</h2>
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

export const SportsFormModal14: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #14</h2>
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

export const SportsFormModal15: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #15</h2>
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

export const SportsFormModal16: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #16</h2>
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

export const SportsFormModal17: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #17</h2>
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

export const SportsFormModal18: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #18</h2>
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

export const SportsFormModal19: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #19</h2>
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

export const SportsFormModal20: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #20</h2>
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

export const SportsFormModal21: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #21</h2>
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

export const SportsFormModal22: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #22</h2>
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

export const SportsFormModal23: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #23</h2>
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

export const SportsFormModal24: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #24</h2>
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

export const SportsFormModal25: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #25</h2>
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

export const SportsFormModal26: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #26</h2>
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

export const SportsFormModal27: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #27</h2>
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

export const SportsFormModal28: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #28</h2>
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

export const SportsFormModal29: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #29</h2>
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

export const SportsFormModal30: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #30</h2>
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

export const SportsFormModal31: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #31</h2>
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

export const SportsFormModal32: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #32</h2>
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

export const SportsFormModal33: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #33</h2>
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

export const SportsFormModal34: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #34</h2>
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

export const SportsFormModal35: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #35</h2>
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

export const SportsFormModal36: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #36</h2>
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

export const SportsFormModal37: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #37</h2>
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

export const SportsFormModal38: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #38</h2>
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

export const SportsFormModal39: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #39</h2>
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

export const SportsFormModal40: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #40</h2>
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

export const SportsFormModal41: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #41</h2>
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

export const SportsFormModal42: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #42</h2>
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

export const SportsFormModal43: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #43</h2>
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

export const SportsFormModal44: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #44</h2>
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

export const SportsFormModal45: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #45</h2>
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

export const SportsFormModal46: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #46</h2>
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

export const SportsFormModal47: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #47</h2>
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

export const SportsFormModal48: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #48</h2>
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

export const SportsFormModal49: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #49</h2>
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

export const SportsFormModal50: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #50</h2>
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

export const SportsFormModal51: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #51</h2>
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

export const SportsFormModal52: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #52</h2>
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

export const SportsFormModal53: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #53</h2>
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

export const SportsFormModal54: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #54</h2>
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

export const SportsFormModal55: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #55</h2>
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

export const SportsFormModal56: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #56</h2>
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

export const SportsFormModal57: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #57</h2>
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

export const SportsFormModal58: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #58</h2>
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

export const SportsFormModal59: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #59</h2>
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

export const SportsFormModal60: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #60</h2>
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

export const SportsFormModal61: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #61</h2>
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

export const SportsFormModal62: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #62</h2>
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

export const SportsFormModal63: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #63</h2>
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

export const SportsFormModal64: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #64</h2>
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

export const SportsFormModal65: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #65</h2>
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

export const SportsFormModal66: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #66</h2>
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

export const SportsFormModal67: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #67</h2>
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

export const SportsFormModal68: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #68</h2>
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

export const SportsFormModal69: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #69</h2>
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

export const SportsFormModal70: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #70</h2>
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

export const SportsFormModal71: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #71</h2>
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

export const SportsFormModal72: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #72</h2>
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

export const SportsFormModal73: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #73</h2>
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

export const SportsFormModal74: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #74</h2>
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

export const SportsFormModal75: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #75</h2>
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

export const SportsFormModal76: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #76</h2>
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

export const SportsFormModal77: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #77</h2>
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

export const SportsFormModal78: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #78</h2>
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

export const SportsFormModal79: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #79</h2>
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

export const SportsFormModal80: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #80</h2>
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

export const SportsFormModal81: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #81</h2>
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

export const SportsFormModal82: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #82</h2>
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

export const SportsFormModal83: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #83</h2>
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

export const SportsFormModal84: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #84</h2>
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

export const SportsFormModal85: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #85</h2>
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

export const SportsFormModal86: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #86</h2>
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

export const SportsFormModal87: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #87</h2>
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

export const SportsFormModal88: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #88</h2>
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

export const SportsFormModal89: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #89</h2>
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

export const SportsFormModal90: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #90</h2>
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

export const SportsFormModal91: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #91</h2>
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

export const SportsFormModal92: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #92</h2>
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

export const SportsFormModal93: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #93</h2>
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

export const SportsFormModal94: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #94</h2>
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

export const SportsFormModal95: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #95</h2>
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

export const SportsFormModal96: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #96</h2>
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

export const SportsFormModal97: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #97</h2>
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

export const SportsFormModal98: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #98</h2>
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

export const SportsFormModal99: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #99</h2>
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

export const SportsFormModal100: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #100</h2>
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

export const SportsFormModal101: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #101</h2>
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

export const SportsFormModal102: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #102</h2>
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

export const SportsFormModal103: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #103</h2>
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

export const SportsFormModal104: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #104</h2>
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

export const SportsFormModal105: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #105</h2>
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

export const SportsFormModal106: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #106</h2>
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

export const SportsFormModal107: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #107</h2>
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

export const SportsFormModal108: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #108</h2>
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

export const SportsFormModal109: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #109</h2>
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

export const SportsFormModal110: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #110</h2>
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

export const SportsFormModal111: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #111</h2>
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

export const SportsFormModal112: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #112</h2>
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

export const SportsFormModal113: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #113</h2>
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

export const SportsFormModal114: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #114</h2>
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

export const SportsFormModal115: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #115</h2>
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

export const SportsFormModal116: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #116</h2>
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

export const SportsFormModal117: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #117</h2>
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

export const SportsFormModal118: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #118</h2>
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

export const SportsFormModal119: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #119</h2>
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

export const SportsFormModal120: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Sports & Extracurricular Activities Form #120</h2>
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

