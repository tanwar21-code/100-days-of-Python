# Coffee Machine Project

from resources import resources
from menu import MENU

def transaction(entry, cost):
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return False

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] += cost
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

def resource_check(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        print(f"Your {choice} will cost ${drink['cost']}")
        if resource_check(drink["ingredients"]):
            if transaction(choice, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please try again.")
