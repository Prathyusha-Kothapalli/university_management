"""
Database seed generator for Executive & Departmental Dashboards
"""
import random
from typing import List, Dict

def generate_dashboards_seeds(count: int = 500) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({
            "entity_code": f"DASHBOARDS_{i+1000}",
            "name": f"Enterprise Executive & Departmental Dashboards Item {i+1}",
            "category": "Seeded",
            "status": "ACTIVE"
        })
    return seeds
