#!/usr/bin/env python3

# sum equivalent that takes a variable number of arguments

def my_sum(*args):
    total = 0
    for elem in args:
        total += elem
    return total

dons_total = my_sum(2, 3, 4, 90, 5090)
print(dons_total)
