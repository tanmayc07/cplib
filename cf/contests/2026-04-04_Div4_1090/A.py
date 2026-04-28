t = int(input())

for i in range(t):
    n = int(input())
    mx = -68
    mn = 68
    for i in range(-67, n+1):
        mn = min(i, n)
        mx = max(mx, mn)
    
    print(mx+1) 