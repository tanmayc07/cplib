import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    x = int(next(data))
    k = int(next(data)) 
    
    if x < k:
        print(1)
        print(x)
    else:
        if x%k == 0:
            print(2)
            print(k+1, x-k-1)
        else:
            print(1)
            print(x)
        
'''
Since the constraint is about divisor of x, if x is divisible
by k, we can simply form a pair using (k+1,x-k-1) giving us
min elements as 2, and if it is not divisible then we can 
directly jump to x. If x itself is smaller than k, then we
can directly jump to x.
'''
