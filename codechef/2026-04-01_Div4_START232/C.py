from collections import defaultdict
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mp = defaultdict(int)
    ans = 0
    
    for i in range(n):
        ans += mp[a[i]-i]
        mp[a[i]-i] += 1
        
    print(ans)
    
'''Upsolved
The constraints allow for only O(N) or O(NlogN) solutions or
lower. The given equation can be rearranged to bring i terms
together and j terms together. We can run a loop and count
i index values of the equation and add if we get same value
for j index.
'''
