from menu import resources, MENU

quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01


def turn_off():
    exit()


def print_espresso():
    print("Espresso:", resources["espresso"])


def print_latte():
    print("Latte:", resources["latte"])


def print_cappuccino():
    print("Cappuccino:", resources["cappuccino"])


def machine_report():
    print("Resources:")
    for item, quantity in resources.items():
        print(f"{item.capitalize()}: {quantity}")


def calculate_cost(coffee_type):
    coffee_cost = MENU[coffee_type]["cost"]
    print(f"The cost of {coffee_type.capitalize()} is ${coffee_cost:.2f}")

    quarters_inserted = int(input("How many quarters? "))
    dimes_inserted = int(input("How many dimes? "))
    nickels_inserted = int(input("How many nickels? "))
    pennies_inserted = int(input("How many pennies? "))

    total_inserted = (quarters_inserted * quarters) + (dimes_inserted * dimes) + \
                     (nickels_inserted * nickels) + (pennies_inserted * pennies)

    if total_inserted >= coffee_cost:
        change = total_inserted - coffee_cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        return True
    else:
        print("Insufficient funds. Please insert more coins.")
        return False


def make_coffee(coffee_type):
    if calculate_cost(coffee_type):
        ingredients = MENU[coffee_type]["ingredients"]
        for ingredient, required_amount in ingredients.items():
            if required_amount > resources.get(ingredient, 0):
                print(f"Insufficient {ingredient}. Cannot make a {coffee_type.capitalize()}.")
                return False
            else:
                resources[ingredient] -= required_amount
        print(f"Making {coffee_type.capitalize()}. Enjoy your coffee!")
        return True
    return False


print("Coffee Machine")

while True:
    option = input("What would you like? (espresso/latte/cappuccino/turn off)?\nFor a report, type 'report': ")

    if option == 'report':
        machine_report()

    elif option == 'espresso':
        if make_coffee("espresso"):
            print("The coffee was made successfully")

    elif option == 'latte':
        if make_coffee("latte"):
            print("The coffee was made successfully")

    elif option == 'cappuccino':
        if make_coffee("cappuccino"):
            print("The coffee was made successfully")

    elif option == 'turn off':
        turn_off()

    else:
        print("Invalid option. Please choose from 'espresso', 'latte', 'cappuccino', or 'turn off'.")
