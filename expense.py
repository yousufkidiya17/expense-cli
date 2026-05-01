"""Expense tracker CLI"""
import argparse
import json
import sys
from pathlib import Path

DATA = Path("expenses.json")

def load():
    return json.loads(DATA.read_text()) if DATA.exists() else []

def save(items):
    DATA.write_text(json.dumps(items, indent=2))

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
add = sub.add_parser("add"); add.add_argument("amount", type=float)
add.add_argument("category"); add.add_argument("note", nargs="?")
sub.add_parser("list"); sub.add_parser("total")
args = parser.parse_args()
