import json
import os

FILE = "expenses.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_expense(data):
    amount = float(input("Amount: "))
    category = input("Category (food, transport, etc): ")
    note = input("Note: ")

    data.append({
        "amount": amount,
        "category": category,
        "note": note
    })

    print("Expense added!")


def show_expenses(data):
    if not data:
        print("No expenses yet.")
        return

    for i, e in enumerate(data, 1):
        print(f"{i}. {e['amount']} TL | {e['category']} | {e['note']}")


def total_expense(data):
    total = sum(e["amount"] for e in data)
    print(f"Total: {total} TL")


def category_summary(data):
    summary = {}

    for e in data:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    print("\nCategory Summary:")
    for cat, amount in summary.items():
        print(f"{cat}: {amount} TL")


def main():
    data = load_data()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Total")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            show_expenses(data)
        elif choice == "3":
            total_expense(data)
        elif choice == "4":
            category_summary(data)
        elif choice == "5":
            save_data(data)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()