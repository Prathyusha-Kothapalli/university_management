from typing import Dict, Any
from .base_tool import BaseTool

class SearchLibraryBooksTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="search_library_books",
            description="Searches central library catalog by title, author, topic or ISBN",
            required_role="student"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        query = arguments.get("query", "")
        return {
            "query": query,
            "total_matches": 3,
            "books": [
                {"book_id": "bk-101", "title": "Operating System Concepts", "author": "Silberschatz", "available_copies": 4},
                {"book_id": "bk-102", "title": "Deep Learning with PyTorch", "author": "Eli Stevens", "available_copies": 2},
                {"book_id": "bk-103", "title": "Database System Concepts", "author": "Abraham Silberschatz", "available_copies": 5}
            ]
        }

class IssueBookTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="issue_book",
            description="Issues library book to a borrower and sets due date",
            required_role="librarian"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        book_id = arguments.get("book_id", "bk-101")
        borrower_id = arguments.get("borrower_id", user_id)
        return {
            "issue_id": f"ISS-{book_id}-992",
            "book_id": book_id,
            "borrower_id": borrower_id,
            "issue_date": "2026-09-10",
            "due_date": "2026-09-24",
            "status": "ISSUED"
        }
