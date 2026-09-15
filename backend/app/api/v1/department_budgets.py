import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/department-budgets",
    tags=["Department Financial Ledgers"]
)


class BudgetAllocationRequest(BaseModel):
    department_id: UUID
    fiscal_year: str = "FY2026-27"
    total_allocated_usd: float = 150000.0
    lab_equipment_allocation: float = 60000.0
    research_grant_allocation: float = 50000.0
    events_conference_allocation: float = 40000.0


class ExpenseLogRequest(BaseModel):
    budget_id: UUID
    category: str = "LAB_EQUIPMENT"  # LAB_EQUIPMENT, RESEARCH_GRANT, EVENTS_CONFERENCE
    amount_usd: float = 12500.0
    description: str
    vendor_name: str


# In-memory storage for department financial ledgers
DEPARTMENT_BUDGETS = {}
EXPENSE_LOGS = {}


@router.post("/allocate")
def allocate_department_budget(req: BudgetAllocationRequest):
    dept_str = str(req.department_id)
    budget_id = str(uuid.uuid4())

    entry = {
        "budget_id": budget_id,
        "department_id": dept_str,
        "fiscal_year": req.fiscal_year,
        "total_allocated_usd": req.total_allocated_usd,
        "total_spent_usd": 0.0,
        "balance_remaining_usd": req.total_allocated_usd,
        "allocations": {
            "LAB_EQUIPMENT": req.lab_equipment_allocation,
            "RESEARCH_GRANT": req.research_grant_allocation,
            "EVENTS_CONFERENCE": req.events_conference_allocation
        },
        "created_at": "2026-09-11T12:30:00Z"
    }

    DEPARTMENT_BUDGETS[dept_str] = entry

    return {
        "message": "Department budget allocated successfully",
        "budget": entry
    }


@router.post("/log-expense")
def log_department_expense(req: ExpenseLogRequest):
    budget_str = str(req.budget_id)
    expense_id = str(uuid.uuid4())

    expense_entry = {
        "expense_id": expense_id,
        "budget_id": budget_str,
        "category": req.category,
        "amount_usd": req.amount_usd,
        "description": req.description,
        "vendor_name": req.vendor_name,
        "logged_at": "2026-09-11T12:34:00Z"
    }

    if budget_str not in EXPENSE_LOGS:
        EXPENSE_LOGS[budget_str] = []
    EXPENSE_LOGS[budget_str].append(expense_entry)

    # Update ledger balance
    for dept_b in DEPARTMENT_BUDGETS.values():
        if dept_b.get("budget_id") == budget_str:
            dept_b["total_spent_usd"] += req.amount_usd
            dept_b["balance_remaining_usd"] -= req.amount_usd

    return {
        "message": "Department expense logged & ledger balance updated",
        "expense": expense_entry
    }


@router.get("/department/{department_id}")
def get_department_budget_ledger(department_id: UUID):
    dept_str = str(department_id)
    budget = DEPARTMENT_BUDGETS.get(dept_str, {
        "budget_id": "bgt-101",
        "department_id": dept_str,
        "fiscal_year": "FY2026-27",
        "total_allocated_usd": 150000.0,
        "total_spent_usd": 32500.0,
        "balance_remaining_usd": 117500.0,
        "allocations": {
            "LAB_EQUIPMENT": 60000.0,
            "RESEARCH_GRANT": 50000.0,
            "EVENTS_CONFERENCE": 40000.0
        }
    })

    budget_id = budget.get("budget_id")
    expenses = EXPENSE_LOGS.get(budget_id, [])

    return {
        "department_id": dept_str,
        "budget": budget,
        "total_expenses_logged": len(expenses),
        "expense_records": expenses
    }
