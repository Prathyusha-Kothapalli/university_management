"""
Database seed generator for Campus Health & Clinic Management
"""
import random
from typing import List, Dict

def generate_health_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"HEALTH_{i+1000}", "name": f"Enterprise Campus Health & Clinic Management Seed {i+1}", "status": "ACTIVE"})
    return seeds
