# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def print_report():
    """Prints current resource values"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(drink):
    """Checks if there are enough resources to make the drink"""
    ingredients = MENU[drink]["ingredients"]
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Prompts user to insert coins and returns the total amount"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def check_transaction(money_received, drink_cost):
    """Checks if payment is enough and handles change"""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True


def make_coffee(drink):
    """Deducts ingredients and serves coffee"""
    ingredients = MENU[drink]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    """Main coffee machine loop"""
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if check_transaction(payment, MENU[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please try again.")


# Run the coffee machine
coffee_machine()
