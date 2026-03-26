t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    b = list(map(int, input().split()))
            
    max_b = 0
    for i in range(n):
        for j in range(1, n):
            if i!=j:
                mx = max(c[i], c[j])
                if mx*0.5 < 100: d = mx*0.5
                else: d = mx-100
                sm = min(c[i], c[j]) + d
                if sm <= k:
                    max_b = max(max_b, b[i]+b[j])
                
    print(max_b)