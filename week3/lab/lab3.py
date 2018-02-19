# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
WARNING
it only has to print either the left or the right digit
if it gets 2 input, it gives in error,
have to use defualt none value i think
'''
def get_digit(n,left,right):
    nlist=[int (i) for i in str(n)]
    nlenght=len(n)
    if left < 1:
        return -1
        
    output=[nlist[left-1],nlist[-right]]
    return output
    
    
def main():
    n=int(input("n: "))
    left=int(input("left: "))
    right=int(input("right: "))
    print(get_digit(n,left,right))
    
main()    