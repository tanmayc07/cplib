from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    c = Counter(b)
    mx = max(b)
    x = 1
    ans = "Yes"
    for k,v in c.items():
        if v > 1:
            x -= 1
            if x < 0 or mx != k:
                ans = "No"
                break
                
    print(ans)