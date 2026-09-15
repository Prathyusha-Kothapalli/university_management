"""
Database seed generator for Academic & Curriculum Management
"""
import random
from typing import List, Dict

def generate_academics_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"ACADEMICS_{i+1000}",
            "name": f"Enterprise Academic & Curriculum Management Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
