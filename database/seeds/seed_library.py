"""
Database seed generator for Library & Digital Repositories
"""
import random
from typing import List, Dict

def generate_library_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"LIBRARY_{i+1000}", "name": f"Enterprise Library & Digital Repositories Seed {i+1}", "status": "ACTIVE"})
    return seeds
