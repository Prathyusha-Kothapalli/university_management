import React, { useState } from "react";

export const ExamsFormModal1: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #1</h2>
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

export const ExamsFormModal2: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #2</h2>
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

export const ExamsFormModal3: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #3</h2>
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

export const ExamsFormModal4: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #4</h2>
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

export const ExamsFormModal5: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #5</h2>
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

export const ExamsFormModal6: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #6</h2>
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

export const ExamsFormModal7: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #7</h2>
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

export const ExamsFormModal8: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #8</h2>
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

export const ExamsFormModal9: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #9</h2>
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

export const ExamsFormModal10: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #10</h2>
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

export const ExamsFormModal11: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #11</h2>
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

export const ExamsFormModal12: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #12</h2>
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

export const ExamsFormModal13: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #13</h2>
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

export const ExamsFormModal14: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #14</h2>
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

export const ExamsFormModal15: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #15</h2>
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

export const ExamsFormModal16: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #16</h2>
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

export const ExamsFormModal17: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #17</h2>
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

export const ExamsFormModal18: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #18</h2>
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

export const ExamsFormModal19: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #19</h2>
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

export const ExamsFormModal20: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #20</h2>
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

export const ExamsFormModal21: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #21</h2>
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

export const ExamsFormModal22: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #22</h2>
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

export const ExamsFormModal23: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #23</h2>
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

export const ExamsFormModal24: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #24</h2>
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

export const ExamsFormModal25: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #25</h2>
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

export const ExamsFormModal26: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #26</h2>
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

export const ExamsFormModal27: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #27</h2>
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

export const ExamsFormModal28: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #28</h2>
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

export const ExamsFormModal29: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #29</h2>
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

export const ExamsFormModal30: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #30</h2>
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

export const ExamsFormModal31: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #31</h2>
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

export const ExamsFormModal32: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #32</h2>
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

export const ExamsFormModal33: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #33</h2>
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

export const ExamsFormModal34: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #34</h2>
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

export const ExamsFormModal35: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #35</h2>
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

export const ExamsFormModal36: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #36</h2>
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

export const ExamsFormModal37: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #37</h2>
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

export const ExamsFormModal38: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #38</h2>
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

export const ExamsFormModal39: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #39</h2>
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

export const ExamsFormModal40: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #40</h2>
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

export const ExamsFormModal41: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #41</h2>
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

export const ExamsFormModal42: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #42</h2>
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

export const ExamsFormModal43: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #43</h2>
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

export const ExamsFormModal44: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #44</h2>
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

export const ExamsFormModal45: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #45</h2>
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

export const ExamsFormModal46: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #46</h2>
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

export const ExamsFormModal47: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #47</h2>
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

export const ExamsFormModal48: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #48</h2>
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

export const ExamsFormModal49: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #49</h2>
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

export const ExamsFormModal50: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #50</h2>
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

export const ExamsFormModal51: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #51</h2>
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

export const ExamsFormModal52: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #52</h2>
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

export const ExamsFormModal53: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #53</h2>
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

export const ExamsFormModal54: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #54</h2>
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

export const ExamsFormModal55: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #55</h2>
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

export const ExamsFormModal56: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #56</h2>
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

export const ExamsFormModal57: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #57</h2>
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

export const ExamsFormModal58: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #58</h2>
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

export const ExamsFormModal59: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #59</h2>
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

export const ExamsFormModal60: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #60</h2>
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

export const ExamsFormModal61: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #61</h2>
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

export const ExamsFormModal62: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #62</h2>
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

export const ExamsFormModal63: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #63</h2>
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

export const ExamsFormModal64: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #64</h2>
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

export const ExamsFormModal65: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #65</h2>
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

export const ExamsFormModal66: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #66</h2>
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

export const ExamsFormModal67: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #67</h2>
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

export const ExamsFormModal68: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #68</h2>
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

export const ExamsFormModal69: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #69</h2>
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

export const ExamsFormModal70: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #70</h2>
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

export const ExamsFormModal71: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #71</h2>
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

export const ExamsFormModal72: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #72</h2>
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

export const ExamsFormModal73: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #73</h2>
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

export const ExamsFormModal74: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #74</h2>
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

export const ExamsFormModal75: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #75</h2>
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

export const ExamsFormModal76: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #76</h2>
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

export const ExamsFormModal77: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #77</h2>
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

export const ExamsFormModal78: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #78</h2>
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

export const ExamsFormModal79: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #79</h2>
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

export const ExamsFormModal80: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #80</h2>
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

export const ExamsFormModal81: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #81</h2>
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

export const ExamsFormModal82: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #82</h2>
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

export const ExamsFormModal83: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #83</h2>
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

export const ExamsFormModal84: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #84</h2>
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

export const ExamsFormModal85: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #85</h2>
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

export const ExamsFormModal86: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #86</h2>
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

export const ExamsFormModal87: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #87</h2>
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

export const ExamsFormModal88: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #88</h2>
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

export const ExamsFormModal89: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #89</h2>
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

export const ExamsFormModal90: React.FC<{ isOpen: boolean; onClose: () => void }> = ({ isOpen, onClose }) => {
  const [name, setName] = useState("");
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div className="bg-slate-800 border border-slate-700 p-6 rounded-xl max-w-md w-full">
        <h2 className="text-xl font-bold text-white mb-4">Examinations & Result Management Form #90</h2>
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

