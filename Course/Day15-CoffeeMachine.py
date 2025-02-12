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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_ingredients(type_of_coffee):
    if resources["water"] >= MENU[type_of_coffee]['ingredients']['water']:
        if resources["coffee"] >= MENU[type_of_coffee]['ingredients']['coffee']:
            if type_of_coffee != 'espresso':
                if resources["milk"] >= MENU[type_of_coffee]['ingredients']['milk']:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                return True
        else:
            print("Sorry there is not enough coffee.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def insert_coins():
    print("Please insert coins.")
    num_of_quarters = float(input("how many quarters?: "))
    num_of_dimes = float(input("how many dimes?: "))
    num_of_nickles = float(input("how many nickles?: "))
    num_of_pennies = float(input("how many pennies?: "))
    return num_of_quarters * 0.25 + num_of_dimes * 0.1 + num_of_nickles * 0.05 + num_of_pennies * 0.01


def process_money(type_of_coffee):
    money_deposited = insert_coins()
    if money_deposited >= MENU[type_of_coffee]['cost']:
        resources['money'] += MENU[type_of_coffee]['cost']
        balance = money_deposited - MENU[type_of_coffee]['cost']
        print(f"Here is ${round(balance,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(type_of_coffee):
    resources['water'] -= MENU[type_of_coffee]['ingredients']['water']
    resources['coffee'] -= MENU[type_of_coffee]['ingredients']['coffee']
    if type_of_coffee != 'espresso':
        resources['milk'] -= MENU[type_of_coffee]['ingredients']['milk']
    print(f"Here is your {type_of_coffee}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        get_report()
    else:
        if check_ingredients(choice):
            if process_money(choice):
                make_coffee(choice)
