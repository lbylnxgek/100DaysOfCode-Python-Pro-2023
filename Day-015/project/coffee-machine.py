from data import MENU, resources
DEBUG = False
cashbox = 0.00


def check_coffee_level(order):
    """Returns True if coffee level is enough to make order, otherwise returns False"""
    coffee_available = resources["coffee"]
    coffee_order = MENU[order]["ingredients"]["coffee"]
    if DEBUG:
        print(f"DEBUG: Checking coffee: available ({coffee_available}) - order ({coffee_order})")
    if coffee_available - coffee_order >= 0:
        if DEBUG:
            print("DEBUG: Coffee available = True")
        return True
    else:
        if DEBUG:
            print("DEBUG: Coffee available = False")
        return False


def check_water_level(order):
    """Returns True if water level is enough to make order, otherwise returns False"""
    water_available = resources["water"]
    water_order = MENU[order]["ingredients"]["water"]
    if DEBUG:
        print(f"DEBUG: Checking water: available ({water_available}) - order ({water_order})")
    if water_available - water_order >= 0:
        if DEBUG:
            print("DEBUG: Water available = True")
        return True
    else:
        if DEBUG:
            print("DEBUG: Water available = False")
        return False


def check_milk_level(order):
    """Returns True if milk level is enough to make order, otherwise returns False"""
    milk_available = resources["milk"]
    milk_order = MENU[order]["ingredients"]["milk"]
    if DEBUG:
        print(f"DEBUG: Checking milk: available ({milk_available}) - order ({milk_order})")
    if milk_available - milk_order >= 0:
        if DEBUG:
            print("DEBUG: Milk available = True")
        return True
    else:
        if DEBUG:
            print("DEBUG: Milk available = False")
        return False


def insert_coins(item_cost):
    """Prompts the user to insert coins.  Returns true if user inserts enough money and gives a refund if necessary."""
    print("Please insert coins.")
    quarters = int(input("  How many quarters? "))
    dimes    = int(input("  How many dimes? "))
    nickles  = int(input("  How many nickles? "))
    pennies  = int(input("  How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if DEBUG:
        print(f"Item cost: {item_cost:.2f}")
        print(f"DEBUG: q={quarters}, d={dimes}, n={nickles}, p={pennies} = {total:.2f}")

    if total > item_cost:
        refund = total - item_cost
        if DEBUG:
            print(f"DEBUG: Refund of {refund:.2f} due.")
        print(f"Please take your change of ${refund:.2f}")
        return True
    elif total == item_cost:
        if DEBUG:
            print("DEBUG: Exact change.")
        return True
    else:
        shortage = item_cost - total
        if DEBUG:
            print(f"DEBUG: Shortage of {shortage}.")
        print(f"Sorry, that's not enough money, refunding ${total:.2f}.")


def brew_coffee(order):
    """Brews the order, adds to the cashbox and subtracts from resources."""
    global cashbox
    global resources

    # Add order cost to cashbox
    if DEBUG:
        print(f"DEBUG: Current cashbox: {cashbox}")
        print(f"DEBUG: Adding {MENU[order]["cost"]} to cashbox")
    cashbox += MENU[order]["cost"]
    if DEBUG:
        print(f"DEBUG New cashbox amount = {cashbox}")

    # Subtract resources used
    if DEBUG:
        print(f'DEBUG: Current resources: c:{resources["coffee"]}, w:{resources["water"]}, m:{resources["milk"]}')
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    if DEBUG:
        print(f'DEBUG: Subtracting {MENU[order]["ingredients"]["coffee"]} from coffee.')
    resources["water"] -= MENU[order]["ingredients"]["water"]
    if DEBUG:
        print(f'DEBUG: Subtracting {MENU[order]["ingredients"]["water"]} from water.')
    if order == "latte" or order == "cappuccino":
        if DEBUG:
            print(f'DEBUG: Subtracting {MENU[order]["ingredients"]["milk"]} from milk.')
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    if DEBUG:
        print(f'DEBUG: New resources: c:{resources["coffee"]}, w:{resources["water"]}, m:{resources["milk"]}')

    print(f"Please enjoy your ☕ {order}!")
    order_coffee()


def order_coffee():
    """Coffee machine main routine"""
    print("\nWelcome to the Sirius Cybernetics Corporation coffee machine.")
    print("Available beverages are:")
    print("  - Espresso - $1.50")
    print("  - Latte - $2.50")
    print("  - Cappuccino - $3.00")
    order = input("What would you like to drink (espresso/latte/cappuccino)? ").lower()

    if order == "report":
        print("\nCurrent supply levels are:")
        print(f"  Coffee: {resources['coffee']}g")
        print(f"  Water: {resources['water']}ml")
        print(f"  Milk: {resources['milk']}ml")
        print(f"  Money: ${cashbox:.2f}")
        order_coffee()
    elif order == "off":
        print("\nPowering off.")
        exit()
    elif order == "espresso":
        if check_coffee_level(order):
            if check_water_level(order):
                if DEBUG:
                    print("Ok to brew!")
            else:
                print("\nSorry, not enough water.")
                order_coffee()
        else:
            print("\nSorry, not enough coffee.")
            order_coffee()
    elif order == "latte":
        if check_coffee_level(order):
            if check_water_level(order):
                if check_milk_level(order):
                    if DEBUG:
                        print("Ok to brew!")
                else:
                    print("\nSorry, not enough milk.")
                    order_coffee()
            else:
                print("\nSorry, not enough water.")
                order_coffee()
        else:
            print("\nSorry, not enough coffee.")
            order_coffee()
    elif order == "cappuccino":
        if check_coffee_level(order):
            if check_water_level(order):
                if check_milk_level(order):
                    if DEBUG:
                        print("Ok to brew!")
                else:
                    print("\nSorry, not enough milk.")
                    order_coffee()
            else:
                print("\nSorry, not enough water.")
                order_coffee()
        else:
            print("\nSorry, not enough coffee.")
            order_coffee()
    else:
        print("\nInvalid choice, please try again.")
        order_coffee()

    if insert_coins(MENU[order]["cost"]):
        if DEBUG:
            print("DEBUG: Sufficient coins inserted!")
        brew_coffee(order=order)
    else:
        order_coffee()


order_coffee()
