import json
import os

CATALOG = [
    {
        "name": "Java 8 (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/",
        "skills": ["java", "developer", "backend"],
        "test_type": "Knowledge"
    },
    {
        "name": "OPQ32r",
        "url": "https://www.shl.com/solutions/products/product-catalog/",
        "skills": ["personality", "leadership", "communication"],
        "test_type": "Personality"
    },
    {
        "name": "General Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/",
        "skills": ["reasoning", "analytical", "aptitude"],
        "test_type": "Cognitive"
    }
]

os.makedirs("data", exist_ok=True)

with open("data/shl_catalog.json", "w", encoding="utf-8") as f:
    json.dump(CATALOG, f, indent=4)

print("Catalog saved successfully!")