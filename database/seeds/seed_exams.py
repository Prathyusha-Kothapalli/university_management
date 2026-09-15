"""
Database seed generator for Examinations & Result Management
"""
import random
from typing import List, Dict

def generate_exams_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"EXAMS_{i+1000}", "name": f"Enterprise Examinations & Result Management Seed {i+1}", "status": "ACTIVE"})
    return seeds
