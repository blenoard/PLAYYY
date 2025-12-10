from categories import add_expense_to_category, add_new_category, delete_or_clear_category
from budget_income_expenses import compute_budget, save_summary_to_file, save_data_to_pickle


def print_menu():
    """Print the main menu options."""
    print("\n--- Budget Menu ---")
    print("1. Enter a new expense for a category")
    print("2. Enter a new category")
    print("3. Export summary file")
    print("4. Delete category or clear its expenses")
    print("5. Exit program")


def run_menu_loop(income, categories, expenses_per_category,
                  data_filename, text_filename):
    """
    Main loop of the program:
    - lets the user choose actions from the menu
    - handles export of summary file
    - handles exit with saving data
    """
    while True:
        print_menu()
        choice = input("\nPlease enter a number from the menu: ")

        if choice == "1":
            add_expense_to_category(categories, expenses_per_category)

        elif choice == "2":
            add_new_category(categories, expenses_per_category)

        elif choice == "3":
            # Export summary file (no console summary)
            save_summary_to_file(income, expenses_per_category, text_filename)

        elif choice == "4":
            delete_or_clear_category(categories, expenses_per_category)

        elif choice == "5":
            # Exit program: save data and say goodbye
            total_expenses, difference = compute_budget(income, expenses_per_category)
            save_data_to_pickle(income, categories, expenses_per_category, data_filename)
            print("\nYour final total expenses are:", total_expenses)
            print("Difference (income - expenses):", difference)
            print("Goodbye and thank you for using BudgetPro!")
            break

        else:
            print("Invalid choice.")
