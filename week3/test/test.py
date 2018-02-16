"""
Full name: Botond Maros
StudentId: 9770358
Email: botond.maros@student.manchester.ac.uk
"""

def digitval(n):
    biggest=0
    n=abs(n)
    while n>1:
        last_d=n%10
        if last_d>biggest:
            biggest=last_d
        n=n//10
    return biggest
    
def digitpos(n):
    biggest = 0
    index = 1
    n = abs(n)
    while n>1:
        power = len(str(n))
        first_digit = n // 10**(power-1)
        if first_digit >= biggest:
            biggest = first_digit
            index = index + 1
        n = n % 10**(power-1)
    return index
   
   

def main():
    print(digitpos(1776))

main()

