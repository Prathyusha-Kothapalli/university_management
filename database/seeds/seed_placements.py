"""
Database seed generator for Placements & Alumni Network
"""
import random
from typing import List, Dict

def generate_placements_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"PLACEMENTS_{i+1000}",
            "name": f"Enterprise Placements & Alumni Network Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
