t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    
    d = N
    mn = 0
    while d>M:
        mn += d
        d -= 1
    print(mn)
    