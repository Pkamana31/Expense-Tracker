import matplotlib.pyplot as plt
from collections import defaultdict
from utils import load_expenses

def show_expense_pie_chart():
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

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.axis("equal")
    plt.show()
