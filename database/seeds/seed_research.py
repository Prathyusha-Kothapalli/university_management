"""
Database seed generator for Research, Grants & Lab Inventory
"""
import random
from typing import List, Dict

def generate_research_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"RESEARCH_{i+1000}",
            "name": f"Enterprise Research, Grants & Lab Inventory Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
