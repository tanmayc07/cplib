import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    m = int(next(data))
    x = next(data)
    s = next(data)
    
    c = 0
    f = 0
    for i in range(7):
        if s in x:
            f = 1
            break
        x = x + x
        c += 1
        
    print(c) if f==1 else print(-1)
        