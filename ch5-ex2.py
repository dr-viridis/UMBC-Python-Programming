#!/usr/bin/env python3

# take a collection of strings, return the length of the longest

def measure_length(collection):
    longest = 0
    for strings in collection:
        print("Current string is", strings)
#        print("And it is ", len(strings), "long")
#        print("Current longest is", longest)
        if len(strings) > longest:
            longest = len(strings)
#            print("Updated length, to ", longest)
    return(longest)



my_collection = ["hello world", "hi there", "a", "ren was my cat"]

longest = measure_length(my_collection)
print("Longest string was ", longest, "characters long")
