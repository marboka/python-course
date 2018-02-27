#WARNING
#i think for (888,1) it should give 32 but it gives 5 
#which is r=2


def sd(n):
    """
    Returns the sum of digits of a natural number `n`.
    Used as an auxiliary function to `sdr`.
    """
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def sdr(n,r=None):
    """
    If `r <= 0`, returns `n`.
    If `r > 0` returns `sd(sd(...sd(n)...))`, where `sd` is applied `r` times.
    If `r` is undefined, returns the fixed point of `sd(sd(...sd(n)...))`, which
    is the first single-digit number that this composition encounters.
    """
    n = abs(n)    
    
    if r is None:
        while n > 10:
            n = sd(n)
        return n
                
    if r<=0:
        return n
        
    for i in range(n):
        n = sd(n)
    return n
        
    
    
def main():
    n = 8888
    r = 1
    print(sd(n))
    print("sdr(" + str(n) + ", " + str(r) + ") =", sdr(n, r))
    print("sdr(" + str(n) + ") =", sdr(n))
     

main()
