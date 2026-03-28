import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    for i in range(0, n):
        print(n-a[i]+1, end=" ")
    print()
    
'''
The constraint that we need a1+b1<=a2+b2... implies that 
we can just make every sum equal to each other.
'''