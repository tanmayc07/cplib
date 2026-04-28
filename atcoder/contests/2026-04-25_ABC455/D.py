n, q = map(int, input().split())

down = [-1]*2*n
up = [-1]*2*n

for i in range(n):
    down[i] = n+i
    up[n+i] = i

for i in range(q):
    c, p = map(int, input().split())
    c-=1
    p-=1
    
    d = down[c]
    down[c] = p
    up[p] = c
    up[d] = -1
    
res = []
for i in range(n):
    x = n+i
    
    cnt = 0
    while up[x] != -1:
        cnt += 1
        x = up[x]
    res.append(cnt)
    
print(*res)

'''Upsolved
This problem is based on the idea of cutting a segment
and attaching to other since we cannot simulate actual
moving of the elements (in this case cards) from one pile
to other for all queries. Core concept is to think in 
terms of linked structure so that we can simply manipulate
few links to compute the state.
'''
