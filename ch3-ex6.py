#!/usr/bin/env python3
lower = int(input("Please enter the lower bound:"))
upper = int(input("Please enter the upper bound:"))
step = int(input("Please enter the step value:"))

for index in range(lower, upper, step):
    print(index)
print(upper) # fencepost for the for loop
