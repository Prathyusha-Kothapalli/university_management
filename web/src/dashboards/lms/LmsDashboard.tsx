import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Video, BookOpen, FileCheck, Users } from 'lucide-react';

export const LmsDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Video className="w-6 h-6 text-purple-400" /> Learning Management System (LMS)
        </h1>
        <p className="text-xs text-slate-400">Digital lecture repository, interactive quizzes, assignments & courseware</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Active Digital Courses" value="142 Courses" icon={<BookOpen className="w-5 h-5" />} />
        <StatCard title="Video Lectures Hosted" value="1,840 Hours" icon={<Video className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Quiz Submissions" value="12,400" icon={<FileCheck className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Daily Active Learners" value="3,920 Students" icon={<Users className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
      </div>
    </div>
  );
};
