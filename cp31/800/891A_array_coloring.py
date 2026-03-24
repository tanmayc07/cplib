import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    o = 0
    for i in range(n):
        if a[i]%2 != 0:
            o += 1
        
    if o%2 == 0:
        print("Yes")
    else:
        print("No")
    
'''
Struggled and overcomplicated with nested if conditions.
Parity of an array or set changes if odd element is added
to it. So number of odd elements will decide we can split the
array or set into two equal parity array or set. Num of odd
elements should be even.
'''
