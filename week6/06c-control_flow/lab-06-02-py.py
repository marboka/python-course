#!/usr/bin/env python3

"""
A (more) Pythonic solution for Problem 6.2.
"""

# Load a list of numbers, repeating the request in case of an input error
while True:
    try:
        numbers = input("A comma-separated list of numbers: ")
        numbers = [ int(x) for x in numbers.split(",") ]
        break
    except ValueError:
        pass

# Count the digits' frequencies
freqs = [ 0 for d in range(10) ]
for x in numbers:
    for d in str(abs(x)):
        freqs[int(d)] += 1

# Print the result
for d, cnt in enumerate(freqs):
    if cnt >= 2:
        print("A digit {} has appeared {} times.".format(d, cnt))
    elif cnt == 1:
        print("A digit {} has appeared once.".format(d))
    else:
        print("A digit {} has appeared in none of the numbers.".format(d))

