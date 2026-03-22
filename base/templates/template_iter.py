import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))

    a = [int(next(data)) for _ in range(n)]
        
    # SOLUTION