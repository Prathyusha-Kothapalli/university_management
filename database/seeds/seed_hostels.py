"""
Database seed generator for Student Life & Hostel Operations
"""
import random
from typing import List, Dict

def generate_hostels_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"HOSTELS_{i+1000}",
            "name": f"Enterprise Student Life & Hostel Operations Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
