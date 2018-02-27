#I SHOULD DO SOMETHING WITH THE DEFAULT NONE VALUES
'''
"""
Get the `k`-th left or right digit from a number.
"""
'''
def get_digit(n,left,right):
    # gets the lenght
    nlist=[int (i) for i in str(n)]
    nlenght=len(nlist)
    
    #errors
    if left is not None and left < 1:
        return -1
    
    if right is not None and right > nlenght:
        return 0
    
    if left is None and right is None:
        return -1
        
    if left is not None and right is not None:
        return -1
    
    #left is number, right is empty
    if left is not None and right is None:
        if left <= nlenght:
            return str(nlist[left-1])
        else: 
            return -1
    
    #right is number left is empty
    if left is None and right is not None:
        if right <= nlenght:
            return str(nlist[-right])
        else:
            return -1


#same thing with leff ifs
def get_digit_nice(n, left, right):
    # gets the lenght
    nlist=[int (i) for i in str(n)]
    nlenght=len(nlist)
    
    if left is None:
        if right is None:
            return -1
        if right > nlenght or right < 1:
            return -1
        return str(nlist[-right])
    else:
        if right is not None:
            return -1
        if left > nlenght or left < 1:
            return 0
        return str(nlist[left-1])
        
    
    
def main():
    n=4321
    left=None
    right=5
    print(get_digit_nice(n,left,right))
    
main()    
