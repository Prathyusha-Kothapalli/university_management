"""
Database seed generator for Transport & Fleet Logistics
"""
import random
from typing import List, Dict

def generate_transport_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"TRANSPORT_{i+1000}",
            "name": f"Enterprise Transport & Fleet Logistics Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
