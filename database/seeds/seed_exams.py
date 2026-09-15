"""
Database seed generator for Examinations & Result Management
"""
import random
from typing import List, Dict

def generate_exams_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"EXAMS_{i+1000}",
            "name": f"Enterprise Examinations & Result Management Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
