import sys

data = iter(sys.stdin.read().split())

t = int(next(data))
n = int(next(data))

a = [int(next(data)) for _ in range(n)]
a = [[int(next(data)) for _ in range(n)] for _ in range(n)]