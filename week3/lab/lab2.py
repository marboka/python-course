# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:05:54 2018

@author: msra4bm8
"""
    
    
def sdn(n,r=None):
    '''
    returns the sum of the digits of the input integer r times
    input: `n` integer, `r` integer
    output: integer(sum of digits)
    '''
    if r==None:
        while True:        
            sum_d=0        
            while n>0:          #basic sd fomr ex1
                last_d=n%10
                n=n//10
                sum_d=sum_d+last_d  
            r=r-1
            n=sum_d
            if sum_d<10:
                return sum_d
        
    elif r>0:    
        while r>0:
            sum_d=0         #at every round r the sum goes back to 0
            while n>0:
                #basic sd() from ex1
                last_d=n%10
                n=n//10
                sum_d=sum_d+last_d  
            r=r-1
            n=sum_d
        return sum_d
        
    elif r<=0:
        return n
    
def main():
    b=int(input("give the number of rounds: "))
    a=int(input("give the number: "))
    if b<=0:
        print (a)
    
    else: 
        print(sdn(a,b))
     

main()