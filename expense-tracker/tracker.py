from charts import show_expense_pie_chart, show_expense_bar_chart
from utils import Expense, load_expenses, save_expenses, export_to_csv
from datetime import datetime
from collections import defaultdict

def print_menu():
    print("\n===== Expense Tracker Menu =====")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View summary by category")
    print("4. Show pie chart")
    print("5. Show bar chart")
    print("6. Delete an expense")
    print("7. Filter expenses by month")
    print("8. Export expenses to CSV")
    print("9. Exit")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n--- Expense List ---")
    for i, e in enumerate(expenses):
        print(f"{i+1}. ₹{e.amount} | {e.category} | {e.date} | {e.note}")

def add_expense():
    try:
        amount = float(input("Enter amount (₹): "))
        category = input("Enter category (e.g., Food, Transport): ")
        note = input("Optional note: ")
        expense = Expense(amount, category, note=note)
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added successfully.")
    except ValueError:
        print("❌ Invalid amount.")

def view_summary():
    expenses = load_expenses()
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount

    if not summary:
        print("No data to summarize.")
        return

    print("\n--- Summary by Category ---")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total:.2f}")

def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to delete.")
        return

    list_expenses(expenses)

    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)
            print(f"🗑️ Deleted: ₹{deleted.amount} | {deleted.category} | {deleted.date}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def filter_by_month():
    month_input = input("Enter month (YYYY-MM): ").strip()
    expenses = load_expenses()
    filtered = [e for e in expenses if e.date.startswith(month_input)]

    if not filtered:
        print(f"No expenses found for {month_input}.")
    else:
        print(f"\n--- Expenses for {month_input} ---")
        list_expenses(filtered)

def main():
    while True:
        print_menu()
        choice = input("Select an option (1–9): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            expenses = load_expenses()
            list_expenses(expenses)
        elif choice == "3":
            view_summary()
        elif choice == "4":
            show_expense_pie_chart()
        elif choice == "5":
            show_expense_bar_chart()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            filter_by_month()
        elif choice == "8":
            export_to_csv()
        elif choice == "9":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1–9.")

if __name__ == "__main__":
    main()
