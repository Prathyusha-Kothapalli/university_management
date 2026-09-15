"""
Database seed generator for Finance, Billing & Payroll
"""
import random
from typing import List, Dict

def generate_finance_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"FINANCE_{i+1000}", "name": f"Enterprise Finance, Billing & Payroll Seed {i+1}", "status": "ACTIVE"})
    return seeds
