def greet_user():
    """Ask the user for their name and repeat until a valid name is entered."""
    while True:
        name = input("Welcome to BudgetPro! Please enter your name: ")

        if name == "":
            print("Name cannot be empty. Please try again.")
            continue

        # Check if the name is numeric
        try:
            float(name)
            print("This is not a valid name. Please try again.")
        except ValueError:
            print("Hello", name + "!")
            return name
