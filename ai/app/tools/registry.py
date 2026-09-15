from typing import Dict, Optional
from .base_tool import BaseTool
from .academic_tools import GetStudentAcademicsTool, GetAttendanceSummaryTool, CalculateGpaTool
from .finance_tools import GetStudentFeeStatusTool, ProcessFeePaymentTool
from .library_tools import SearchLibraryBooksTool, IssueBookTool
from .placement_tools import GetPlacementDrivesTool, VerifyOfferLetterTool
from .exam_tools import GenerateHallTicketTool

class ToolRegistry:
    """
    Central Registry & Executor for all UniSphere AI Agent Tools.
    """
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        self._register_default_tools()

    def _register_default_tools(self):
        tools_list = [
            GetStudentAcademicsTool(),
            GetAttendanceSummaryTool(),
            CalculateGpaTool(),
            GetStudentFeeStatusTool(),
            ProcessFeePaymentTool(),
            SearchLibraryBooksTool(),
            IssueBookTool(),
            GetPlacementDrivesTool(),
            VerifyOfferLetterTool(),
            GenerateHallTicketTool()
        ]
        for tool in tools_list:
            self.register_tool(tool)

    def register_tool(self, tool: BaseTool):
        self._tools[tool.name] = tool

    def get_tool(self, name: str) -> Optional[BaseTool]:
        return self._tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        return {name: tool.description for name, tool in self._tools.items()}
