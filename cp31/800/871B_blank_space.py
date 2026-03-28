import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    cnt, i = 0, 0
    l = 0
    while i < n:
        while i<n and a[i] == 0:
            cnt += 1
            i += 1
        l = max(l, cnt)
        cnt = 0
        i += 1
        
    print(l)   
    
'''
Simple simulation.
'''