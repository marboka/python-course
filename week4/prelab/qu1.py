# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:19:18 2018

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
    
    
def my_reverse(x):
    y=list()
    for i in range(len(x)-1, -1, -1):
        y.append(x[i])
    return y
    
def main():
    x=load_a_list_of_ints()
    print(my_reverse(x))
    return
main()