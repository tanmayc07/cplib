import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    cnt = 0
    for i in range(n):
        if a[i]-1 != i:
            cnt += 1
    
    print(cnt)