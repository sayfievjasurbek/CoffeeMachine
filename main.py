from random import choice

from debugpy.launcher import channel
from prompt_toolkit.filters import is_read_only
from pygments.lexers import ml

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,  # Added money to track earnings


}

def is_resource_sufficient(order_incredients):
    """Returns True when order can be made, False otherwise."""
    for item in order_incredients:
        if  order_incredients[item] >= resources[item]:
            print(f"Sorry the is not enough {item} ")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_succesfull(money_recieved, drink_cost):
    """Return true when the payment is accepted , or false otherwise"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is $ {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money.Money refunded")
        return False
def make_coffee(drink_name, order_incredients):
    """Goal of this function deduct the required ingredients from resources"""
    for item in order_incredients:
        resources[item] -= order_incredients[item]
    print(f"Here is your {drink_name}  ☕️")


is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']} ")
        print(f"Money: {resources['money']}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])














