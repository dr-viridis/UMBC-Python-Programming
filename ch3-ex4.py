#!/usr/bin/env python3
firstnum = int(input("Please enter the first number:"))
secondnum = int(input("Please enter the second number:"))
sum = 0
# Hmm, do I need to sort? Seems like counting up or down should 
# produce the same result, right?

for index in range(firstnum, secondnum):
    sum = sum + index
sum = sum + secondnum #not counted in the final loop?
print("The inclusive sum is", sum)
