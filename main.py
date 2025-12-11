from greet_user import greet_user
from budget_income_expenses import get_valid_period, load_or_init_budget
from menu import run_menu_loop


def main():
    """Entry point of the program."""
    greet_user()

    period = get_valid_period()

    income, categories, expenses_per_category, data_filename, text_filename = \
        load_or_init_budget(period)

    run_menu_loop(income, categories, expenses_per_category,
                  data_filename, text_filename)


if __name__ == "__main__":
    main()
