import json
import os

def save_json(results, path="zara/output/results.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=4)
