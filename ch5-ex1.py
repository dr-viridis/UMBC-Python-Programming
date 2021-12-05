#!/usr/bin/env python3

# function prompts for positive integer
# validates info, returns integer if valid, returns 0 if not
# application (not function) indicates error

def input_function():
    integer = int(input("Give me a positive integer, please: "))
    if (integer > 0):
        return(integer)
    else:
        return(0)

result = input_function()
if result != 0:
    print("Your integer was:", result)
else:
    print("You gave an invalid number!")
