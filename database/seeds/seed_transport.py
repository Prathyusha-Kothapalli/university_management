"""
Database seed generator for Transport & Fleet Logistics
"""
import random
from typing import List, Dict

def generate_transport_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"TRANSPORT_{i+1000}", "name": f"Enterprise Transport & Fleet Logistics Seed {i+1}", "status": "ACTIVE"})
    return seeds
