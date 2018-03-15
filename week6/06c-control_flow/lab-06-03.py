#!/usr/bin/env python3

"""
A program that loads a line of text (i.e., a string) and prints
the frequencies of all of its characters.
"""

# Load a list of numbers, repeating the request in case of an input error
text = input("A line of text: ")

# Count the digits' frequencies
freqs = dict()
for c in text:
    if c in freqs:
        freqs[c] += 1
    else:
        freqs[c] = 1

# Print the result
for c, cnt in freqs.items():
    if cnt >= 2:
        print("A character \"{}\" has appeared {} times.".format(c, cnt))
    else:  # cnt == 1, because 0 is impossible
        print("A digit \"{}\" has appeared once.".format(c))

