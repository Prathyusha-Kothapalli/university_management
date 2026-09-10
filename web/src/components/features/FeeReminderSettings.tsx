import React, { useState } from 'react';
import { Bell, Mail, Phone, Clock, Save, CheckCircle } from 'lucide-react';

export const FeeReminderSettings: React.FC = () => {
  const [emailAlerts, setEmailAlerts] = useState(true);
  const [smsAlerts, setSmsAlerts] = useState(true);
  const [whatsappAlerts, setWhatsappAlerts] = useState(false);
  const [leadDays, setLeadDays] = useState<number>(7);
  const [saved, setSaved] = useState(false);

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    setSaved(true);
    setTimeout(() => setSaved(false), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-amber-50 text-amber-600 rounded-lg">
            <Bell className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Automated Fee Payment Reminders</h3>
            <p className="text-xs text-gray-500">Configure automated alert dispatch channels and reminder schedules</p>
          </div>
        </div>
        {saved && (
          <span className="text-xs text-emerald-600 font-semibold bg-emerald-50 px-2.5 py-1 rounded-full flex items-center gap-1 border border-emerald-100">
            <CheckCircle className="w-3.5 h-3.5" /> Preference Saved
          </span>
        )}
      </div>

      <form onSubmit={handleSave} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <label className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
            emailAlerts ? 'bg-amber-50/50 border-amber-200' : 'bg-gray-50 border-gray-100'
          }`}>
            <div className="flex items-center gap-2.5 text-xs font-semibold text-gray-800">
              <Mail className="w-4 h-4 text-amber-600" />
              Email Reminders
            </div>
            <input
              type="checkbox"
              checked={emailAlerts}
              onChange={e => setEmailAlerts(e.target.checked)}
              className="rounded text-amber-600 focus:ring-amber-500"
            />
          </label>

          <label className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
            smsAlerts ? 'bg-amber-50/50 border-amber-200' : 'bg-gray-50 border-gray-100'
          }`}>
            <div className="flex items-center gap-2.5 text-xs font-semibold text-gray-800">
              <Phone className="w-4 h-4 text-amber-600" />
              SMS Alerts
            </div>
            <input
              type="checkbox"
              checked={smsAlerts}
              onChange={e => setSmsAlerts(e.target.checked)}
              className="rounded text-amber-600 focus:ring-amber-500"
            />
          </label>

          <label className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
            whatsappAlerts ? 'bg-amber-50/50 border-amber-200' : 'bg-gray-50 border-gray-100'
          }`}>
            <div className="flex items-center gap-2.5 text-xs font-semibold text-gray-800">
              <Bell className="w-4 h-4 text-amber-600" />
              WhatsApp Digest
            </div>
            <input
              type="checkbox"
              checked={whatsappAlerts}
              onChange={e => setWhatsappAlerts(e.target.checked)}
              className="rounded text-amber-600 focus:ring-amber-500"
            />
          </label>
        </div>

        <div className="p-4 bg-gray-50 rounded-xl border border-gray-100 flex items-center justify-between">
          <div className="flex items-center gap-2 text-xs text-gray-700">
            <Clock className="w-4 h-4 text-amber-600" />
            <span>Send first reminder prior to due date:</span>
          </div>
          <select
            value={leadDays}
            onChange={e => setLeadDays(Number(e.target.value))}
            className="text-xs border border-gray-200 rounded-lg px-3 py-1.5 bg-white font-semibold focus:ring-2 focus:ring-amber-500"
          >
            <option value={3}>3 Days Before</option>
            <option value={7}>7 Days Before (Recommended)</option>
            <option value={14}>14 Days Before</option>
            <option value={30}>30 Days Before</option>
          </select>
        </div>

        <div className="flex justify-end">
          <button
            type="submit"
            className="bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 shadow-sm transition-colors"
          >
            <Save className="w-4 h-4" />
            Save Reminder Schedule
          </button>
        </div>
      </form>
    </div>
  );
};
