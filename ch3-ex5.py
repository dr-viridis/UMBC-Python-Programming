#!/usr/bin/env python3
sentence = input("Please enter a series of numbers, then hit return.")

# I guess we're treating it as a sentence (collection of words) first?

numbers = sentence.split(' ')  #should be a list of numbers? 
# and we're assuming good/legal input

for each_number in numbers:
    if int(each_number) > 0:
        print(each_number,"is greater than zero")
