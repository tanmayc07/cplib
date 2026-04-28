t = int(input())

for i in range(t):
    n = int(input())
    a = [0]*3*n 
    c = 1
    for i in range(0,3*n,3): 
        a[i] = c
        c += 1
    for i in range(1,3*n): 
        if not a[i]:
            a[i] = c
            c += 1
    
    for i in range(3*n):
        print(a[i], end=" ")
    print()