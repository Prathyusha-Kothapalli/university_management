"""
Database seed generator for Sports & Extracurricular Activities
"""
import random
from typing import List, Dict

def generate_sports_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"SPORTS_{i+1000}",
            "name": f"Enterprise Sports & Extracurricular Activities Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
