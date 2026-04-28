from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))

hs = set(a)
hc = Counter(a)

if len(hs)==n: print("Yes")
else: print("No")

if len(hc) == m: print("Yes")
else: print("No")