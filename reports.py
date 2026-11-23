def monthly_report(expenses):

    month = input("Enter month (YYYY-MM): ")

    total = 0
    category_totals = {}

    for expense in expenses:

        if expense["date"].startswith(month):

            total += expense["amount"]

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\nMonthly Total:", total)

    print("\nCategory-wise Report:")

    for category, amount in category_totals.items():
        print(category, ":", amount)

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