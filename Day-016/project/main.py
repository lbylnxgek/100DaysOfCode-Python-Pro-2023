from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_machine_on = True
while coffee_machine_on:
    available_drinks = menu.get_items()
    print("\nWelcome to the Sirius Cybernetics Corporation coffee machine.")
    selection = input(f"What would you like to drink({available_drinks})? ").lower()
    if selection == "off":
        coffee_machine_on = False
        print("\nPowering off...")
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"Your selection costs: ${drink.cost:.2f}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("\nInvalid selection, please try again.")
