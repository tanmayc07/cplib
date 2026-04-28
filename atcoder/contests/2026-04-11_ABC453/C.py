N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    cnt, curr, prev = 0, 0.5, 0
    for j in range(N):
        prev = curr
        if ((1<<j)&i): curr += L[j]
        else: curr -= L[j]
        
        if (prev>0 and curr<0) or (prev<0 and curr>0): cnt += 1
    
    ans = max(ans, cnt)
    
print(ans)
    
        
'''
Bitmasking and power set generation to simulate all the
possible counts for every moves because N<=20 so 2^20==10^6
which is acceptable since allowed ops=10^8.
'''
