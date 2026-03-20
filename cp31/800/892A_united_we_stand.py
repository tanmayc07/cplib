import sys
from collections import Counter

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
    
    lb, lc = 0, 0
    b = []
    c = []
    m = min(a)
    f = Counter(a)
    for i in range(f[m]):
        b.append(m)
    for i in range(len(a)):
        if not a[i] == m:
            c.append(a[i])
    if len(c) == 0:
        print(-1)
    else:
        print(f"{len(b)} {len(c)}")
        for i in b:
            print(i, end=" ")
        print()
        for i in c:
            print(i, end=" ")
        print()
    
'''
As per the constraints, since we want both of the arrays to be
non-empty and only c array has constraint that it should not
contain divisor of any element in b, we can just fill b with
minimum element from a array and repeat it for all occurrences
since we can't add it to c.
'''
