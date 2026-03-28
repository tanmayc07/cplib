import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for i in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
    
    neg = a.count(-1)
    pos = a.count(1)
    curr = 0
    
    while neg > pos:
        neg -= 1
        pos += 1
        curr += 1
    
    if neg%2 == 0: print(curr)
    else: print(curr+1)
    
'''
We need to calculate the number of flips to make count of -1s 
equal or less than 1s and then depending on the parity of 
negative numbers, we might need to add 1 more flip.
'''
