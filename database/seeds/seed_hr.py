"""
Database seed generator for Human Resources & Faculty Management
"""
import random
from typing import List, Dict

def generate_hr_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"HR_{i+1000}", "name": f"Enterprise Human Resources & Faculty Management Seed {i+1}", "status": "ACTIVE"})
    return seeds
