import sys

data = iter(sys.stdin.read().split())

n = int(next(data))
k = int(next(data))
a = [int(next(data)) for _ in range(n)]
ka = []
for i in range(k):
    row = []
    row.append(int(next(data)))
    row.append(int(next(data)))
    ka.append(row)

ps = [0] * (len(a)+1)
for i in range(k):
    start = ka[i][0]
    stop = ka[i][1]
    
    ps[start-1] += 1
    ps[stop] -= 1
    
c = 0
for i in range(n):
    c += ps[i]
    a[i] += c
    
for num in a:
    print(num, end=" ")
print()    

'''Upsolved
Was able to come up with the logic but did it brute force
and got TLE. It uses prefix sum range update technique 
aka difference array.
'''
