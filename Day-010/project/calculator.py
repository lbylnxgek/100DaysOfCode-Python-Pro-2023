from art import logo


def add(n1, n2):
    """Add two numbers and return the result"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers and return the result"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers and return the result"""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers and return the result"""
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    """Perform addition, subtraction, multiplication or division on two numbers."""
    print(logo)
    num1 = int(input("What's the first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number: "))
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation or 'q' to quit: "
        )
        if should_continue == "y":
            num1 = answer
        elif should_continue == "n":
            more_numbers = False
            calculator()
        else:
            more_numbers = False
            print("\nThank you for using the Python calculator.  End of Line.")
            exit()


calculator()
