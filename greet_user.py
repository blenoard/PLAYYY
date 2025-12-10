def greet_user():
    """Ask the user for their name and greet them."""
    user_input = input("Welcome to BudgetPro! Please enter your name: ")
    if user_input == "":
        print("Name cannot be empty.")
        return
    try:
        float(user_input)
        print("This is not a valid name.")
        return
    except ValueError:
        print("Hello", user_input + "!")
