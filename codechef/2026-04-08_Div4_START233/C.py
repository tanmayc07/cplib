t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    m = n-k
    medians = set()
    
    for i in range(n):
        S, L = 0, 0
        for j in range(n):
            if a[j]<a[i]: S+=1
            if a[j]>a[i]: L+=1
        
        if m%2 == 0:
            if max(0, S-(m//2-1)) + max(0, L-m//2) <= k:
                medians.add(a[i])
        else:
            if max(0, S-m//2) + max(0, L-m//2) <= k:
                medians.add(a[i])
        
    print(*sorted(list(medians)))