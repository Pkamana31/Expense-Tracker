import json
from datetime import datetime
from pathlib import Path
import csv

# File path for storing data
EXPENSE_FILE = Path(__file__).parent / "expenses.json"

class Expense:
    def __init__(self, amount, category, date=None, note=""):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.note = note

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            note=data.get("note", "")
        )

def load_expenses():
    if not EXPENSE_FILE.exists():
        return []
    with open(EXPENSE_FILE, "r") as f:
        try:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)

def export_to_csv(filename="expenses_export.csv"):
    expenses = load_expenses()
    if not expenses:
        print("No expenses to export.")
        return

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Date", "Note"])
        for e in expenses:
            writer.writerow([e.amount, e.category, e.date, e.note])

    print(f"📁 Exported {len(expenses)} expenses to {filename}")

