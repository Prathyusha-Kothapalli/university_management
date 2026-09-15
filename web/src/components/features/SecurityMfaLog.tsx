import React, { useState } from 'react';
import { ShieldCheck, Smartphone, Lock, SmartphoneNfc, Globe } from 'lucide-react';

interface Session {
  id: string;
  device: string;
  location: string;
  ip: string;
  lastActive: string;
  current: boolean;
}

export const SecurityMfaLog: React.FC = () => {
  const [mfaEnabled, setMfaEnabled] = useState(true);
  const [sessions, setSessions] = useState<Session[]>([
    { id: 'sess-1', device: 'Chrome on Windows 11 (Desktop)', location: 'Hyderabad, India', ip: '103.220.14.92', lastActive: 'Active now', current: true },
    { id: 'sess-2', device: 'UniSphere AI Mobile App (iOS 17)', location: 'Hyderabad, India', ip: '103.220.14.95', lastActive: '2 hours ago', current: false },
    { id: 'sess-3', device: 'Safari on macOS Sonoma', location: 'Bengaluru, India', ip: '49.207.198.11', lastActive: '3 days ago', current: false },
  ]);

  const handleRevoke = (id: string) => {
    setSessions(sessions.filter(s => s.id !== id));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <Lock className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Multi-Factor Authentication & Active Sessions</h3>
            <p className="text-xs text-gray-500">Manage 2FA security protocols, authenticator apps & login session logs</p>
          </div>
        </div>

        <label className="flex items-center gap-2 cursor-pointer bg-gray-50 px-3 py-1.5 rounded-lg border border-gray-200">
          <span className="text-xs font-semibold text-gray-700">2FA Status</span>
          <input
            type="checkbox"
            checked={mfaEnabled}
            onChange={e => setMfaEnabled(e.target.checked)}
            className="rounded text-rose-600 focus:ring-rose-500"
          />
        </label>
      </div>

      {mfaEnabled && (
        <div className="p-3.5 bg-emerald-50 border border-emerald-100 rounded-xl mb-4 flex items-center justify-between">
          <div className="flex items-center gap-2.5 text-xs text-emerald-800 font-medium">
            <ShieldCheck className="w-5 h-5 text-emerald-600 shrink-0" />
            <span>Two-Factor Authentication (TOTP Authenticator App) is active. Your account is secured.</span>
          </div>
          <button className="text-xs font-bold text-emerald-700 underline hover:text-emerald-800">
            View Recovery Keys
          </button>
        </div>
      )}

      <div className="space-y-3">
        <h4 className="text-xs font-semibold text-gray-800 flex items-center gap-1.5">
          <Globe className="w-4 h-4 text-rose-600" /> Active Login Sessions
        </h4>

        <div className="divide-y divide-gray-100 border border-gray-100 rounded-xl overflow-hidden">
          {sessions.map(sess => (
            <div key={sess.id} className="p-3.5 bg-white flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-gray-100 rounded-lg text-gray-600">
                  {sess.device.includes('Mobile') ? <SmartphoneNfc className="w-4 h-4" /> : <Smartphone className="w-4 h-4" />}
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-xs text-gray-900">{sess.device}</span>
                    {sess.current && (
                      <span className="text-[10px] bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded-full">
                        This Device
                      </span>
                    )}
                  </div>
                  <div className="text-[11px] text-gray-400 font-mono">
                    {sess.location} • IP: {sess.ip} • {sess.lastActive}
                  </div>
                </div>
              </div>

              {!sess.current && (
                <button
                  onClick={() => handleRevoke(sess.id)}
                  className="text-xs text-rose-600 hover:text-rose-700 font-semibold border border-rose-100 hover:bg-rose-50 px-3 py-1 rounded-lg transition-colors"
                >
                  Revoke Session
                </button>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
