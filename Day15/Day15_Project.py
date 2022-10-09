from menu import *

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#TODO
'''
#1: print report how much ressrouces is left
#2 check if ressources are sufficient
'''

def print_report(resources):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml")

def calc_change(coffee):
    amount =MENU[coffee]['cost']
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters*COINS['quarter'] + dimes*COINS['dime'] + nickels*COINS['nickel'] + pennies*COINS['penny']

    return total - amount

def calc_remaning(resources, coffee):
    if "water" in MENU[coffee]['ingredients']:
        resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    if "milk" in MENU[coffee]['ingredients']:
        resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
    if "coffee" in MENU[coffee]['ingredients']:
        resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
    
    return resources

def check_resources(resources, coffee):
    if resources['water'] < 0 and resources['milk'] < 0 and resources['coffee'] < 0:
        return False
    else:
        return True

def enough_money(change):
    if change > 0:
        print(f"Here's {change} in change")
        return True
    else: 
        return False

while True:
    coffee = input("What would you like? (espresso/latte/cappucino): ")
    if coffee == 'report':
        print_report(resources)
    else:
        change = calc_change(coffee)
        if check_resources(resources, coffee) and enough_money(change):
            print(f"Here is your {coffee} and enjoy!")
            resources = calc_remaning(resources, coffee)
        else:
            print("Sorry that's not enough money. Money refunded")


#cappuccino
