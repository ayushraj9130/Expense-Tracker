# Expense Tracker

A command-line based Expense Tracker application built using Python. It allows users to manage daily expenses, store records in JSON format, and generate expense reports.

## Features

- Add new expenses
- View all expenses
- Update existing expenses
- Delete expenses with confirmation
- Store expense data permanently using JSON
- Generate monthly expense reports
- Generate category-wise expense reports
- Analyze highest and lowest expenses
- Calculate total and average expenses
- Validate user inputs, amounts, and dates

## Technologies Used

- Python
- JSON
- Git
- GitHub

## Project Structure

```text
Expense Tracker/
│
├── main.py
├── expense.py
├── storage.py
├── reports.py
│
├── Data/
│   └── expenses.json
│
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ayushraj9130/Expense-Tracker.git
```

### 2. Open the project folder

```bash
cd Expense-Tracker
```

### 3. Run the application

```bash
python main.py
```

## How to Use

After running the application, you will see the following menu:

```text
==============================
       EXPENSE TRACKER
==============================

1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Monthly Report
6. Expense Analysis
7. Exit
```

Choose an option by entering its corresponding number.

### Expense Data Format

Each expense is stored as a dictionary:

```python
{
    "id": 1,
    "title": "Lunch",
    "amount": 150.0,
    "category": "Food",
    "date": "2026-11-25"
}
```

The application stores expense records in `Data/expenses.json`.

## Learning Outcomes

Through this project, I practiced:

- Python functions and modules
- Lists and dictionaries
- CRUD operations
- File handling
- JSON data storage
- Exception handling
- Input validation
- Git and GitHub

## Future Improvements

- Search expenses
- Filter expenses by category
- Export reports to CSV
- Add automated tests using pytest
- Build a REST API using FastAPI

## Author

**Aayush**

GitHub: [ayushraj9130](https://github.com/ayushraj9130)