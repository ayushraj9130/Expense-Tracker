# storage.py se save aur load functions import karna
from storage import save_expenses
from datetime import datetime

# ==============================
# 1. ADD EXPENSE
# ==============================

def add_expense(expenses):

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

def view_expense(expenses):

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


def update_expense(expenses):

    if not expenses:
        print("No expenses available to update!")
        return

    # Step 1: Expense ID validation
    while True:
        try:
            expense_id = int(input("Enter Expense ID to update: "))
            break
        except ValueError:
            print("Please enter a valid ID!")

    # Step 2: Find expense
    for expense in expenses:

        if expense["id"] == expense_id:

            print("\nCurrent Expense Details:")
            print(expense)

            print("\nEnter New Details:")

            # Step 3: Validate title
            while True:
                new_title = input("Enter new title: ").strip()

                if new_title:
                    break

                print("Title cannot be empty!")

            # Step 4: Validate amount
            while True:
                try:
                    new_amount = float(input("Enter new amount: "))

                    if new_amount > 0:
                        break

                    print("Amount must be greater than zero!")

                except ValueError:
                    print("Please enter a valid number!")

            # Step 5: Validate category
            while True:
                new_category = input("Enter new category: ").strip()

                if new_category:
                    break

                print("Category cannot be empty!")

            # Step 6: Validate date
            while True:
                new_date = input("Enter new date (YYYY-MM-DD): ")

                try:
                    datetime.strptime(new_date, "%Y-%m-%d")
                    break

                except ValueError:
                    print("Invalid date! Example: 2026-11-22")

            # Step 7: Update dictionary
            expense["title"] = new_title
            expense["amount"] = new_amount
            expense["category"] = new_category
            expense["date"] = new_date

            # Step 8: Save updated expenses
            save_expenses(expenses)

            print("Expense updated successfully!")
            return

    print("Expense ID not found!")


# ==============================
# 4. DELETE EXPENSE
# ==============================


def delete_expense(expenses):

    if not expenses:
        print("No expenses available to delete!")
        return

    # Step 1: Validate Expense ID
    while True:
        try:
            search_id = int(input("Enter Expense ID to delete: "))
            break

        except ValueError:
            print("Please enter a valid ID!")

    # Step 2: Find Expense
    for expense in expenses:

        if expense["id"] == search_id:

            print("\nExpense Found:")
            print(expense)

            # Step 3: Confirmation
            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirm == "yes":

                expenses.remove(expense)

                save_expenses(expenses)

                print("Expense deleted successfully!")

            elif confirm == "no":
                print("Deletion cancelled!")

            else:
                print("Invalid confirmation! Deletion cancelled.")

            return

    print("Expense ID not found!")
