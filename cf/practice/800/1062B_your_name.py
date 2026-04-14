from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s, t = input().split()
    
    s = Counter(s)
    t = Counter(t)
    
    if s==t: print("Yes")
    else: print("No")