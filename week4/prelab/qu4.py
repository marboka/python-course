# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bisearch(x,n):
    
    index = list()
    for i in range (1, len(x) + 1):
        index.append(i)
    print (index)
    i=0
    ii=0
    while len(x) >= 1:        
        if x[len(x)//2] > n:
            x = x[0:(len(x)//2)+1] 
            index = index[0:(len(index)//2)+1]
            ii += 1
        else:
            x = x[len(x)//2:len(x)+1] 
            index = index[len(index)//2:len(index)+1]
            ii += 1
            
        if x[0] == n:
            print('found it ',x[0], 'index: ' ,index[0])
            return True
            
        if ii == i:             
            return False
        

def main():
    x=[11,12,13,14,15,16,17,18,19]
    n=5

    print(bisearch(x,n))
    return
    
main()
