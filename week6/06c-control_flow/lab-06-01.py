#!/usr/bin/env python3

"""
A program that loads a list of integers until it loads a zero
(which does not get added to the list). The program then prints
the sums of all rightmost digits, all the second to rightmost ones, etc.
"""

# Input
numbers = list()
k = 1
while True:
    try:
        n = int(input("{}. number: ".format(k)))
    except ValueError:  # Do NOT use empt except, as it disables Ctrl+C
        continue
    if n == 0:
        break
    k += 1
    # We don't need the numbers, but their digits, so we save
    # their absolute values to the list
    numbers.append(abs(n))

# Count by removing the last digit of each number
cnts = list()
while True:
    done = True  # True unless we encounter a non-zero
    current_cnt = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            done = False
            current_cnt += numbers[i] % 10
            numbers[i] //= 10
    if done:
        break
    else:
        cnts.append(current_cnt)

# Display the results
for i, cnt in enumerate(cnts, start=1):
    print("The sum of the {}. digits from the right: {}".format(i, cnt))

