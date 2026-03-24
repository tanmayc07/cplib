import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    mn = float('inf')
    cnt = 0
    f = 1
    for i in range(n-1):
        if a[i] > a[i+1]:
            f = 0
            break
        
        cnt = (a[i+1]-a[i])//2 + 1
        mn = min(mn, cnt)
    
    if f: print(mn)
    else: print(0)
    
'''
Kept thinking 2/2=0 lol. To make array unsorted we need to 
find min non-negative diff adjacent pair of elements. We
can derive the answer from the diff.
'''
