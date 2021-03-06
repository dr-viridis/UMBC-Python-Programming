#!/usr/bin/env python3

# Calculator options: 1. add 2. subtract 3. multiply 4. divide 5.quit
# prompt user for 2 numbers, each action its own function

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def terminate():
    print("Thank you for using the calculator")
    exit()

def illegal():
    print("Illegal selection!\n")

data = []
menu = {"1": addition, "2": subtraction, "3": multiply, "4": divide, "5": terminate}
#keys = sorted(menu.keys())
while True:
    print("""Calculator options:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit""")
    choice = input("Please enter your choice: ")
    if (choice == "5"):
        exit()
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print("You have chosen ",menu[choice].__name__)
    result = menu.get(choice,illegal)(num1,num2)
    print(result)

