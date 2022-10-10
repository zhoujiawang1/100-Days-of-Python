from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    coffee = input(f"What coffee would you like? ({menu.get_items()}): ")
    if coffee == "c_report":
        machine.report()
    elif coffee == "m_report":
        money_machine.report()
    else:
        drink = menu.find_drink(coffee)
        if drink:
            if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                machine.make_coffee(drink)
