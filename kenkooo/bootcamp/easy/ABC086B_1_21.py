
import sys

data = iter(sys.stdin.read().split())

a = next(data)
b = next(data)

c = int(a + b)
f = 0
for i in range(1, c//2):
    if i*i == c:
        f = 1

if f: print("Yes")
else: print("No")