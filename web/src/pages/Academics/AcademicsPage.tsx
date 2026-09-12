import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { academicsApi, timetableApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { Course, CourseOffering, Classroom, Timetable, AttendanceSession } from '../../types';
import { BookOpen, Calendar, MapPin, Plus, CheckSquare, AlertTriangle, FileText, CheckCircle2, UserPlus, Info, Network, Cpu, Star, Zap } from 'lucide-react';

export const AcademicsPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'courses' | 'offerings' | 'classrooms' | 'timetables' | 'attendance'>('courses');

  // Features State
  const [isLabModalOpen, setIsLabModalOpen] = useState(false);
  const [isOfficeHoursModalOpen, setIsOfficeHoursModalOpen] = useState(false);
  const [isFeedbackModalOpen, setIsFeedbackModalOpen] = useState(false);
  const [isOverloadModalOpen, setIsOverloadModalOpen] = useState(false);

  // Modal States
  const [isAddCourseModalOpen, setIsAddCourseModalOpen] = useState(false);
  const [newCourseCode, setNewCourseCode] = useState('');
  const [newCourseTitle, setNewCourseTitle] = useState('');
  const [newCourseCredits, setNewCourseCredits] = useState(4);

  // Feature 24: Peer Study Circle & Tutor Finder Modal State
  const [isStudyCircleModalOpen, setIsStudyCircleModalOpen] = useState(false);

  // Feature 2: Syllabus Modal
  const [selectedCourseForSyllabus, setSelectedCourseForSyllabus] = useState<Course | null>(null);

  // Feature 4: Classroom Specs Modal
  const [selectedClassroomForSpecs, setSelectedClassroomForSpecs] = useState<Classroom | null>(null);

  // Feature 5: Prerequisite Chain Modal
  const [selectedCourseForPrereqs, setSelectedCourseForPrereqs] = useState<Course | null>(null);

  // Attendance Logger Modal State
  const [isLogAttendanceModalOpen, setIsLogAttendanceModalOpen] = useState(false);
  const [sessionTopic, setSessionTopic] = useState('');
  const [sessionDate, setSessionDate] = useState(new Date().toISOString().split('T')[0]);

  // Queries
  const { data: courses = [], refetch: refetchCourses } = useFetch(academicsApi.getCourses);
  const { data: offerings = [] } = useFetch(academicsApi.getCourseOfferings);
  const { data: classrooms = [] } = useFetch(timetableApi.getClassrooms);
  const { data: timetables = [] } = useFetch(timetableApi.getTimetables);
  const { data: sessions = [], refetch: refetchSessions } = useFetch(timetableApi.getAttendanceSessions);

  const handleCreateCourse = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Successfully created course ${newCourseCode}: ${newCourseTitle}`, 'success');
    setIsAddCourseModalOpen(false);
    setNewCourseCode('');
    setNewCourseTitle('');
    refetchCourses();
  };

  const handleLogAttendanceSession = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Logged attendance session for "${sessionTopic}" on ${sessionDate}`, 'success');
    setIsLogAttendanceModalOpen(false);
    setSessionTopic('');
    refetchSessions();
  };

  // Feature 3: Register / Enroll in Course Section
  const handleEnrollSection = (offering: CourseOffering) => {
    showToast(`Enrolled in Course Offering ${offering.id} (${offering.section_name})`, 'success');
  };

  const courseColumns: Column<Course>[] = [
    { header: 'Code', accessorKey: 'course_code', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.course_code}</strong> },
    { header: 'Title', accessorKey: 'title' },
    { header: 'Credits', accessorKey: 'credits', cell: (r) => <span>{r.credits} Credits</span> },
    { header: 'Description', accessorKey: 'description' },
  ];

  const offeringColumns: Column<CourseOffering>[] = [
    { header: 'Offering ID', accessorKey: 'id', cell: (r) => <span style={{ color: '#a855f7' }}>{r.id}</span> },
    { header: 'Section', accessorKey: 'section_name' },
    { header: 'Capacity', accessorKey: 'max_capacity' },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#10b981', fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  const classroomColumns: Column<Classroom>[] = [
    { header: 'Building', accessorKey: 'building_name' },
    { header: 'Room No.', accessorKey: 'room_number', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.room_number}</strong> },
    { header: 'Type', accessorKey: 'type' },
    { header: 'Capacity', accessorKey: 'capacity', cell: (r) => <span>{r.capacity} seats</span> },
  ];

  const timetableColumns: Column<Timetable>[] = [
    { header: 'Day', accessorKey: 'day_of_week', cell: (r) => <strong>{r.day_of_week}</strong> },
    { header: 'Start Time', accessorKey: 'start_time' },
    { header: 'End Time', accessorKey: 'end_time' },
    { header: 'Classroom ID', accessorKey: 'classroom_id' },
  ];

  const sessionColumns: Column<AttendanceSession>[] = [
    { header: 'Session Date', accessorKey: 'session_date', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.session_date}</strong> },
    { header: 'Lecture Topic', accessorKey: 'topic' },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#10b981', fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Academics & Course Management
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 3 & 4 API integration (`/api/v1/courses/`, `/api/v1/classrooms/`, `/api/v1/timetables/`, `/api/v1/attendance-sessions/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="outline" icon={<Zap size={16} />} onClick={() => setIsOverloadModalOpen(true)}>
            Credit Overload Waiver
          </Button>
          <Button variant="outline" icon={<Cpu size={16} />} onClick={() => setIsLabModalOpen(true)}>
            Lab Equipment Booking
          </Button>
          <Button variant="outline" icon={<UserPlus size={16} />} onClick={() => setIsOfficeHoursModalOpen(true)}>
            Faculty Office Hours
          </Button>
          <Button variant="outline" icon={<Star size={16} />} onClick={() => setIsFeedbackModalOpen(true)}>
            Course Feedback Survey
          </Button>
          <Button variant="secondary" icon={<CheckSquare size={16} />} onClick={() => setIsLogAttendanceModalOpen(true)}>
            Record Attendance
          </Button>
          <Button variant="primary" icon={<Plus size={16} />} onClick={() => setIsAddCourseModalOpen(true)}>
            Add Course
          </Button>
        </div>
      </div>

      {/* Attendance Eligibility Alert Banner */}
      <div style={{ padding: '1rem 1.25rem', background: 'rgba(245, 158, 11, 0.12)', border: '1px solid rgba(245, 158, 11, 0.3)', borderRadius: '12px', display: 'flex', alignItems: 'center', gap: '12px' }}>
        <AlertTriangle size={20} style={{ color: '#f59e0b', flexShrink: 0 }} />
        <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
          <strong style={{ color: '#f59e0b' }}>Attendance Eligibility Policy:</strong> Minimum 75% attendance required in each enrolled course offering to qualify for Spring 2026 End-Semester Examinations.
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'courses', label: 'Courses Catalog', icon: <BookOpen size={16} /> },
          { id: 'offerings', label: 'Course Offerings', icon: <Calendar size={16} /> },
          { id: 'classrooms', label: 'Classrooms & Labs', icon: <MapPin size={16} /> },
          { id: 'timetables', label: 'Timetable Schedules', icon: <Calendar size={16} /> },
          { id: 'attendance', label: 'Attendance Sessions', icon: <CheckSquare size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '8px 16px',
              borderRadius: '8px',
              border: activeTab === tab.id ? '1px solid rgba(56, 189, 248, 0.4)' : 'none',
              background: activeTab === tab.id ? 'rgba(37, 99, 235, 0.2)' : 'transparent',
              color: activeTab === tab.id ? '#38bdf8' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Data Table Content */}
      <Card>
        {activeTab === 'courses' && (
          <DataTable
            columns={courseColumns}
            data={courses || []}
            searchPlaceholder="Search course code or title..."
            actions={(row) => (
              <div style={{ display: 'flex', gap: '6px' }}>
                <Button variant="outline" size="sm" icon={<FileText size={14} />} onClick={() => setSelectedCourseForSyllabus(row)}>
                  Syllabus
                </Button>
                <Button variant="ghost" size="sm" icon={<Network size={14} />} onClick={() => setSelectedCourseForPrereqs(row)}>
                  Prereqs
                </Button>
              </div>
            )}
          />
        )}
        {activeTab === 'offerings' && (
          <DataTable
            columns={offeringColumns}
            data={offerings || []}
            searchPlaceholder="Search course offerings..."
            actions={(row) => (
              <Button variant="primary" size="sm" icon={<UserPlus size={14} />} onClick={() => handleEnrollSection(row)}>
                Enroll Section
              </Button>
            )}
          />
        )}
        {activeTab === 'classrooms' && (
          <DataTable
            columns={classroomColumns}
            data={classrooms || []}
            searchPlaceholder="Search classrooms..."
            actions={(row) => (
              <Button variant="outline" size="sm" icon={<Info size={14} />} onClick={() => setSelectedClassroomForSpecs(row)}>
                View Specs
              </Button>
            )}
          />
        )}
        {activeTab === 'timetables' && <DataTable columns={timetableColumns} data={timetables || []} searchPlaceholder="Search timetables..." />}
        {activeTab === 'attendance' && <DataTable columns={sessionColumns} data={sessions || []} searchPlaceholder="Search lecture sessions..." />}
      </Card>

      {/* Feature 2: Course Syllabus Modal */}
      <Modal
        isOpen={!!selectedCourseForSyllabus}
        onClose={() => setSelectedCourseForSyllabus(null)}
        title={`Course Syllabus & Learning Outcomes: ${selectedCourseForSyllabus?.course_code || ''}`}
      >
        {selectedCourseForSyllabus && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <h3 style={{ margin: 0, color: '#38bdf8' }}>{selectedCourseForSyllabus.title} ({selectedCourseForSyllabus.credits} Credits)</h3>
            <p style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>{selectedCourseForSyllabus.description}</p>

            <div style={{ padding: '1rem', background: 'rgba(255,255,255,0.03)', borderRadius: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#a855f7' }}>Module Weekly Outline:</div>
              <div style={{ fontSize: '0.8rem', color: '#cbd5e1', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <CheckCircle2 size={14} style={{ color: '#10b981' }} /> Weeks 1-4: Mathematical Foundations & Linear Algebra
              </div>
              <div style={{ fontSize: '0.8rem', color: '#cbd5e1', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <CheckCircle2 size={14} style={{ color: '#10b981' }} /> Weeks 5-8: Deep Learning Architectures & CNNs
              </div>
              <div style={{ fontSize: '0.8rem', color: '#cbd5e1', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <CheckCircle2 size={14} style={{ color: '#10b981' }} /> Weeks 9-12: Attention Layers & Distributed Training
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <Button variant="primary" onClick={() => setSelectedCourseForSyllabus(null)}>Close Syllabus</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Feature 4: Classroom Specs Modal */}
      <Modal
        isOpen={!!selectedClassroomForSpecs}
        onClose={() => setSelectedClassroomForSpecs(null)}
        title={`Classroom Facility Specs: Room ${selectedClassroomForSpecs?.room_number || ''}`}
      >
        {selectedClassroomForSpecs && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', fontSize: '0.85rem' }}>
            <div style={{ padding: '1rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '10px' }}>
              <h4 style={{ margin: 0, color: '#38bdf8' }}>{selectedClassroomForSpecs.building_name} ({selectedClassroomForSpecs.type})</h4>
              <p style={{ margin: '4px 0 0 0', color: '#cbd5e1' }}>Total Seating Capacity: {selectedClassroomForSpecs.capacity} students</p>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ color: '#e2e8f0' }}>✔ 4K Laser Projection System & Interactive Whiteboard</div>
              <div style={{ color: '#e2e8f0' }}>✔ Dual Surround Sound Microphones & Lecture Capture Recording</div>
              <div style={{ color: '#e2e8f0' }}>✔ Gigabit High-Speed Wi-Fi 6 Access Points</div>
              <div style={{ color: '#e2e8f0' }}>✔ Central Climate-Controlled HVAC</div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <Button variant="primary" onClick={() => setSelectedClassroomForSpecs(null)}>Close</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Feature 5: Prerequisite Chain Modal */}
      <Modal
        isOpen={!!selectedCourseForPrereqs}
        onClose={() => setSelectedCourseForPrereqs(null)}
        title={`Prerequisite Chain: ${selectedCourseForPrereqs?.course_code || ''}`}
      >
        {selectedCourseForPrereqs && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
              Required prerequisite courses before enrolling in <strong>{selectedCourseForPrereqs.title}</strong>:
            </div>

            <div style={{ padding: '1rem', background: 'rgba(255,255,255,0.03)', borderRadius: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#10b981', fontSize: '0.85rem', fontWeight: 600 }}>
                <span>1. CS101 Introduction to Programming (Python)</span>
                <span>COMPLETED (Grade A)</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#10b981', fontSize: '0.85rem', fontWeight: 600 }}>
                <span>2. MATH201 Linear Algebra & Probability</span>
                <span>COMPLETED (Grade A)</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#38bdf8', fontSize: '0.85rem', fontWeight: 600 }}>
                <span>3. CS204 Database Management Systems</span>
                <span>ENROLLED (Spring 2026)</span>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <Button variant="primary" onClick={() => setSelectedCourseForPrereqs(null)}>Close</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Add Course Modal */}
      <Modal
        isOpen={isAddCourseModalOpen}
        onClose={() => setIsAddCourseModalOpen(false)}
        title="Add New University Course"
      >
        <form onSubmit={handleCreateCourse} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Course Code</label>
            <input
              type="text"
              required
              placeholder="e.g. CS404"
              value={newCourseCode}
              onChange={(e) => setNewCourseCode(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Course Title</label>
            <input
              type="text"
              required
              placeholder="e.g. Autonomous Robotics & Vision"
              value={newCourseTitle}
              onChange={(e) => setNewCourseTitle(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Credits</label>
            <input
              type="number"
              min={1}
              max={6}
              value={newCourseCredits}
              onChange={(e) => setNewCourseCredits(Number(e.target.value))}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsAddCourseModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Create Course</Button>
          </div>
        </form>
      </Modal>

      {/* Record Attendance Session Modal */}
      <Modal
        isOpen={isLogAttendanceModalOpen}
        onClose={() => setIsLogAttendanceModalOpen(false)}
        title="Record Lecture Attendance Session"
      >
        <form onSubmit={handleLogAttendanceSession} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Session Date</label>
            <input
              type="date"
              required
              value={sessionDate}
              onChange={(e) => setSessionDate(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Lecture Topic</label>
            <input
              type="text"
              required
              placeholder="e.g. Multi-Head Self Attention & QKV Projections"
              value={sessionTopic}
              onChange={(e) => setSessionTopic(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsLogAttendanceModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Save Session Log</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 24: Peer-to-Peer Study Circles & Tutor Finder Modal */}
      <Modal
        isOpen={isStudyCircleModalOpen}
        onClose={() => setIsStudyCircleModalOpen(false)}
        title="Peer Study Circles & Accredited Student Tutors"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
            Connect with active course study groups or book 1-on-1 peer tutoring sessions:
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {/* Circle 1 */}
            <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <strong style={{ color: '#f8fafc', fontSize: '0.9rem' }}>CS301 Machine Learning Midterm Circle</strong>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>6 Members • Meets Tuesdays @ Science Library Room 204</div>
              </div>
              <Button variant="primary" size="sm" onClick={() => showToast('Joined CS301 Machine Learning Study Circle!', 'success')}>
                Join Circle
              </Button>
            </div>

            {/* Tutor 1 */}
            <div style={{ padding: '0.85rem 1rem', background: 'rgba(168,85,247,0.1)', border: '1px solid rgba(168,85,247,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <strong style={{ color: '#f8fafc', fontSize: '0.9rem' }}>Sophia Chen (Teaching Assistant • 4.95★)</strong>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Specialty: Linear Algebra & Matrix Calculus • Free Peer Session</div>
              </div>
              <Button variant="outline" size="sm" onClick={() => showToast('Booked 1-on-1 tutoring slot with Sophia Chen!', 'success')}>
                Book Session
              </Button>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
            <Button variant="primary" onClick={() => setIsStudyCircleModalOpen(false)}>Done</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 6: Lab Equipment Reservation Modal */}
      <Modal
        isOpen={isLabModalOpen}
        onClose={() => setIsLabModalOpen(false)}
        title="Engineering & AI Hardware Lab Reservation"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#38bdf8', fontSize: '0.9rem' }}>NVIDIA H100 AI Compute Node Bench #4</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>High-Performance Deep Learning Lab • 4-Hour Time Slot</div>
            </div>
            <Button variant="primary" size="sm" onClick={() => { showToast('Reserved H100 GPU Workstation Slot for 4 hours!', 'success'); setIsLabModalOpen(false); }}>
              Reserve Slot
            </Button>
          </div>

          <div style={{ padding: '0.85rem 1rem', background: 'rgba(16,185,129,0.1)', border: '1px solid rgba(16,185,129,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#10b981', fontSize: '0.9rem' }}>Embedded Systems Robotics Oscilloscope Kit</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Hardware Lab Room 102 • Kit #12</div>
            </div>
            <Button variant="outline" size="sm" onClick={() => { showToast('Reserved Oscilloscope Kit #12!', 'success'); setIsLabModalOpen(false); }}>
              Reserve Kit
            </Button>
          </div>
        </div>
      </Modal>

      {/* Feature 7: Faculty Office Hours Booking Modal */}
      <Modal
        isOpen={isOfficeHoursModalOpen}
        onClose={() => setIsOfficeHoursModalOpen(false)}
        title="Book 1-on-1 Faculty Advisory Office Hours"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(168,85,247,0.1)', border: '1px solid rgba(168,85,247,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#c084fc', fontSize: '0.9rem' }}>Prof. Alan Turing (Machine Learning Chair)</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Wednesdays 02:00 PM – 04:00 PM • Turing Hall 304</div>
            </div>
            <Button variant="primary" size="sm" onClick={() => { showToast('Booked office hours meeting with Prof. Alan Turing!', 'success'); setIsOfficeHoursModalOpen(false); }}>
              Book Slot
            </Button>
          </div>
        </div>
      </Modal>

      {/* Feature 8: Course Feedback Survey Modal */}
      <Modal
        isOpen={isFeedbackModalOpen}
        onClose={() => setIsFeedbackModalOpen(false)}
        title="Spring 2026 Anonymous Course Teaching Survey"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Course Teaching Rating</label>
            <select style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}>
              <option>★★★★★ (5/5) Excellent Course Quality & Instruction</option>
              <option>★★★★☆ (4/5) Very Good</option>
              <option>★★★☆☆ (3/5) Average</option>
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Qualitative Suggestions</label>
            <textarea rows={3} placeholder="Share constructive feedback for instructor..." style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
            <Button variant="ghost" onClick={() => setIsFeedbackModalOpen(false)}>Cancel</Button>
            <Button variant="primary" onClick={() => { showToast('Submitted anonymous course feedback survey!', 'success'); setIsFeedbackModalOpen(false); }}>Submit Survey</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 53: Course Credit Overload Waiver Modal */}
      <Modal
        isOpen={isOverloadModalOpen}
        onClose={() => setIsOverloadModalOpen(false)}
        title="Apply for Semester Academic Credit Overload Waiver"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(37,99,235,0.1)', borderRadius: '10px', border: '1px solid rgba(56,189,248,0.3)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Current Cumulative GPA</div>
              <strong style={{ fontSize: '1.2rem', color: '#38bdf8' }}>3.84 / 4.0 (Eligible for Max 28 Credits)</strong>
            </div>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Requested Overload Course</label>
            <input type="text" defaultValue="CS499: Advanced Quantum Computing Research Seminar (4 Credits)" style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }} />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
            <Button variant="ghost" onClick={() => setIsOverloadModalOpen(false)}>Cancel</Button>
            <Button variant="primary" onClick={() => { showToast('Submitted Dean Credit Overload Waiver Request!', 'success'); setIsOverloadModalOpen(false); }}>Submit Waiver Request</Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
