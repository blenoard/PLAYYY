def show_categories(categories):
    """Print all available categories with numbers."""
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, start=1):
        print(str(i) + ".", cat)


def choose_category(categories):
    """
    Let the user choose a category by number.
    Return the index (0-based) or None if user returns to menu.
    """
    if not categories:
        print("No categories available.")
        return None

    show_categories(categories)
    print("0. Return to main menu")

    prompt = "Choose a category number (or 0 to return): "
    selected = input(prompt)

    if selected == "0":
        return None

    if selected.isdigit():
        idx = int(selected) - 1
        if 0 <= idx < len(categories):
            return idx

        print("Invalid category number.")
        return None

    print("Please enter a number.")
    return None


def add_expense_to_category(categories, expenses_per_category):
    """Add a new expense to an existing category."""
    idx = choose_category(categories)
    if idx is None:
        return

    chosen_category = categories[idx]

    while True:
        prompt = "Enter your expense for " + chosen_category + ": "
        amount_input = input(prompt)

        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Expense must be greater than 0. Please try again.")
            else:
                expenses_per_category[chosen_category] += amount
                print("Saved", amount, "for", chosen_category)
                break
        except ValueError:
            print("This is not a number. Please try again.")


def add_new_category(categories, expenses_per_category):
    """Add a completely new category (with optional first expense)."""
    print("\n2) New category")
    prompt = "Enter new category name OR '0' to return: "
    new_cat = input(prompt).strip()

    if new_cat == "0":
        return

    if new_cat == "":
        print("Category name cannot be empty.")
    elif new_cat in categories:
        print("Category already exists.")
    else:
        categories.append(new_cat)
        expenses_per_category[new_cat] = 0.0
        print("New category added:", new_cat)

        while True:
            prompt = (
                "Enter your first expense for " + new_cat +
                " (or press Enter to skip): "
            )
            amount_input = input(prompt).strip()

            if amount_input == "":
                print("No expense entered for", new_cat)
                break

            try:
                amount = float(amount_input)
                if amount < 0:
                    print("Expense cannot be negative. Please try again.")
                else:
                    expenses_per_category[new_cat] += amount
                    print("Saved", amount, "for", new_cat)
                    break
            except ValueError:
                print("This is not a number. Please try again.")


def delete_or_clear_category(categories, expenses_per_category):
    """
    Let the user delete a category completely
    or clear all expenses of a category.
    """
    if not categories:
        print("No categories to modify.")
        return

    print("\n4) Delete category or clear its expenses")
    idx = choose_category(categories)
    if idx is None:
        return

    chosen_category = categories[idx]

    print("\nWhat do you want to do with", chosen_category, "?")
    print("1. Delete category completely")
    print("2. Clear all expenses in this category")
    sub_choice = input("Please enter 1 or 2: ")

    if sub_choice == "1":
        del categories[idx]
        del expenses_per_category[chosen_category]
        print("Category deleted:", chosen_category)
    elif sub_choice == "2":
        expenses_per_category[chosen_category] = 0.0
        print("All expenses for", chosen_category, "have been cleared.")
    else:
        print("Invalid choice.")
