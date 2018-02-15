# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:36:52 2018

@author: msra4bm8
"""

def max_digit(n,d=1,r=0):
    '''
    gives the max digit of `n` that gives remainder `r` when divided by `d`
    input:
            n (integer) - our number
            d (integer) - the one with we are diving with
            r (integer) - the remainder after n%d
    output:
            integer between 1 and 9
    '''
    max_d=0
    while n>9:
        last_d=n%10
        if last_d%d==r and last_d>max_d:
            max_d=last_d
        n=n//10
    return max_d
    
def main():
    n=123412
    d1=2
    r1=1
    print(max_digit(n))
    print(max_digit(n,d1))
    print(max_digit(n,d1,r1))
    
main()