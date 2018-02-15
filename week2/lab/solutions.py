# Problem 1

from sys import exit
from math import sqrt, floor

"""
A program that loads one integer n, a digit d, and
two nonnegative integers a and b such that a>b,
verifies that the input satisfies these conditions,
and prints the largest integer x such that:
1. 0≤x≤n,
2. x is a perfect square of some integer
   (i.e., there exists y in Z such that x=y^2),
3. the last digit of x is d,
4. the remainder of the division of x by a is equal to b.
If there is no such number, the program prints
an appropriate message.
"""

n = int(input("n = "))
d = int(input("d = "))
a = int(input("a = "))
b = int(input("b = "))

if not (0 <= d <= 9 and a > b >= 0):
    print("The input is faulty.")
    # This stops the program execution, to avoid putting
    # all of the rest of the code inside `else`.
    # It requires the above `import` line and a nonnegative
    # integer argument (the zero would mean "exiting after
    # finishing the job successfully").
    exit(1)

max_x = None

for y in range(floor(sqrt(n))+1):
    x = y**2
    if x % 10 == d and x % a == b:
        max_x = x

if max_x is None:
    print("No such number exists!")
else:
    print("The desired number:", max_x)

#--------------------------------------------------------------

# Problem 2

"""
A program that loads n and prints how many integers x there are such that
* x is a perfect square,
* 1<x≤n,
* n is divisable by x.
"""

n = int(input("n = "))

y = 2
x = y**2
cnt = 0

while x <= n:
    if n % x == 0:
        cnt += 1
    y += 1
    x = y**2

print("Solution:", cnt)

#--------------------------------------------------------------

# Problem 3

"""
A program that loads a natural number n and prints how many ways are there
to write n as a sum of consecutive natural numbers (including the one-element
sum of n alone).
"""

n = int(input("n = "))
cnt = 0

for first in range(1, n+1):

    # Get the smallest sum `>= n` that starts from `first`
    sum_from_first = first
    k = first
    while sum_from_first < n:
        k += 1
        sum_from_first += k

    # Check that this sum is exactly `n` (and not more)
    if sum_from_first == n:
        cnt += 1
        # This part is not required by the problem at hand
        print("Found one:            ", end="")
        for i in range(first, k+1):
            if i > first:
                print("+", end="")
            print(i, end="")
        print()
        # A shorter version of the same output
        # (beyond what we've covered so far)
        print("Found one (Pythonic):", "+".join(str(x) for x in range(first, k+1)))

print("The number of such sums:", cnt)

#--------------------------------------------------------------

# Problem 4

"""
A program that loads two integers and computes their greatest common divisors
using the Euclid's algorithm (for example, the one from MATH10101) and
prints it.
"""

m = int(input("m = "))
n = int(input("n = "))

# We want to keep m, n for output
cm = abs(m)  # current m
cn = abs(n)  # current n

# If m < n, the first step will swap them
while cn > 0:
    r = cm % cn
    cm = cn
    cn = r

print("gcd(" + str(m) + ", " + str(n) + ") =", cm)

#--------------------------------------------------------------

# Problem 5

"""
A program that loads two integers and computes their lowest common multiplier.
We base this on the solution of Problem 2.4.
"""

m = int(input("m = "))
n = int(input("n = "))

# We want to keep m, n for output
cm = abs(m)  # current m
cn = abs(n)  # current n

# If m < n, the first step will swap them
while cn > 0:
    r = cm % cn
    cm = cn
    cn = r

# From lab-02-04.py
print("gcd(" + str(m) + ", " + str(n) + ") =", cm)

# |m| / gcd(m,n) <= lcm(m,n), so we avoid computing too big a number
# We use integer division because we know that |m| is divisible by gcd(m,n)
print("lcm(" + str(m) + ", " + str(n) + ") =", (abs(m) // cm) * abs(n))

#--------------------------------------------------------------

# Problem 6

"""
A program that loads a natural number and checks if it is a palindrome.
"""

n = int(input("n = "))

# Let us reverse the digits of `n`, while preserving `n` itself
t = n
rev = 0
while t > 0:
    rev = 10 * rev + t % 10
    t //= 10

print("rev n =", rev)
if n == rev:
    print("Number", n, "is a palindrome.")
else:
    print("Number", n, "is not a palindrome.")

#--------------------------------------------------------------

# Problem 7

"""
A program that loads a natural number and checks if its digits come in
1. a descending order (for example: 731, but not 331 or 713);
2. a non-increasing order (for example: 731 or 331, but not 713).
"""

n = int(input("n = "))
t = n  # Preserve the number for the output

# In order to compare two consecutive digits, we need to remember
# the previous one in each step.

# The last digit (the variable name is explained in the loop)
left_digit = t % 10
t //= 10

# To check if ALL items we observe satisfy a condition, we
# assume that they do and look for a counter-example.
digits_decreasing = True
digits_nonincreasing = True

while t > 0:
    right_digit = left_digit
    left_digit = t % 10
    t //= 10

    # `right_digit` used to be to the right of `left_digit` in the number.
    # So, `left_digit > right_digit` means that they are in a decreasing order.
    # Therefore, `left_digit <= right_digit` is a counter-example.
    if left_digit <= right_digit:
        digits_decreasing = False
    # Similarly, `left_digit >= right_digit` means that they are in a non-increasing order.
    # Therefore, `left_digit < right_digit` is a counter-example.
    if left_digit < right_digit:
        digits_nonincreasing = False

# After the number is done, check which conditions stayed `True` (i.e., there were
# no counter-examples).
if digits_decreasing:
    print("The digits of", n, "are decreasing.")
else:
    print("The digits of", n, "are not decreasing.")
if digits_nonincreasing:
    print("The digits of", n, "are nonincreasing.")
else:
    print("The digits of", n, "are not nonincreasing (i.e., there is an increment between at least two).")

#--------------------------------------------------------------

# Problem 8

"""
A program that loads a natural number and prints its
1. second digit from the left,
2. third digit from the right.
If the number doesn't have two/three digits, the respective digits are
considered to be zero.
"""

n = int(input("n = "))

# The second digit from the left can be obtained by removing all but two
# digits from the right and then taking the last one. The criterion is simple
# here: a nonnegative number has _at most_ two digits if it is <100.
# Don't forget the `abs`, since `n` is an integer (i.e., it can be negative).
t = abs(n)
if t < 10:
    # A nonnegative number `t` has less than two digits
    print("The number doesn't have the second digit from the left.")
else:
    while t > 99:
        # while `t` has more than two digits, remove the last one
        t //= 10
    # Now, only the leftmost two digits have remained; take the right one
    second_from_left = t % 10
    print("The second digit from the left:", second_from_left)

# The third digit from the right can be obtained by removing the last two
# digits and then taking the remaining last one.
# Here, we check the number of digits of `n`, to show that `abs` is
# not necessary for that check.
if -99 <= n <= 99:
    # An integer `n` has at most two digits
    third_from_right = 0
else:
    third_from_right = (abs(n) // 100) % 10

print("The third digit from the right:", third_from_right)

#--------------------------------------------------------------

# Problem 9

"""
Problem 9. Write a program that loads a natural number n and prints
Fibonacci numbers F0,F1,...,Fn.
"""

n = int(input("n = "))

print("F0 = 0")
print("F1 = 1")
Fk = 0   # F_k
Fk1 = 1  # F_{k+1}

# The last k that we need is the one for which `k+2 == n`, i.e.,
# `k == n-2`. Since range goes up to the top limit, but excludes it,
# we need that limit to be `n-1`.
for k in range(n-1):
    Fk2 = Fk1 + Fk
    print("F" + str(k+2) + " =", Fk2)
    Fk = Fk1
    Fk1 = Fk2
