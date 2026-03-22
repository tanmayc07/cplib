import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    c = int(next(data))
    k = int(next(data))
    a = [int(next(data)) for _ in range(n)]
    
    a = sorted(a)
    for i in range(n):
        while a[i] < c and k > 0:
            a[i] += 1
            k -= 1
        
        if a[i] <= c:
            c += a[i]
            
    print(c)