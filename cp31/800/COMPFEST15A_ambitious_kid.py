import sys

data = iter(sys.stdin.read().split())

n = int(next(data))

a = []
m = float('inf')

for i in range(n):
    e = int(next(data))
    m = min(m, abs(e))
    a.append(e)
    
print(m)