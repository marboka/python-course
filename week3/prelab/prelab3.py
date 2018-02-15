# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:04:40 2018

@author: msra4bm8
"""

def prime(n):
    '''
    returns True if n is prime, False otherwise
    input: `n` integer
    ouput: Boolen
    '''
    divisor=0
    for i in range(1,n+1):
        if n%i==0:
            divisor=divisor+1
            print (divisor)
            
    if divisor>2:
        return False
    else:
        return True
    
def main():
    n1=2
    n2=3
    n3=8
    print (n1, prime(n1))
    print (n2, prime(n2))
    print (n3, prime(n3))
    
main()
