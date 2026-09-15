import React, { useState } from 'react';
import { Users, Search, MessageSquare, Briefcase, GraduationCap, CheckCircle } from 'lucide-react';

interface Alumnus {
  id: string;
  name: string;
  gradYear: number;
  company: string;
  designation: string;
  location: string;
  domain: string;
  avatarUrl: string;
  mentorshipAvailable: boolean;
}

export const AlumniDirectory: React.FC = () => {
  const [search, setSearch] = useState('');
  const [selectedDomain, setSelectedDomain] = useState('All');
  const [requestedId, setRequestedId] = useState<string | null>(null);

  const alumni: Alumnus[] = [
    {
      id: 'alm-1',
      name: 'Aditya Srivastava',
      gradYear: 2021,
      company: 'Microsoft',
      designation: 'Senior Cloud Solution Architect',
      location: 'Hyderabad / Seattle',
      domain: 'Cloud Computing & DevOps',
      avatarUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150',
      mentorshipAvailable: true
    },
    {
      id: 'alm-2',
      name: 'Pooja Sundaram',
      gradYear: 2022,
      company: 'Meta AI',
      designation: 'Machine Learning Engineer II',
      location: 'Bengaluru',
      domain: 'AI & Deep Learning',
      avatarUrl: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150',
      mentorshipAvailable: true
    },
    {
      id: 'alm-3',
      name: 'Rohan Deshmukh',
      gradYear: 2020,
      company: 'Uber',
      designation: 'Staff Backend Engineer',
      location: 'San Francisco',
      domain: 'Distributed Systems',
      avatarUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150',
      mentorshipAvailable: false
    }
  ];

  const filtered = alumni.filter(a => {
    const matchesSearch = a.name.toLowerCase().includes(search.toLowerCase()) || a.company.toLowerCase().includes(search.toLowerCase());
    const matchesDomain = selectedDomain === 'All' || a.domain === selectedDomain;
    return matchesSearch && matchesDomain;
  });

  const handleRequestMentorship = (id: string) => {
    setRequestedId(id);
    setTimeout(() => setRequestedId(null), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <Users className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Alumni Directory & Mentorship Connector</h3>
            <p className="text-xs text-gray-500">Connect with 1,200+ global alumni across tech, finance & research</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-4">
        <div className="md:col-span-2 relative">
          <Search className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search alumni by name, company (e.g. Google, Meta)..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
          />
        </div>

        <select
          value={selectedDomain}
          onChange={e => setSelectedDomain(e.target.value)}
          className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-indigo-500"
        >
          <option value="All">All Tech Domains</option>
          <option value="AI & Deep Learning">AI & Deep Learning</option>
          <option value="Cloud Computing & DevOps">Cloud Computing & DevOps</option>
          <option value="Distributed Systems">Distributed Systems</option>
        </select>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {filtered.map(person => (
          <div key={person.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex flex-col justify-between space-y-3">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <img
                  src={person.avatarUrl}
                  alt={person.name}
                  className="w-10 h-10 rounded-full object-cover border border-gray-200"
                />
                <div>
                  <h4 className="font-semibold text-xs text-gray-900">{person.name}</h4>
                  <span className="text-[10px] text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-full font-medium flex items-center gap-1 w-max mt-0.5">
                    <GraduationCap className="w-3 h-3" /> Class of {person.gradYear}
                  </span>
                </div>
              </div>

              <div className="space-y-1 text-xs text-gray-600">
                <div className="flex items-center gap-1.5 font-medium text-gray-800">
                  <Briefcase className="w-3.5 h-3.5 text-gray-400" />
                  {person.designation}
                </div>
                <div className="text-indigo-700 font-semibold">{person.company}</div>
                <div className="text-[11px] text-gray-400">{person.location}</div>
              </div>
            </div>

            <div className="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span className="text-[10px] text-gray-500">{person.domain}</span>
              {person.mentorshipAvailable ? (
                <button
                  onClick={() => handleRequestMentorship(person.id)}
                  className={`text-xs font-semibold px-3 py-1.5 rounded-lg flex items-center gap-1 transition-all ${
                    requestedId === person.id
                      ? 'bg-emerald-600 text-white'
                      : 'bg-indigo-600 hover:bg-indigo-700 text-white'
                  }`}
                >
                  {requestedId === person.id ? (
                    <>
                      <CheckCircle className="w-3.5 h-3.5" /> Request Sent
                    </>
                  ) : (
                    <>
                      <MessageSquare className="w-3.5 h-3.5" /> Request 1:1
                    </>
                  )}
                </button>
              ) : (
                <span className="text-[11px] text-gray-400 font-medium italic">Mentorship Full</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
