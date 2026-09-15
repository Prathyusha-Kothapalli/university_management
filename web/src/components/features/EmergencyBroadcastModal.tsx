import React, { useState } from 'react';
import { AlertOctagon, Send, CheckCircle2, ShieldAlert } from 'lucide-react';

interface BroadcastAlert {
  id: string;
  title: string;
  category: 'Weather' | 'Security' | 'Academic Notice' | 'Maintenance';
  message: string;
  sentAt: string;
  targetAudience: string;
}

export const EmergencyBroadcastModal: React.FC = () => {
  const [alerts, setAlerts] = useState<BroadcastAlert[]>([
    {
      id: 'ALT-101',
      title: 'Heavy Rain Warning & Schedule Adjustment',
      category: 'Weather',
      message: 'Due to severe weather warnings in Hyderabad, all evening classes after 05:00 PM will transition to online Zoom sessions.',
      sentAt: 'Today, 02:15 PM',
      targetAudience: 'All Students, Faculty & Parents'
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [title, setTitle] = useState('');
  const [category, setCategory] = useState<BroadcastAlert['category']>('Weather');
  const [message, setMessage] = useState('');
  const [audience, setAudience] = useState('All Students & Faculty');
  const [dispatched, setDispatched] = useState(false);

  const handleBroadcast = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !message) return;

    const newAlert: BroadcastAlert = {
      id: `ALT-${Math.floor(100 + Math.random() * 900)}`,
      title,
      category,
      message,
      sentAt: 'Just Now',
      targetAudience: audience
    };

    setAlerts([newAlert, ...alerts]);
    setDispatched(true);
    setTimeout(() => {
      setDispatched(false);
      setShowModal(false);
      setTitle('');
      setMessage('');
    }, 2000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <AlertOctagon className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Emergency Broadcast & Campus Alert Center</h3>
            <p className="text-xs text-gray-500">One-click push broadcast for inclement weather, campus notices & emergency alerts</p>
          </div>
        </div>
        <button
          onClick={() => setShowModal(true)}
          className="bg-rose-600 hover:bg-rose-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <Send className="w-4 h-4" />
          New Campus Broadcast
        </button>
      </div>

      <div className="space-y-3">
        {alerts.map(a => (
          <div key={a.id} className="p-4 rounded-xl border border-rose-100 bg-rose-50/30 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-rose-700 bg-rose-100 px-2.5 py-0.5 rounded-full">
                  {a.category}
                </span>
                <h4 className="font-bold text-xs text-gray-900">{a.title}</h4>
              </div>
              <span className="text-[11px] text-gray-400 font-medium">{a.sentAt}</span>
            </div>
            <p className="text-xs text-gray-700">{a.message}</p>
            <div className="text-[11px] text-gray-500 italic">Target: {a.targetAudience}</div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <div className="flex items-center gap-2 text-rose-600">
              <ShieldAlert className="w-5 h-5" />
              <h3 className="font-semibold text-gray-900 text-sm">Issue Emergency Campus Alert</h3>
            </div>

            {dispatched ? (
              <div className="p-5 bg-emerald-50 text-emerald-800 rounded-xl text-center space-y-1 border border-emerald-100">
                <CheckCircle2 className="w-8 h-8 text-emerald-600 mx-auto mb-1" />
                <h4 className="font-bold text-xs">Emergency Broadcast Dispatched!</h4>
                <p className="text-[11px]">SMS, Email & Mobile Push notifications dispatched to {audience}.</p>
              </div>
            ) : (
              <form onSubmit={handleBroadcast} className="space-y-3">
                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Alert Headline / Title</label>
                  <input
                    type="text"
                    placeholder="e.g. Inclement Weather Alert"
                    value={title}
                    onChange={e => setTitle(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-rose-500 focus:outline-none"
                    required
                  />
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-medium text-gray-700 mb-1">Category</label>
                    <select
                      value={category}
                      onChange={e => setCategory(e.target.value as any)}
                      className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-rose-500"
                    >
                      <option value="Weather">Weather Notice</option>
                      <option value="Security">Security Advisory</option>
                      <option value="Academic Notice">Academic Notice</option>
                      <option value="Maintenance">Campus Maintenance</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-700 mb-1">Audience</label>
                    <select
                      value={audience}
                      onChange={e => setAudience(e.target.value)}
                      className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-rose-500"
                    >
                      <option value="All Students & Faculty">All Students & Faculty</option>
                      <option value="All Parents & Guardians">All Parents & Guardians</option>
                      <option value="Entire Campus Community">Entire Campus Community</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Broadcast Message</label>
                  <textarea
                    rows={3}
                    value={message}
                    onChange={e => setMessage(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-rose-500 focus:outline-none"
                    placeholder="Type urgent broadcast message..."
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
                    className="px-4 py-2 text-xs font-semibold bg-rose-600 hover:bg-rose-700 text-white rounded-lg flex items-center gap-1"
                  >
                    <Send className="w-3.5 h-3.5" />
                    Send Broadcast Now
                  </button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
