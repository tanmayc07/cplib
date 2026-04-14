t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    
    cnt = a + b//3
    b %= 3
    
    if b>0 and 3-b > c:
        print(-1)
        continue
    
    if b>0:
        cnt += 1
        c -= 3-b
        
    cnt += (c+2)//3
    print(cnt)
    
'''
We first start with all introverts and then
calculate the number of tents for extroverts,
if we have remaining extro, we take them from
universal and then calc tent for remaining universals.
'''
