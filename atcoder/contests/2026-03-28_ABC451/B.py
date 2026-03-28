import sys

data = iter(sys.stdin.read().split())

n = int(next(data))
m = int(next(data))
a = [[int(next(data)) for _ in range(2)] for _ in range(n)]

d1 = [0]*(m+1)
d2 = [0]*(m+1)

for i in range(n):
    d1[a[i][0]] += 1
    d2[a[i][1]] += 1
    
for i in range(1, m+1):
    print(d2[i]-d1[i])
    