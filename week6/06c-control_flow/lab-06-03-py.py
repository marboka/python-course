#!/usr/bin/env python3

"""
A (bit more) Pythonic solution for Problem 6.3.
"""

# Load a list of numbers, repeating the request in case of an input error
text = input("A line of text: ")

# Count the digits' frequencies
freqs = dict()
for c in text:
    # `get(c)` returns `freqs[c]` if it exists and `None` otherwise
    # `get(c, default)` returns `freqs[c]` if it exists and default otherwise
    # See: https://docs.python.org/3/library/stdtypes.html#dict.get
    freqs[c] = freqs.get(c, 0) + 1

# Print the result
for c, cnt in freqs.items():
    if cnt >= 2:
        print("A character \"{}\" has appeared {} times.".format(c, cnt))
    else:  # cnt == 1, because 0 is impossible
        print("A digit \"{}\" has appeared once.".format(c))

