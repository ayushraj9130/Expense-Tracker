
import json
from pathlib import Path

# Current storage.py file ka folder
BASE_DIR = Path(__file__).resolve().parent

# JSON file ka complete path
FILE_PATH = BASE_DIR / "Data" / "expenses.json"


# Save expenses
def save_expenses(expenses):

    # Agar Data folder nahi hai toh create karo
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")


# Load expenses
def load_expenses():

    try:
        with open(FILE_PATH, "r") as file:
            expenses = json.load(file)

        return expenses

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        raise ValueError(
            f"Invalid JSON data found in {FILE_PATH}"
        )
