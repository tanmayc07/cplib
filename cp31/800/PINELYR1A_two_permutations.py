t = int(input())

for i in range(t):
    n,a,b = map(int, input().split())
    
    if a+b+2 <= n or a==b==n:
        print("YES")
    else:
        print("NO")
        
        
'''
Since we need to create two permutations with same prefix
and suffix, we need atleast two elements after fixing
the prefix and suffix elements. The edge case that I missed
was that if a==b==n, then by default prefix==suffix.
'''
