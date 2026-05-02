"""Expense tracker CLI"""
import argparse
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DATA = Path("expenses.json")

def load():
    return json.loads(DATA.read_text()) if DATA.exists() else []

def save(items):
    DATA.write_text(json.dumps(items, indent=2))

def cmd_add(args):
    items = load()
    items.append({"amount": args.amount, "category": args.category, "note": args.note or "", "date": datetime.now().isoformat()})
    save(items)
    print(f"added {args.amount} to {args.category}")

def cmd_list(args):
    for it in load():
        print(f'{it["date"][:10]}  {it["amount"]:>8.2f}  {it["category"]:<12} {it["note"]}')

def cmd_total(args):
    print(f"total: {sum(it["amount"] for it in load()):.2f}")

def cmd_summary(args):
    by_cat = defaultdict(float)
    for it in load():
        by_cat[it["category"]] += it["amount"]
    for cat, amt in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        print(f"{cat:<12} {amt:>8.2f}")

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
add = sub.add_parser("add"); add.add_argument("amount", type=float)
add.add_argument("category"); add.add_argument("note", nargs="?")
sub.add_parser("list"); sub.add_parser("total"); sub.add_parser("summary")
args = parser.parse_args()
{"add": cmd_add, "list": cmd_list, "total": cmd_total, "summary": cmd_summary}.get(args.cmd, lambda a: parser.print_help())(args)
