import sys
import math

data = iter(sys.stdin.read().split())

n = int(next(data))

# Brute Force
for i in range(1, n+1):
    # int() -> nearest integer
    # round() -> nearest neighbour. not good because floating point quirk
    if int(i * 1.08) == n:
        print(i)
        exit()

print(":(")

# Math [n/1.08 <= X < N+1/1.08]
X = math.ceil(n/1.08)

if math.floor(X * 1.08) == n:
    print(X)
else:
    print(":(")