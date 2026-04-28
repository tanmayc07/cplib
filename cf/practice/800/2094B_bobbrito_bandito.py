t = int(input())

for _ in range(t):
    n, m, l, r = map(int, input().split())
    
    d = n-m
    v = min(d, r)
    r -= v
    d -= v
    l += d
    print(f"{l} {r}")
    
'''
Since we need [l', r'] inside of [l, r] and we also
need to include 0 in it, we think of chopping from both ends.
We need to chop n-m positions since the length of [l',r']
is m. We first chop the segment r-r' and then l-l'.
'''
