# Uses: lists, functions, list comprehensions, sum()

expenses = [
    [1, "05", "Data Subscription", 2500],
    [2, "06", "Lunch", 1200],
    [3, "06", "Transport", 800]
]


def add_expense(month, description, amount):
    new_id = len(expenses) + 1
    expenses.append([new_id, month, description, float(amount)])
    print(f"  Expense added with ID {new_id}.")


def view_expenses():
    if not expenses:
        print("  No expenses recorded yet.")
        return
    print(f"\n  {'ID':<5} {'Month':<8} {'Description':<25} {'Amount (N)'}")
    print("  " + "-" * 50)
    for exp in expenses:
        print(f"  {exp[0]:<5} {exp[1]:<8} {exp[2]:<25} {exp[3]:,.2f}")


def update_expense(expense_id, new_description, new_amount):
    for exp in expenses:
        if exp[0] == expense_id:
            exp[2] = new_description
            exp[3] = float(new_amount)
            print(f"  Expense {expense_id} updated.")
            return
    print(f"  Expense with ID {expense_id} not found.")


def delete_expense(expense_id):
    for exp in expenses:
        if exp[0] == expense_id:
            expenses.remove(exp)
            print(f"  Expense {expense_id} deleted.")
            return
    print(f"  Expense with ID {expense_id} not found.")


def summary_all():
    total = sum([exp[3] for exp in expenses])
    print(f"\n  Total spent across all months: N{total:,.2f}")


def summary_by_month(month):
    monthly = [exp[3] for exp in expenses if exp[1] == month]
    if monthly:
        print(f"\n  Total spent in month '{month}': N{sum(monthly):,.2f}")
    else:
        print(f"  No expenses found for month '{month}'.")


while True:
    print("\n===== CPE Expense Tracker =====")
    print("  1. Add expense")
    print("  2. View all expenses")
    print("  3. Update expense")
    print("  4. Delete expense")
    print("  5. Total summary")
    print("  6. Summary by month")
    print("  7. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        month = input("  Month (e.g. 06): ").strip()
        desc = input("  Description: ").strip()
        amount = input("  Amount: ").strip()
        add_expense(month, desc, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        exp_id = int(input("  Expense ID to update: ").strip())
        new_desc = input("  New description: ").strip()
        new_amt = input("  New amount: ").strip()
        update_expense(exp_id, new_desc, new_amt)
    elif choice == "4":
        exp_id = int(input("  Expense ID to delete: ").strip())
        delete_expense(exp_id)
    elif choice == "5":
        summary_all()
    elif choice == "6":
        month = input("  Enter month (e.g. 06): ").strip()
        summary_by_month(month)
    elif choice == "7":
        print("  Exiting. Bye!")
        break
    else:
        print("  Invalid choice. Try again.")