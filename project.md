# 🍏 BudgetPro – Monthly Budget Planner (Console)

🚧 This is a template-style project documentation for the course Programming Foundations at FHNW, BSc BIT.  
🚧 Do not keep this section in your final submission.

This project is intended to:

- Practice the complete process from problem analysis to implementation  
- Apply Python programming concepts learned in the Programming Foundations module  
- Demonstrate the use of console interaction, data validation, and file processing  
- Produce clean, well-structured, and modular code  
- Prepare students for teamwork and documentation in later modules  

---

# 📝 Analysis

## Problem

Many people track monthly budgets manually, which leads to missing data, incorrect calculations, and inconsistent tracking.  
BudgetPro aims to provide users with a structured way to record income and expenses across categories, automatically compute totals, and save monthly data persistently.

## Scenario

A user starts BudgetPro at the beginning of a month and enters their income and first expenses for default categories.  
The program creates a new budget for the selected month.

If the user later runs the program again for the same month, BudgetPro loads existing data automatically from a file, allowing the user to continue adding expenses, managing categories, or exporting summaries.

## User Stories

- As a user, I want to enter my income.  
- As a user, I want to enter expenses into structured categories.  
- As a user, I want to add new categories.  
- As a user, I want to delete or reset existing categories.  
- As a user, I want to export a monthly summary file.  
- As a user, I want my monthly data to be saved and reloaded automatically.

## Use Cases

- Validate period (YYYY-MM)  
- Create a new monthly budget  
- Load an existing monthly budget  
- Enter expenses  
- Add new categories  
- Delete or clear categories  
- Export a summary text file  
- Save and exit program  

---

# ✅ Project Requirements

This application meets all three requirements:

## 1. Interactive App (Console Input)

Users can:

- Enter period (YYYY-MM)  
- Enter income  
- Enter expenses  
- Navigate a menu  
- Add/delete categories  
- Export summary  
- Exit program  

The application uses loops and menu-driven interaction with `input()`.

## 2. Data Validation

Examples:

- **Period validation:**  
  Ensures correct format `YYYY-MM`, numeric values, and valid month (01–12).
- **Income/Expense validation:**  
  Accepts only numbers and rejects negative or invalid input.
- **Category validation:**  
  Ensures no duplicate names and correct index selection.

## 3. File Processing

The program uses two file types:

### ✔ Monthly Data File (`.dat`) – Pickle  
Stores:
- income  
- categories  
- expenses per category  

Loaded automatically when the same month is selected again.

### ✔ Summary File (`.txt`)  
Human-readable export for records, containing:
- income  
- expenses per category  
- total expenses  
- difference (income – expenses)  
- financial status (under/over/balanced budget)

---

# ⚙️ Implementation

## Technology

- Python 3  
- GitHub Codespaces  
- Standard library only (`pickle`)  
- Modular program architecture  

---

## 📂 Repository Structure

BudgetPro/
├── main.py # entry point of the program
├── greet_user.py # user greeting
├── categories.py # category management functions
├── budget_income_expenses.py # income, expenses, validation, summary, persistence
├── menu.py # menu loop and navigation
├── BudgetPro_2025-12.txt # example summary file
├── BudgetPro_2025-12.dat # example data file
└── README.md # documentation


---

## ▶️ How to Run


Runs the full console application.

---

## 📚 Libraries Used

### `pickle`
Used for saving and loading monthly data in structured Python dictionaries.  
Part of the Python standard library.

---

# 👥 Team & Contributions

All team members contributed jointly to all parts of the project:

| Team Member | Contribution |
|------------|--------------|
| Team Member A | General development (income, expenses, categories, menu) |
| Team Member B | General development (validation, persistence, summary export) |
| Team Member C | General development (modularization, testing, documentation) |

*(Replace A, B, C with actual group member names.)*

---

# 🤝 Contributing

Use this repository as a starting point by importing it into your own GitHub account.  
Commit regularly to track progress.  

---

# 📝 License

This project is provided for educational use only as part of the Programming Foundations module.  
MIT License.

