import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    k = int(next(data))
    
    if n%2==0 or (n-k)%2==0:
        print("YES")
    else:
        print("NO")
        
'''
(n-k) check decides if we can use the even component with the
odd to make the integer.
'''
