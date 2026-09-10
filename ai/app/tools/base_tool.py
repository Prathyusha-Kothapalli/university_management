from abc import ABC, abstractmethod
from typing import Dict, Any
from ai.app.schemas.schemas import ToolCallRequest, ToolCallResponse
import time

class BaseTool(ABC):
    """
    Abstract Base Class for all authorized UniSphere AI Agent Tools.
    """
    def __init__(self, name: str, description: str, required_role: str):
        self.name = name
        self.description = description
        self.required_role = required_role

    @abstractmethod
    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        pass

    def run(self, request: ToolCallRequest) -> ToolCallResponse:
        start_time = time.time()
        try:
            res = self.execute(request.arguments, request.user_id, request.user_role)
            elapsed = (time.time() - start_time) * 1000
            return ToolCallResponse(
                tool_name=self.name,
                success=True,
                result=res,
                execution_time_ms=elapsed
            )
        except Exception as e:
            elapsed = (time.time() - start_time) * 1000
            return ToolCallResponse(
                tool_name=self.name,
                success=False,
                error=str(e),
                execution_time_ms=elapsed
            )
