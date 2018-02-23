# -*- coding: utf-8 -*-


def get_len(n):
    """
    Returns the length of a natural number `n`.
    """
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res


def digit (n,k):
    if k<=0:
        return -1
    elif get_len(n)<k:
        return 0
    else:
        for _ in range(k - 1):
            n //= 10
        return n % 10
        

def mersenne(n):
    n=n+1
    m=1
    while m>0:
        if n == 2 ** m:
            return True
        if 2**m>n:
            return False
        else:
            m=m+1
        
    
    
    
    

def main():
    print(digit(12345,0))
    print(digit(12345,1))
    print(digit(12345,2))
    print(digit(12345,3))
    print(digit(12345,4))
    print(digit(12345,5))
    print(digit(12345,6))
    print(digit(12345,8))

    print(mersenne(31))
    print(mersenne(127))
    print(mersenne(30))
   

main()