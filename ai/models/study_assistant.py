from typing import List, Optional, Literal
from pydantic import BaseModel, Field

ExplanationMode = Literal["detailed", "beginner", "code", "exam_summary"]

class ChatMessageItem(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class StudyAssistantRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Student's query or study question")
    course_id: str = Field(default="CS101", description="Identifier of the course (e.g. CS101, CS202, MATH301)")
    mode: ExplanationMode = Field(default="detailed", description="Explanation style/mode")
    conversation_id: Optional[str] = Field(None, description="Optional conversation tracking ID")
    history: Optional[List[ChatMessageItem]] = Field(default=[], description="Prior messages in this conversation")

class SourceCitation(BaseModel):
    title: str
    snippet: str
    page: str
    relevance_score: float

class StudyAssistantResponse(BaseModel):
    answer: str
    sources: List[SourceCitation]
    confidence: float
    conversation_id: str
    course_id: str
    mode: ExplanationMode
    follow_up_questions: List[str]

class FeedbackRequest(BaseModel):
    conversation_id: str
    message_index: Optional[int] = None
    is_helpful: bool
    comment: Optional[str] = None

