#!/usr/bin/env python3

# sum equivalent that takes a variable number of arguments
# needs to be updated to return a tuple to the calling function

def my_sum(*args):
    """ Returns a tuple consisting of the total and 
    mean of the elements provided to it"""
    total = 0
    mean = 0
    for elem in args:
        total += elem
    mean = total/(len(args))
#    print(total, mean)
    my_tuple = (total, mean)
    return my_tuple

print("Doc string:", my_sum.__doc__)

#dons_tuple = (0,0)
dons_tuple = my_sum(2, 3, 40)

print("mean = ", dons_tuple[1], "total = ", dons_tuple[0])

# below doesn't use enumerate correctly!
#for total, mean in enumerate(dons_tuple):
#    print("mean = ", mean, "total = ", total)

#dons_total = my_sum(2, 3, 40)
#print(dons_total)
