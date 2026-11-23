from storage import load_expenses
from reports import monthly_report, expense_analysis
from expense import add_expense, view_expense, update_expense, delete_expense

def main():
    expenses = load_expenses()
    # ==============================
    # 5. MAIN MENU
    # ==============================

    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Monthly Report")
        print("6. Expense Analysis")
        print("7. Exit")

        choose = int(input("Enter your choice: "))

        if choose == 1:
            add_expense()

        elif choose == 2:
            view_expense()

        elif choose == 3:
            update_expense()

        elif choose == 4:
            delete_expense()

        elif choose == 5:
            monthly_report(expenses)

        elif choose == 6:
            expense_analysis(expenses)

        elif choose == 7:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main() 