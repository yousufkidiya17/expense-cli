"""Basic tests"""
import tempfile
from pathlib import Path

import expense

def test_add_list():
    with tempfile.TemporaryDirectory() as d:
        expense.DATA = Path(d) / "e.json"
        expense.save([{"amount": 10, "category": "food", "note": "", "date": "2026-05-01"}])
        assert expense.load()[0]["amount"] == 10
        print("ok")

if __name__ == "__main__":
    test_add_list()
