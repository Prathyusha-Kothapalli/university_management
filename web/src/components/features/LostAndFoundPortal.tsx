import React, { useState } from 'react';
import { Package, PlusCircle, CheckCircle, MapPin, Tag } from 'lucide-react';

interface Item {
  id: string;
  title: string;
  category: 'Electronics' | 'IDs & Wallets' | 'Books & Stationery' | 'Accessories';
  location: string;
  dateFound: string;
  status: 'Unclaimed' | 'Claimed & Verified';
  finderName: string;
}

export const LostAndFoundPortal: React.FC = () => {
  const [items, setItems] = useState<Item[]>([
    { id: 'LF-881', title: 'Apple AirPods Pro in White Case', category: 'Electronics', location: 'Turing Hall - Desk 14', dateFound: '2026-09-08', status: 'Unclaimed', finderName: 'Security Desk Gate 1' },
    { id: 'LF-882', title: 'Blue Leather Wallet with Student ID', category: 'IDs & Wallets', location: 'Central Library 2nd Floor', dateFound: '2026-09-09', status: 'Claimed & Verified', finderName: 'Librarian Counter' },
  ]);

  const [showModal, setShowModal] = useState(false);
  const [title, setTitle] = useState('');
  const [category, setCategory] = useState<Item['category']>('Electronics');
  const [location, setLocation] = useState('');

  const handleReport = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !location) return;

    const newItem: Item = {
      id: `LF-${Math.floor(100 + Math.random() * 900)}`,
      title,
      category,
      location,
      dateFound: new Date().toISOString().split('T')[0],
      status: 'Unclaimed',
      finderName: 'Student Reporter'
    };

    setItems([newItem, ...items]);
    setShowModal(false);
    setTitle('');
    setLocation('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-amber-50 text-amber-600 rounded-lg">
            <Package className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Campus Lost & Found Portal</h3>
            <p className="text-xs text-gray-500">Report & claim misplaced belongings across lecture halls, labs & hostels</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <PlusCircle className="w-4 h-4" />
          Report Found Item
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {items.map(item => (
          <div key={item.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold text-amber-700 bg-amber-100 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                <Tag className="w-3 h-3" /> {item.category}
              </span>
              <span className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full ${
                item.status === 'Unclaimed' ? 'bg-amber-50 text-amber-800 border border-amber-200' : 'bg-emerald-50 text-emerald-800'
              }`}>
                {item.status}
              </span>
            </div>

            <h4 className="font-bold text-xs text-gray-900">{item.title}</h4>

            <div className="flex items-center justify-between text-xs text-gray-500 pt-1 border-t border-gray-100">
              <span className="flex items-center gap-1">
                <MapPin className="w-3.5 h-3.5 text-amber-600" /> {item.location}
              </span>
              <span className="text-[11px] text-gray-400">Found: {item.dateFound}</span>
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Report Misplaced / Found Item</h3>
            <form onSubmit={handleReport} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Item Name / Description</label>
                <input
                  type="text"
                  placeholder="e.g., Blue Casio Calculator, Black Leather Jacket"
                  value={title}
                  onChange={e => setTitle(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Category</label>
                <select
                  value={category}
                  onChange={e => setCategory(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-amber-500"
                >
                  <option value="Electronics">Electronics (Laptops, Earbuds, Chargers)</option>
                  <option value="IDs & Wallets">IDs, Wallets & Cards</option>
                  <option value="Books & Stationery">Books & Stationery</option>
                  <option value="Accessories">Keys & Personal Accessories</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Location Found / Left At</label>
                <input
                  type="text"
                  placeholder="e.g., Lab-3, Cafeteria Counter 2"
                  value={location}
                  onChange={e => setLocation(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-amber-500 focus:outline-none"
                  required
                />
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-xs text-gray-600 hover:bg-gray-100 rounded-lg"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-medium bg-amber-600 hover:bg-amber-700 text-white rounded-lg flex items-center gap-1"
                >
                  <CheckCircle className="w-3.5 h-3.5" /> Submit Item Report
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
