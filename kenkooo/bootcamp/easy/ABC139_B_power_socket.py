import sys
from collections import Counter

data = iter(sys.stdin.read().split())

a = int(next(data))
b = int(next(data))

c = 0
out = 1
    
while out < b:
    out -= 1
    out += a
    c += 1

print(c)