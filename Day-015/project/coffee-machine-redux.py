from data import MENU, resources

DEBUG = False
menu_items = []
menu_string = ""
cashbox = 0.00


def check_resources(order_ingredients):
    """Returns True if there are enough resources, False if not."""

    for item in order_ingredients:
        if DEBUG:
            print(
                f"  * DEBUG: Comparing item {item} order:{order_ingredients[item]} resources:{resources[item]}"
            )
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}, please try again.")
            return False
    return True


def insert_coins(order_cost):
    """Prompts the user to insert coins, gives change as necessary.  Returns True if enough money
    was inserted and adds to the cashbox. Otherwise returns False"""

    global cashbox

    print("Please insert coins.")
    quarters = int(input("  How many quarters? "))
    dimes = int(input("  How many dimes? "))
    nickles = int(input("  How many nickles? "))
    pennies = int(input("  How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if DEBUG:
        print(
            f"  * DEBUG: q={quarters}, d={dimes}, n={nickles}, p={pennies} = {total:.2f}"
        )
        print(f"  * DEBUG: Comparing total={total:.2f} order_cost={order_cost:.2f}")
        print(f"  * DEBUG: Current cashbox: {cashbox}")

    if total > order_cost:
        refund = total - order_cost
        if DEBUG:
            print(f"  * DEBUG: Refund of {refund:.2f} due.")
            print(f"  * DEBUG: Adding {order_cost} to cashbox")
        print(f"Please take your change of ${refund:.2f}")
        cashbox += order_cost
        if DEBUG:
            print(f"  * DEBUG New cashbox amount = {cashbox}")
        return True
    elif total == order_cost:
        if DEBUG:
            print("  * DEBUG: Exact change.")
            print(f"  * DEBUG: Adding {order_cost} to cashbox")
        cashbox += order_cost
        if DEBUG:
            print(f"  * DEBUG New cashbox amount = {cashbox}")
        return True
    else:
        shortage = order_cost - total
        if DEBUG:
            print(f"  * DEBUG: Shortage of {shortage}.")
        print(f"Sorry, that's not enough money, refunding ${total:.2f}.")
        return False


def brew_coffee(order_ingredients):
    """Brews the order and subtracts ingredients from resources."""

    global resources

    if DEBUG:
        print(f"  * DEBUG: order_ingredients={order_ingredients}")
        print(f"  * DEBUG: resources={resources}")

    for item in order_ingredients:
        if DEBUG:
            print(
                f"  * DEBUG: Subtracting item={item} quantity={order_ingredients[item]}"
            )
        resources[item] -= order_ingredients[item]
        if DEBUG:
            print(f"  * DEBUG: resources={resources}")


def coffee_menu():
    """Generates the global menu_items list, based on keys in MENU"""

    global menu_items
    for item in MENU:
        menu_items.append(item)
    menu_items.sort()
    if DEBUG:
        print(f"  * DEBUG: menu_items={menu_items}")


def print_menu_items():
    """Prints a formatted list of menu items"""

    for item in menu_items:
        print(f"  - {item.capitalize()} - ${MENU[item]['cost']:.2f}")


def format_menu_string():
    """Generates a formatted string of menu items, saved to global menu_string"""

    global menu_string
    for item in menu_items:
        menu_string += item
        menu_string += "/"

    # Trim trailing slash from string
    menu_string = menu_string[:-1]
    if DEBUG:
        print(f"  * DEBUG: menu_string={menu_string}")



def order_coffee():
    """Coffee machine main routine"""

    print("\nWelcome to the Sirius Cybernetics Corporation coffee machine.")
    print_menu_items()
    selection = input(f"What would you like to drink ({menu_string})? ").lower()

    if selection == "off":
        print("\nPowering off.")
        exit()
    elif selection == "report":
        print("\nCurrent supply levels are:")
        print(f"  Coffee: {resources['coffee']}g")
        print(f"  Water: {resources['water']}ml")
        print(f"  Milk: {resources['milk']}ml")
        print(f"  Money: ${cashbox:.2f}")
        order_coffee()
    elif selection in menu_items:
        drink = MENU[selection]
        if DEBUG:
            print(f"  * DEBUG: order={selection} drink={drink}")
        if check_resources(order_ingredients=drink["ingredients"]):
            if DEBUG:
                print("  * DEBUG: Resources True")
            if insert_coins(drink["cost"]):
                if DEBUG:
                    print("  * DEBUG: Coins True")
                brew_coffee(order_ingredients=drink["ingredients"])
                print(f"Here is your {selection} ☕ !")
                print(
                    "Thank you for using a Sirius Cybernetics Corporation product. Share and enjoy!\n"
                )
                order_coffee()
            else:
                order_coffee()
        else:
            order_coffee()
    # Invalid choice, recycle to order_coffee()
    else:
        order_coffee()


coffee_menu()
format_menu_string()
order_coffee()
