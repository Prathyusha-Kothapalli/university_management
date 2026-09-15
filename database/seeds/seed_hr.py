"""
Database seed generator for Human Resources & Faculty Management
"""
import random
from typing import List, Dict

def generate_hr_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"HR_{i+1000}",
            "name": f"Enterprise Human Resources & Faculty Management Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
