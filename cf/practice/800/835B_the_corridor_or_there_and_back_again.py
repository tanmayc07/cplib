t = int(input())

for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    a.sort()
    mn = float('inf')
    for i in range(n):
        x = a[i][0] + ((a[i][1]-1)//2)
        mn = min(mn, x)
        
    print(mn)