"""
Database seed generator for Library & Digital Repositories
"""
import random
from typing import List, Dict

def generate_library_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"LIBRARY_{i+1000}",
            "name": f"Enterprise Library & Digital Repositories Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
