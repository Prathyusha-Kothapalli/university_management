"""
Database seed generator for Academic & Curriculum Management
"""
import random
from typing import List, Dict

def generate_academics_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"ACADEMICS_{i+1000}", "name": f"Enterprise Academic & Curriculum Management Seed {i+1}", "status": "ACTIVE"})
    return seeds
