"""
Full name: Botond Maros
StudentId: 9770387
Lab class: B
Email: botond.maros@student.manchester.ac.uk
"""



def evenodd(L):
    even=list()
    odd=list()
    for i in range (0,len(L)):
        if L[i] % 2 == 0:
            even.append(L[i])
        else:
            odd.append(L[i])
    merged = list(reversed(even)) + sorted(odd)  
    
    return merged

def is_prime(n):
    """
    Returns `True` if `n` is prime, and `False` otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
    
def prime_slice(L, a, b):
    newlist=list()
    for i in range(a,b+1):
        if is_prime(L[i]):
            newlist.append(L[i])
            
    return newlist

def main():
    
    return

main()
    
