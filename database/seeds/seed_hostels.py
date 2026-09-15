"""
Database seed generator for Student Life & Hostel Operations
"""
import random
from typing import List, Dict

def generate_hostels_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"HOSTELS_{i+1000}", "name": f"Enterprise Student Life & Hostel Operations Seed {i+1}", "status": "ACTIVE"})
    return seeds
