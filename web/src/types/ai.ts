export type ExplanationMode = 'detailed' | 'beginner' | 'code' | 'exam_summary';

export interface Course {
  id: string;
  name: string;
  code: string;
  department: string;
  description: string;
}

export interface SourceCitation {
  title: string;
  snippet: string;
  page: string;
  relevance_score: number;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
  sources?: SourceCitation[];
  confidence?: number;
  conversation_id?: string;
  course_id?: string;
  mode?: ExplanationMode;
  follow_up_questions?: string[];
  isBookmarked?: boolean;
  helpfulRating?: 'helpful' | 'not_helpful' | null;
  isError?: boolean;
}

export interface ConversationSession {
  id: string;
  title: string;
  courseId: string;
  mode: ExplanationMode;
  lastUpdated: string;
  messages: ChatMessage[];
}

export interface StudyAssistantRequestPayload {
  question: string;
  course_id: string;
  mode: ExplanationMode;
  conversation_id?: string;
  history?: Array<{ role: 'user' | 'assistant'; content: string }>;
}

export interface StudyAssistantResponsePayload {
  answer: string;
  sources: SourceCitation[];
  confidence: number;
  conversation_id: string;
  course_id: string;
  mode: ExplanationMode;
  follow_up_questions: string[];
}

