# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:51:21 2018

@author: msra4bm8
"""


import math
def binom (n, k):
    '''
    calcualtes the binomial coefficient of `n` over `k`
    input: `n` and `k` both integers
    output: integer
    '''    
    if n<0 or k<0:
        return 0
    coeff=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return int(coeff)
    
def binomf (n, k):
    '''
    calcualtes the binomial coefficient of `n` over `k`
    input: `n` and `k` both integers
    output: float
    '''    
    if n<0 or k<0:
        return 0
    coeff=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return coeff
    
def main():
    n=5
    k=2
    print(binom(n,k))
    print(binomf(n,k))
    
main()
    