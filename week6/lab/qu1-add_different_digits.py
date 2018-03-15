# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def load_integers():
    ''' 
    loads integers, stops when n=0
    '''
    lst = list()
    while True:
        try:
            n = int(input('integer: '))
            if n == 0:
                break
            lst.append(n)
        except ValueError:
            print('thats not an integer')
        
    return lst
    
def sum_from_right(L):
    counter = 1 
    while True:
        summ = 0
        done = True
        for i in range (0, len(L)):
            if L[i] >  0:
                done = False
                summ = summ + L[i] % 10
                L[i] = L[i] // 10 
        if done:
            break
        print ('the sum of the {}. digits from the right: {}'.format(counter,summ))
        counter += 1
        
def main():
    sum_from_right(load_integers())
    return
    
main()