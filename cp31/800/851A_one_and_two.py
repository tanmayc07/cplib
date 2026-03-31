t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # PREFIX CALC WITH MATH
    cnt = a.count(2)
    curr, ans = 0, -1
    for i in range(n):
        if a[i]==2: curr += 1
        if cnt - curr == curr:
            ans = i+1
            break
            
    print(ans)

    
    # BRUTE FORCE
    p = [1]*n
    s = [1]*n
    
    p[0] = a[0]
    for i in range(1,n):
        p[i] = a[i]*p[i-1]
    
    for i in range(n-2, -1, -1):
        s[i] = s[i+1]*a[i+1]
        
    ans = -1
    for i in range(n):
        if p[i]==s[i]:
            ans = i+1
            break
            
    print(ans)        
    

'''
Since we cannot store 2^1000 in long long or any type, we need
to do prefix calc because we only have 2s we can count 2s and
use it to get the index.
'''
