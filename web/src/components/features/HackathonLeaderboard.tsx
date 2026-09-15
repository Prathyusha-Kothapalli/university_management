import React, { useState } from 'react';
import { Trophy, Star } from 'lucide-react';

interface Team {
  rank: number;
  teamName: string;
  projectName: string;
  category: string;
  score: number;
  prize: string;
  members: string;
}

export const HackathonLeaderboard: React.FC = () => {
  const [teams] = useState<Team[]>([
    { rank: 1, teamName: 'NeuralKnights', projectName: 'Autonomous Swarm Medical Drone Dispatch', category: 'AI for Healthcare', score: 98.4, prize: '🥇 1st Place (₹1,00,000)', members: 'Alex Morgan, Vikram Mehta' },
    { rank: 2, teamName: 'CyberVanguard', projectName: 'Zero-Knowledge Decentralized Identity Vault', category: 'Web3 & Security', score: 94.2, prize: '🥈 2nd Place (₹50,000)', members: 'Sameer Sen, Kavya Pillai' },
    { rank: 3, teamName: 'EcoGrid Tech', projectName: 'IoT Solar Microgrid Predictive Balancer', category: 'CleanEnergy', score: 91.0, prize: '🥉 3rd Place (₹25,000)', members: 'Sneha Kulkarni, Karthik Raja' },
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-amber-50 text-amber-600 rounded-lg">
            <Trophy className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">University Hackathon Leaderboard & Project Gallery</h3>
            <p className="text-xs text-gray-500">Live scoring leaderboard, jury evaluation matrix & project showcase gallery</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {teams.map(team => (
          <div
            key={team.rank}
            className={`p-4 rounded-xl border flex items-center justify-between transition-all ${
              team.rank === 1 ? 'bg-amber-50/50 border-amber-200' :
              team.rank === 2 ? 'bg-slate-50 border-slate-200' :
              'bg-orange-50/30 border-orange-100'
            }`}
          >
            <div className="flex items-center gap-3.5">
              <div className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-xs font-mono shrink-0 ${
                team.rank === 1 ? 'bg-amber-400 text-slate-950' :
                team.rank === 2 ? 'bg-slate-300 text-slate-900' :
                'bg-amber-700 text-white'
              }`}>
                #{team.rank}
              </div>

              <div>
                <div className="flex items-center gap-2">
                  <h4 className="font-bold text-xs text-gray-900">{team.teamName}</h4>
                  <span className="text-[10px] font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded-full">
                    {team.category}
                  </span>
                </div>
                <p className="text-xs text-gray-700 font-medium">{team.projectName}</p>
                <div className="text-[11px] text-gray-400">Team: {team.members}</div>
              </div>
            </div>

            <div className="text-right shrink-0">
              <div className="text-xs font-bold text-amber-800">{team.prize}</div>
              <div className="text-xs font-mono font-bold text-emerald-700 mt-0.5 flex items-center justify-end gap-0.5">
                <Star className="w-3.5 h-3.5 fill-emerald-500 text-emerald-500" /> {team.score} / 100
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
