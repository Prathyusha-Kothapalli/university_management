"""
Database seed generator for Placements & Alumni Network
"""
import random
from typing import List, Dict

def generate_placements_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"PLACEMENTS_{i+1000}", "name": f"Enterprise Placements & Alumni Network Seed {i+1}", "status": "ACTIVE"})
    return seeds
