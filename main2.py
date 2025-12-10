import pickle  # für das Speichern/Laden der Daten-Strukturen


def greet_user():
    user_input = input("Welcome to BudgetPro! Please enter your name: ")
    if user_input == "":
        print("Name cannot be empty.")
        return
    try:
        float(user_input)
        print("This is not a valid name.")
        return
    except ValueError:
        print(f"Hello {user_input}!")


def print_menu():
    print("\n--- Budget Menu ---")
    print("1. Enter new expense for a category.")
    print("2. Enter a new category.")
    print("3. View summary.")
    print("4. Delete category or clear category expenses.")
    print("5. Save & Continue.")


def enter_income():
    while True:
        try:
            income = float(input("Please enter your income: "))
            print("Your income is", income)
            return income
        except ValueError:
            print("This is not a number. Please try again.")


def show_extra_return(extra_return):
    print("\n")
    for i, cat in enumerate(extra_return, start=0):
        print(f"{i}. {cat}")


def show_categories(categories):
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")


def show_budget(income, expenses_per_category):
    total_expenses = sum(expenses_per_category.values())
    print("\n=== BUDGET SUMMARY ===")
    print("Your income is:", income)
    print("Your total expenses are:", total_expenses)

    difference = income - total_expenses
    print("Your budget difference is:", difference)

    if difference > 0:
        print("You are under budget.")
    elif difference < 0:
        print("You are over budget.")
    else:
        print("Your budget is balanced.")

    return total_expenses, difference


def save_summary_to_file(income, expenses_per_category, total_expenses, difference, filename):
    file = open(filename, "w")

    file.write("BUDGET SUMMARY\n")
    file.write("-----------------\n")
    file.write("Income: " + str(income) + "\n")
    file.write("\nExpenses by category:\n")
    for cat, amount in expenses_per_category.items():
        file.write(f"- {cat}: {amount}\n")

    file.write("\nTotal expenses: " + str(total_expenses) + "\n")
    file.write("Difference (income - expenses): " + str(difference) + "\n")

    if difference > 0:
        file.write("Status: You are under budget.\n")
    elif difference < 0:
        file.write("Status: You are over budget.\n")
    else:
        file.write("Status: Your budget is balanced.\n")

    file.close()
    print("Summary saved to", filename)


def save_data_to_pickle(income, categories, expenses_per_category, data_filename):
    # speichert die Daten-Struktur für den Monat
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
    # versucht, bestehende Daten zu laden (für den Monat)
    try:
        file = open(data_filename, "rb")
        data = pickle.load(file)
        file.close()
        print("Existing data loaded from", data_filename)
        return data
    except FileNotFoundError:
        # kein File vorhanden -> neuer Monat
        return None


def init_expenses_for_all_categories(categories, expenses_per_category):
    print("\nNow we will go through your main categories once.")
    print("If you have no expense for a category, just press Enter.")

    for category in categories:
        while True:
            user_input = input("Enter your expense for " + category + " (or press Enter to skip): ").strip()

            if user_input == "":
                # keine Eingabe -> 0 lassen, weiter
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


def main():
    greet_user()

    # Monat/Jahr für diese Budget-Datei abfragen
    period = input("Enter year and month for this budget (e.g. 2025-11): ").strip()
    if period == "":
        # Fallback, falls User nichts eingibt
        period = "unknown-period"

    data_filename = "BudgetPro_" + period + ".dat"  # pickle-Datei
    text_filename = "BudgetPro_" + period + ".txt"  # Text-Report

    # Versuch, bestehende Daten zu laden
    loaded_data = load_data_from_pickle(data_filename)

    if loaded_data is not None:
        # ➜ Zweiter (oder weiterer) Run für diesen Monat:
        income = loaded_data["income"]
        categories = loaded_data["categories"]
        expenses_per_category = loaded_data["expenses_per_category"]
        print("\nContinuing with existing budget data for", period)
    else:
        # ➜ Erster Run für diesen Monat:
        print("\nStarting a new monthly budget for", period)
        income = enter_income()

        # Standard-Kategorien
        categories = ["rent", "food", "subscriptions", "transport", "other expenses"]
        expenses_per_category = {cat: 0.0 for cat in categories}

        # Einmal durch alle Kategorien gehen:
        init_expenses_for_all_categories(categories, expenses_per_category)

    # Extra-Menüzeile für "return"
    extra_return = ["RETURN TO BUDGET MENU."]

    while True:
        print_menu()
        choice = input("\nPlease enter a number from the menu: ")

        if choice == "1":
            # Enter new expense for a category
            if not categories:
                print("No categories available. Please add a new category first (option 2).")
                continue

            show_extra_return(extra_return)
            show_categories(categories)
            selected = input("Please choose a category number (or 0 to return): ")

            if selected == "0":
                # zurück ins Hauptmenü
                continue

            if selected.isdigit():
                idx = int(selected) - 1
                if 0 <= idx < len(categories):
                    chosen_category = categories[idx]
                    while True:
                        amount_input = input(f"Enter your expense for {chosen_category}: ")
                        try:
                            amount = float(amount_input)
                            if amount <= 0:
                                print("Expense must be greater than 0. Please try again.")
                            else:
                                expenses_per_category[chosen_category] += amount
                                print(f"Saved {amount} for {chosen_category}.")
                                break
                        except ValueError:
                            print("This is not a number. Please try again.")
                else:
                    print("Invalid category number.")
            else:
                print("Please enter a number.")

        elif choice == "2":
            print("\n2) New category")
            two_choice_sub = input("Enter new category name OR '0' to return: ").strip()

            if two_choice_sub == "0":
                # zurück ins Hauptmenü
                continue

            new_cat = two_choice_sub

            if new_cat == "":
                print("Category name cannot be empty.")
            elif new_cat in categories:
                print("Category already exists.")
            else:
                categories.append(new_cat)
                expenses_per_category[new_cat] = 0.0
                print("New category added:", new_cat)

                while True:
                    amount_input = input(f"Enter your expense for {new_cat}: ")
                    try:
                        amount = float(amount_input)
                        if amount < 0:
                            print("Expense cannot be negative. Please try again.")
                        else:
                            expenses_per_category[new_cat] += amount
                            print(f"Saved {amount} for {new_cat}.")
                            break
                    except ValueError:
                        print("This is not a number. Please try again.")

        elif choice == "3":
            # View summary
            total_expenses, difference = show_budget(income, expenses_per_category)

        elif choice == "4":
            # Kategorie löschen oder Kosten einer Kategorie zurücksetzen
            if not categories:
                print("No categories to modify.")
                continue

            print("\n4) Delete category or clear its expenses")
            show_categories(categories)
            print("0. Return to main menu")

            selected = input("Choose a category number to modify (or 0 to return): ")

            if selected == "0":
                continue

            if selected.isdigit():
                idx = int(selected) - 1
                if 0 <= idx < len(categories):
                    chosen_category = categories[idx]
                    print("\nWhat do you want to do with", chosen_category, "?")
                    print("1. Delete category completely")
                    print("2. Clear all expenses in this category")
                    sub_choice = input("Please enter 1 or 2: ")

                    if sub_choice == "1":
                        # Kategorie komplett löschen
                        del categories[idx]
                        del expenses_per_category[chosen_category]
                        print("Category deleted:", chosen_category)
                    elif sub_choice == "2":
                        # Ausgaben auf 0 setzen
                        expenses_per_category[chosen_category] = 0.0
                        print("All expenses for", chosen_category, "have been cleared.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid category number.")
            else:
                print("Please enter a number.")

        elif choice == "5":
            # Save & Continue (Programm bleibt laufen)
            total_expenses, difference = show_budget(income, expenses_per_category)

            # Textfile pro Monat (z.B. BudgetPro_2025-11.txt)
            save_summary_to_file(income, expenses_per_category,
                                 total_expenses, difference, text_filename)

            # pickle-Datei mit allen Daten, damit der Monat beim nächsten Start weitergeht
            save_data_to_pickle(income, categories, expenses_per_category, data_filename)

            print("\nData saved successfully! Returning to main menu...\n")
            continue

        else:
            print("Invalid choice.")


# Start program.
main()
