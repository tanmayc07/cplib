t = int(input())

for _ in range(t):
    n,m,a,b,c = map(int, input().split())
    cm = min(n, m)
    re = max(n,m)-cm
    if n>m: print(cm*c+re*a)
    else: print(cm*c+re*b)
