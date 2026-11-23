
import json

# JSON file ka location
FILE_PATH = "data/expenses.json"


# Function: Python expenses ko JSON file mein save karega
def save_expenses(expenses):

    # "w" means write mode
    # Agar file mein purana data hai, to replace ho jayega
    with open(FILE_PATH, "w") as file:

        # Python list ko JSON format mein convert karke save karna
        # indent=4 JSON ko readable banata hai
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")


# Function: JSON file se expenses load karega
def load_expenses():

    try:

        # "r" means read mode
        with open(FILE_PATH, "r") as file:

            # JSON file ka data Python list mein convert hoga
            expenses = json.load(file)

        # Loaded expenses return karna
        return expenses

    # Agar JSON file nahi milti
    except FileNotFoundError:
        return []

    # Agar JSON file ka format galat hai
    except json.JSONDecodeError:
        raise ValueError("Your expenses.json file contains invalid JSON.")
