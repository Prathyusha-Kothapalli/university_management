import React, { useState } from 'react';
import { BookOpen, Download, Search, CheckCircle2 } from 'lucide-react';

interface Ebook {
  id: string;
  title: string;
  author: string;
  isbn: string;
  format: 'PDF e-Textbook' | 'EPUB Reader';
  downloaded: boolean;
}

export const DigitalLibraryEbooks: React.FC = () => {
  const [search, setSearch] = useState('');
  const [ebooks, setEbooks] = useState<Ebook[]>([
    { id: 'bk-101', title: 'Operating System Concepts (10th Edition)', author: 'Silberschatz, Galvin & Gagne', isbn: '978-1118063330', format: 'PDF e-Textbook', downloaded: false },
    { id: 'bk-102', title: 'Deep Learning with PyTorch & Python', author: 'Eli Stevens, Luca Antiga', isbn: '978-1617295263', format: 'PDF e-Textbook', downloaded: true },
    { id: 'bk-103', title: 'Database System Concepts (7th Edition)', author: 'Abraham Silberschatz', isbn: '978-0078022159', format: 'EPUB Reader', downloaded: false },
  ]);

  const toggleDownload = (id: string) => {
    setEbooks(ebooks.map(e => e.id === id ? { ...e, downloaded: true } : e));
  };

  const filtered = ebooks.filter(e => e.title.toLowerCase().includes(search.toLowerCase()) || e.author.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <BookOpen className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Digital Library E-Book & PDF Textbook Portal</h3>
            <p className="text-xs text-gray-500">Access 45,000+ digital textbooks, Wiley/IEEE engineering journals & DRM-free PDFs</p>
          </div>
        </div>
      </div>

      <div className="relative mb-4">
        <Search className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
        <input
          type="text"
          placeholder="Search eBooks by title, author or ISBN..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {filtered.map(bk => (
          <div key={bk.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex flex-col justify-between space-y-3">
            <div>
              <span className="text-[10px] font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded">
                {bk.format}
              </span>
              <h4 className="font-bold text-xs text-gray-900 mt-2 line-clamp-2">{bk.title}</h4>
              <p className="text-xs text-gray-500 mt-0.5">{bk.author}</p>
              <div className="text-[10px] font-mono text-gray-400 mt-1">ISBN: {bk.isbn}</div>
            </div>

            <button
              onClick={() => toggleDownload(bk.id)}
              className={`w-full py-2 text-xs font-semibold rounded-lg flex items-center justify-center gap-1.5 transition-all ${
                bk.downloaded
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-sm'
              }`}
            >
              {bk.downloaded ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Downloaded (Offline Available)
                </>
              ) : (
                <>
                  <Download className="w-3.5 h-3.5" /> Download e-Book
                </>
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
