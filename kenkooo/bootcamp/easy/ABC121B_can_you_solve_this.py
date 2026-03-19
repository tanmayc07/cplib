import sys

data = iter(sys.stdin.read().split())

n = int(next(data))
m = int(next(data))
c = int(next(data))

b = [int(next(data)) for _ in range(m)]
a = [[int(next(data)) for _ in range(m)] for _ in range(n)]

cnt = 0
for i in range(n):
    tot = 0
    for j in range(m):
        tot += a[i][j] * b[j]
    tot += c
    if tot > 0:
        cnt += 1
        
print(cnt)
