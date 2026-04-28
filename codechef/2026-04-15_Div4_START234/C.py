t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    ts = sum(a)
    if ts >= 0: print(n)
    else:
        mx = 0
        ps = 0
        for i in range(n):
            if ts-ps >= 0:
                mx = n-i
                break
            ps += a[i]
        print(mx)        
            
'''Upsolved
The intuition stems from the constraint that we only care about
the longest subsequence i.e its length and so we can simply
sort the array and take elements until the sum>=0.
'''
