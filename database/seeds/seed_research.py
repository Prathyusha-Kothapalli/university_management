"""
Database seed generator for Research, Grants & Lab Inventory
"""
import random
from typing import List, Dict

def generate_research_seeds(count: int = 1000) -> List[Dict]:
    seeds = []
    for i in range(count):
        seeds.append({"code": f"RESEARCH_{i+1000}", "name": f"Enterprise Research, Grants & Lab Inventory Seed {i+1}", "status": "ACTIVE"})
    return seeds
