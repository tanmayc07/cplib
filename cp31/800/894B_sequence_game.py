import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    a = [int(next(data)) for _ in range(n)]
    r = [a[0]]
    
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            r.append(a[i])
        r.append(a[i])
        
    print(len(r))
    for nm in r:
        print(nm, end=" ")
    print()
    
'''
Since the first element will always be fixed, 
we can keep checking if the next element is smaller than or equal
to previous element and if it isn't we can just repeat the current
element in our result array.
'''
