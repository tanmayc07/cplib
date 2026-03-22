import sys

data = iter(sys.stdin.read().split())

n = int(next(data))

for i in range(n, 1, -1):
    print(i, end=",")
print(1)