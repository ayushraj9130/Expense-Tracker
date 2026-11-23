# storage.py se save aur load functions import karna
from storage import save_expenses, load_expenses
from reports import monthly_report, expense_analysis
from datetime import datetime


expenses = load_expenses()

# ==============================
# 1. ADD EXPENSE
# ==============================

def add_expense():

    while True:
        title = input("Enter title: ").strip()

        if title:
            break

        print("Title cannot be empty!")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            break

        except ValueError:
            print("Please enter a valid number!")

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty!")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date! Example: 2026-11-22")

    expense = {
        "id": max((item["id"] for item in expenses), default=0) + 1,
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# ==============================
# 2. VIEW EXPENSES
# ==============================

def view_expense():

    # Check karna ki list empty hai ya nahi
    if not expenses:
        print("No expenses found!")
        return

    print("\n========== ALL EXPENSES ==========")

    # Har expense ko ek-ek karke display karna
    for expense in expenses:

        print(f"\nID: {expense['id']}")
        print(f"Title: {expense['title']}")
        print(f"Amount: ₹{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")

        print("------------------------------------")


# ==============================
# 3. UPDATE EXPENSE
# ==============================

def update_expense():

    if not expenses:
        print("No expenses available to update!")
        return

    # User se expense ID lena
    expense_id = int(input("Enter Expense ID to update: "))

    # Matching ID search karna
    for expense in expenses:

        if expense["id"] == expense_id:

            print("\nCurrent Expense Details:")
            print(expense)

            print("\nEnter New Details:")

            new_title = input("Enter new title: ")
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            new_date = input("Enter new date (YYYY-MM-DD): ")

            # Dictionary ki existing values update karna
            expense["title"] = new_title
            expense["amount"] = new_amount
            expense["category"] = new_category
            expense["date"] = new_date

            # Updated data JSON file mein save karna
            save_expenses(expenses)

            print("Expense updated successfully!")
            return

    print("Expense ID not found!")


# ==============================
# 4. DELETE EXPENSE
# ==============================

def delete_expense():

    if not expenses:
        print("No expenses available to delete!")
        return

    search_id = int(input("Enter Expense ID to delete: "))

    for expense in expenses:

        if expense["id"] == search_id:

            print("\nExpense Found:")
            print(expense)

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirm.lower() == "yes":

                # List se matching dictionary delete karna
                expenses.remove(expense)

                # Deleted data JSON file mein save karna
                save_expenses(expenses)

                print("Expense deleted successfully!")

            else:
                print("Deletion cancelled!")

            return

    print("Expense ID not found!")