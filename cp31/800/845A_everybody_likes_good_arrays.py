import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
        
    curr = a[0]
    cnt = 0
    for i in range(n-1):
        if curr%2 == a[i+1]%2:
            curr = a[i]*a[i+1]
            cnt += 1
        else:
            curr = a[i+1]
            
    print(cnt)
    
'''
We are not asked to actually return the final array by mutating
it, so we can simply linearly traverse the array and keep 
a count if we need to do the operation.
'''
