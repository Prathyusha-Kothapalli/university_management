"""
Database seed generator for Sports & Extracurricular Activities
"""
import random
from typing import List, Dict

def generate_sports_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"SPORTS_{i+1000}", "name": f"Enterprise Sports & Extracurricular Activities Seed {i+1}", "status": "ACTIVE"})
    return seeds
