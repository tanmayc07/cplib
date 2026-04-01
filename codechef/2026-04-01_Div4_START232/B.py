t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mx = max(a)
    mn = min(a)
    cnt = 0
    
    for num in a: 
        if num != mx and num != mn: cnt += 1
        
    print(cnt)