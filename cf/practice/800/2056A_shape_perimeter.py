t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    res = 0
    for i in range(n-1):
        res += 4*m
        h = m-a[i+1][1]
        w = m-a[i+1][0]
        res -= 2*(h+w)
    res += 4*m
    print(res)