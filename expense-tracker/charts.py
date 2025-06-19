import matplotlib.pyplot as plt
from collections import defaultdict
from utils import load_expenses

def show_expense_pie_chart():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to display.")
        return

    category_totals = defaultdict(float)
    for e in expenses:
        category_totals[e.category] += e.amount

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    if not values or sum(values) == 0:
        print("No expense values to plot.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Spending Distribution by Category")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def show_expense_bar_chart():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found for chart.")
        return

    category_totals = defaultdict(float)
    for e in expenses:
        category_totals[e.category] += e.amount

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    if not values or sum(values) == 0:
        print("No expense values to plot.")
        return

    plt.figure(figsize=(8, 5))
    plt.barh(labels, values, color="skyblue")
    plt.xlabel("Total Amount Spent (₹)")
    plt.title("Spending by Category")
    plt.tight_layout()
    plt.show()
