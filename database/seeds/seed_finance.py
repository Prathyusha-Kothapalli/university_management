"""
Database seed generator for Finance, Billing & Payroll
"""
import random
from typing import List, Dict

def generate_finance_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"FINANCE_{i+1000}",
            "name": f"Enterprise Finance, Billing & Payroll Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
