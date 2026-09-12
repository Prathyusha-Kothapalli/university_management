import React, { useState } from 'react';
import { BookOpen, CheckCircle, Circle, BarChart3 } from 'lucide-react';

interface Unit {
  id: number;
  title: string;
  topicsCompleted: number;
  totalTopics: number;
  completed: boolean;
}

interface CourseSyllabus {
  code: string;
  name: string;
  faculty: string;
  units: Unit[];
}

export const SyllabusTracker: React.FC = () => {
  const [courses, setCourses] = useState<CourseSyllabus[]>([
    {
      code: 'CS-401',
      name: 'Artificial Intelligence',
      faculty: 'Dr. Ananya Sharma',
      units: [
        { id: 1, title: 'Unit I: Search Strategies & Heuristics', topicsCompleted: 5, totalTopics: 5, completed: true },
        { id: 2, title: 'Unit II: Knowledge Representation & Logic', topicsCompleted: 4, totalTopics: 4, completed: true },
        { id: 3, title: 'Unit III: Machine Learning Foundations', topicsCompleted: 3, totalTopics: 4, completed: false },
        { id: 4, title: 'Unit IV: Deep Learning & Neural Networks', topicsCompleted: 1, totalTopics: 5, completed: false },
        { id: 5, title: 'Unit V: Natural Language Processing & Computer Vision', topicsCompleted: 0, totalTopics: 4, completed: false },
      ]
    },
    {
      code: 'CS-302',
      name: 'Data Structures & Algorithms',
      faculty: 'Prof. Rajesh Verma',
      units: [
        { id: 1, title: 'Unit I: Stacks, Queues & Arrays', topicsCompleted: 4, totalTopics: 4, completed: true },
        { id: 2, title: 'Unit II: Trees & Binary Search Trees', topicsCompleted: 4, totalTopics: 4, completed: true },
        { id: 3, title: 'Unit III: Graph Algorithms & Dynamic Programming', topicsCompleted: 5, totalTopics: 5, completed: true },
        { id: 4, title: 'Unit IV: Sorting & Searching Algorithms', topicsCompleted: 3, totalTopics: 3, completed: true },
        { id: 5, title: 'Unit V: Advanced Data Structures & Hashing', topicsCompleted: 2, totalTopics: 4, completed: false },
      ]
    }
  ]);

  const [activeCode, setActiveCode] = useState('CS-401');

  const activeCourse = courses.find(c => c.code === activeCode) || courses[0];

  const calculateProgress = (c: CourseSyllabus) => {
    const totalDone = c.units.reduce((acc, u) => acc + u.topicsCompleted, 0);
    const totalAll = c.units.reduce((acc, u) => acc + u.totalTopics, 0);
    return Math.round((totalDone / totalAll) * 100);
  };

  const toggleUnit = (unitId: number) => {
    setCourses(prev => prev.map(c => {
      if (c.code !== activeCode) return c;
      return {
        ...c,
        units: c.units.map(u => {
          if (u.id !== unitId) return u;
          const nextCompleted = !u.completed;
          return {
            ...u,
            completed: nextCompleted,
            topicsCompleted: nextCompleted ? u.totalTopics : 0
          };
        })
      };
    }));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <BookOpen className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Syllabus Progress & Unit Tracker</h3>
            <p className="text-xs text-gray-500">Track module completion and upcoming syllabus milestones</p>
          </div>
        </div>
        <div className="flex gap-2">
          {courses.map(c => (
            <button
              key={c.code}
              onClick={() => setActiveCode(c.code)}
              className={`px-3 py-1.5 text-xs font-semibold rounded-lg border transition-all ${
                activeCode === c.code
                  ? 'bg-emerald-600 text-white border-emerald-600 shadow-sm'
                  : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'
              }`}
            >
              {c.code} ({calculateProgress(c)}%)
            </button>
          ))}
        </div>
      </div>

      {/* Selected Course Header */}
      <div className="p-4 rounded-xl bg-gray-50 border border-gray-100 mb-4 space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <span className="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full mr-2">
              {activeCourse.code}
            </span>
            <span className="font-semibold text-sm text-gray-900">{activeCourse.name}</span>
            <span className="text-xs text-gray-500 ml-2">• Instructor: {activeCourse.faculty}</span>
          </div>
          <div className="flex items-center gap-1.5 text-emerald-600 font-bold text-sm">
            <BarChart3 className="w-4 h-4" />
            {calculateProgress(activeCourse)}% Completed
          </div>
        </div>

        {/* Progress Bar */}
        <div className="h-2.5 w-full bg-gray-200 rounded-full overflow-hidden">
          <div
            style={{ width: `${calculateProgress(activeCourse)}%` }}
            className="bg-emerald-500 h-full rounded-full transition-all duration-500"
          />
        </div>
      </div>

      {/* Units List */}
      <div className="space-y-2.5">
        {activeCourse.units.map(unit => (
          <div
            key={unit.id}
            onClick={() => toggleUnit(unit.id)}
            className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
              unit.completed
                ? 'bg-emerald-50/40 border-emerald-200 text-gray-900'
                : 'bg-white border-gray-100 hover:border-gray-200 text-gray-700'
            }`}
          >
            <div className="flex items-center gap-3">
              {unit.completed ? (
                <CheckCircle className="w-5 h-5 text-emerald-600 shrink-0" />
              ) : (
                <Circle className="w-5 h-5 text-gray-300 shrink-0" />
              )}
              <div>
                <h4 className={`text-xs font-semibold ${unit.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                  {unit.title}
                </h4>
                <p className="text-[11px] text-gray-500">
                  {unit.topicsCompleted} of {unit.totalTopics} sub-topics covered
                </p>
              </div>
            </div>
            <span className={`text-xs font-medium px-2.5 py-1 rounded-full ${
              unit.completed ? 'bg-emerald-100 text-emerald-800' : 'bg-gray-100 text-gray-600'
            }`}>
              {unit.completed ? 'Completed' : 'In Progress'}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
