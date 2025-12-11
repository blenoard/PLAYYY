import pickle


def get_valid_period():
    """
    Ask the user for a year-month string in the format YYYY-MM.
    Repeat until the format and month are valid.
    """
    while True:
        period = input("Enter year and month for this budget (YYYY-MM): ").strip()

        # basic structure check
        if len(period) != 7 or period[4] != "-":
            print("Invalid format. Please use YYYY-MM (for example 2025-12).")
            continue

        year_str = period[:4]
        month_str = period[5:]

        if not (year_str.isdigit() and month_str.isdigit()):
            print("Year and month must be numbers. Please try again.")
            continue

        month = int(month_str)
        if month < 1 or month > 12:
            print("Month must be between 01 and 12. Please try again.")
            continue

        return period


def enter_income():
    """Ask the user for the monthly income with input validation."""
    while True:
        user_input = input("Please enter your income: ")
        try:
            income = float(user_input)

            if income < 0:
                print("Income cannot be negative. Please try again.")
            else:
                print("Your income is", income)
                return income

        except ValueError:
            print("This is not a number. Please try again.")



def init_expenses_for_all_categories(categories, expenses_per_category):
    """
    Go through all categories once and ask for an initial expense.
    The user can skip a category by pressing Enter.
    """
    print("\nNow we will go through your main categories once.")
    print("If you have no expense for a category, just press Enter.")

    for category in categories:
        while True:
            user_input = input("Enter your expense for " + category +
                               " (or press Enter to skip): ").strip()

            if user_input == "":
                print("No expense entered for", category)
                break

            try:
                amount = float(user_input)
                if amount < 0:
                    print("Expense cannot be negative. Please try again.")
                else:
                    expenses_per_category[category] += amount
                    print("Saved", amount, "for", category)
                    break
            except ValueError:
                print("This is not a number. Please try again.")


def compute_budget(income, expenses_per_category):
    """
    Compute total expenses and the difference (income - expenses).
    Does not print anything, only returns numbers.
    """
    total_expenses = sum(expenses_per_category.values())
    difference = income - total_expenses
    return total_expenses, difference


def save_summary_to_file(income, expenses_per_category, filename):
    """
    Create a text file with a budget summary.
    This function does not print the summary to the console.
    """
    total_expenses, difference = compute_budget(income, expenses_per_category)

    file = open(filename, "w")

    file.write("BUDGET SUMMARY\n")
    file.write("-----------------\n")
    file.write("Income: " + str(income) + "\n")
    file.write("\nExpenses by category:\n")
    for cat, amount in expenses_per_category.items():
        file.write("- " + cat + ": " + str(amount) + "\n")

    file.write("\nTotal expenses: " + str(total_expenses) + "\n")
    file.write("Difference (income - expenses): " + str(difference) + "\n")

    if difference > 0:
        file.write("Status: You are under budget.\n")
    elif difference < 0:
        file.write("Status: You are over budget.\n")
    else:
        file.write("Status: Your budget is balanced.\n")

    file.close()
    print("Summary exported to", filename)


def save_data_to_pickle(income, categories, expenses_per_category, data_filename):
    """Save the current data to a pickle file for this period."""
    data = {
        "income": income,
        "categories": categories,
        "expenses_per_category": expenses_per_category
    }
    file = open(data_filename, "wb")
    pickle.dump(data, file)
    file.close()
    print("Data saved to", data_filename)


def load_data_from_pickle(data_filename):
    """
    Try to load existing data from pickle file.
    Return the data dict or None if file does not exist.
    """
    try:
        file = open(data_filename, "rb")
        data = pickle.load(file)
        file.close()
        print("Existing data loaded from", data_filename)
        return data
    except FileNotFoundError:
        return None


def load_or_init_budget(period):
    """
    Load existing budget data for the given period if available.
    Otherwise, create a new budget with default categories
    and ask the user for income and initial expenses.
    """
    data_filename = "BudgetPro_" + period + ".dat"
    text_filename = "BudgetPro_" + period + ".txt"

    # Try to load existing data for this period
    loaded_data = load_data_from_pickle(data_filename)

    if loaded_data is not None:
        print("\nExisting budget data found for", period + ".")
        # Ask the user if they want to reuse the existing data
        while True:
            answer = input("Do you want to use the existing data? (Y/N): ").strip().lower()

            if answer == "y":
                print("Loading existing data...\n")
                income = loaded_data["income"]
                categories = loaded_data["categories"]
                expenses_per_category = loaded_data["expenses_per_category"]
                break

            elif answer == "n":
                print("Starting a NEW monthly budget for", period + ". Previous data will be overwritten.\n")
                income = enter_income()

                categories = ["rent", "food", "subscriptions",
                              "transport", "other expenses"]
                expenses_per_category = {cat: 0.0 for cat in categories}

                init_expenses_for_all_categories(categories, expenses_per_category)
                break

            else:
                print("Please enter Y or N.")
    else:
        # No existing data: start a fresh budget
        print("\nNo existing data found. Starting a new monthly budget for", period)
        income = enter_income()

        categories = ["rent", "food", "subscriptions",
                      "transport", "other expenses"]
        expenses_per_category = {cat: 0.0 for cat in categories}

        init_expenses_for_all_categories(categories, expenses_per_category)

    return income, categories, expenses_per_category, data_filename, text_filename
