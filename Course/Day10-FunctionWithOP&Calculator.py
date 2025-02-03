# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
# print(format_name("rahul", "KHATRI"))

from art import logo_calc


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculation(n1):
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    result =  operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continue_calc == 'y':
        calculation(result)


while True:
    print(logo_calc)
    n1 = float(input("What's the first number?: "))
    calculation(n1)
