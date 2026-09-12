from typing import Dict, Any
from .base_tool import BaseTool

class GetStudentFeeStatusTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="get_student_fee_status",
            description="Retrieves tuition fee ledger, total billed, amount paid, and outstanding dues",
            required_role="student"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        return {
            "student_id": user_id,
            "total_fee_billed": 75000,
            "amount_paid": 50000,
            "outstanding_balance": 25000,
            "due_date": "2026-09-30",
            "payment_status": "Partial Paid",
            "currency": "INR"
        }

class ProcessFeePaymentTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="process_fee_payment",
            description="Processes instant tuition fee payment transaction and generates digital receipt",
            required_role="finance"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        amount = arguments.get("amount", 25000)
        return {
            "transaction_id": f"TXN-{user_id[:4]}-99281",
            "amount_paid": amount,
            "status": "SUCCESS",
            "timestamp": "2026-09-10 17:20:00",
            "receipt_url": f"https://unisphere.ai/receipts/TXN-99281.pdf"
        }
