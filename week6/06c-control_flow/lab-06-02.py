#!/usr/bin/env python3

"""
A program that loads a list of integers as a string (all the numbers are
separated by a single comma) and prints the frequency of each digit.
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
    if x == 0:
        # A zero has one digit (a zero), but it would go unnoticed
        # in our general algorithm, so we handle this case separately
        freqs[0] += 1
        continue
    x = abs(x)
    while x > 0:
        freqs[x%10] += 1
        x //= 10

# Print the result
for d, cnt in enumerate(freqs):
    if cnt >= 2:
        print("A digit {} has appeared {} times.".format(d, cnt))
    elif cnt == 1:
        print("A digit {} has appeared once.".format(d))
    else:
        print("A digit {} has appeared in none of the numbers.".format(d))

