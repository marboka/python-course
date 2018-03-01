# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:32:32 2018

@author: msra4bm8
"""

def load_a_list_of_ints():
    """
    Loads a list of integers by first asking for its length.
    """
    L = list()
    n = int(input("The number of list elements: "))
    for k in range(n):
        L.append(int(input(str(k+1) + ". element: ")))
    return L
    
def my_sort(x):
    y=list()
    lenght=len(x)
    for i in range(0,n-1):
        left = i
        for ii in range(left+1, lenght):
            if L[left] > x[ii]:
            left = ii
        y.append(i)
        lenght = lenght - 1
                
    return y
    
def main():
    x=[1,2,5,4]
    print(my_sort(x))
    return
    
main()