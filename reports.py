from datetime import datetime
def monthly_report(expenses):

    # Step 1: Validate month
    while True:
        month = input("Enter month (YYYY-MM): ").strip()

        try:
            parsed_month = datetime.strptime(month, "%Y-%m")

            if parsed_month.strftime("%Y-%m") == month:
                break

            print("Invalid format! Example: 2026-11")

        except ValueError:
            print("Invalid month! Example: 2026-11")

    # Step 2: Initialize variables
    total = 0
    category_totals = {}

    # Step 3: Filter expenses
    for expense in expenses:

        if expense["date"].startswith(month):

            total += expense["amount"]

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    # Step 4: Handle empty monthly report
    if not category_totals:
        print(f"No expenses found for {month}.")
        return

    # Step 5: Display report
    print(f"\n===== MONTHLY REPORT: {month} =====")

    print(f"Monthly Total: Rs.{total:.2f}")

    print("\nCategory-wise Report:")

    for category, amount in category_totals.items():
        print(f"{category}: Rs.{amount:.2f}")


def expense_analysis(expenses):

    if not expenses:
        print("No expenses available.")
        return

    highest = max(expenses, key=lambda x: x["amount"])
    lowest = min(expenses, key=lambda x: x["amount"])

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    print("\n----- EXPENSE ANALYSIS -----")

    print("Highest:", highest["title"], highest["amount"])
    print("Lowest:", lowest["title"], lowest["amount"])
    print("Total:", total)
    print("Average:", average)