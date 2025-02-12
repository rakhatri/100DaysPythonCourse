from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)

