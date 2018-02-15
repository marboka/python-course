# -*- coding: utf-8 -*-

def sd(n):
    '''
    returns the sum of the digits of the input integer
    input: `n` integer
    output: integer(sum of digits)
    '''
    sum_d=0
    while n>0:
        last_d=n%10
        n=n//10
        sum_d=sum_d+last_d
    return sum_d

def main():
    '''
    ask for a number a numbers (m)
    adds the digits of those m numbers
    multiplies the added digits
    adds the digits of the number defined by the multiplication
    input: 
            `m` number of number
            `mm` each endependent number
    output:
            integer
    '''
    m=int(input("how many numbers do you want: "))
    cnt=0
    product=1
    while cnt<m:
        mm=int(input("number: "))
        cnt+=1
        product=product*sd(mm)
    print(sd(product))    

main()