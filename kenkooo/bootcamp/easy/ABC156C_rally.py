import sys
from collections import Counter

data = iter(sys.stdin.read().split())

n = int(next(data))
a = [int(next(data)) for _ in range(n)]
m = float("inf")

for i in range(1, 101):
    t = 0
    for j in range(len(a)):
        t += (a[j]-i)**2
    m = min(m, t)
    
print(m)