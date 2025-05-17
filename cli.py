
import csv
import os

def save_csv(results, path="zara/output/results.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["site", "url", "found", "avatar", "last_activity"])
        for site, data in results.items():
            writer.writerow([
                site,
                data.get("url", ""),
                data.get("exists", False),
                data.get("avatar", ""),
                data.get("activity", "")
            ])

import argparse
import asyncio
import json
from zara.core import ZaraScanner
from zara.output import save_json

def load_sites(path="zara/sites.json"):
    with open(path, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="🔍 Zara - Username Enumerator")
    parser.add_argument("username", help="Username to scan")
    parser.add_argument("--format", choices=["json", "pretty", "csv"], default="pretty", help="Output format type")
    args = parser.parse_args()

    sites = load_sites()
    scanner = ZaraScanner(args.username, sites)

    print(f"🔎 Scanning {len(sites)} sites for: {args.username}")
    results = asyncio.run(scanner.run())

    found = {k: v for k, v in results.items() if v.get("exists")}
    print(f"\n✅ Found on {len(found)} sites:")
    for site, info in found.items():
        print(f"- {site}: {info['url']}")

    if args.format == "csv":
        save_csv(results)
        print("📄 Saved to zara/output/results.csv")
    elif args.format == "json":
        save_json(results)
        print("📦 Saved to zara/output/results.json")
    else:
        from rich import print as rprint
        rprint(results)


if __name__ == "__main__":
    main()
