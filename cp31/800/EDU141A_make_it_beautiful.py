from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    curr = 0
    idx = -1
    for i in range(n):
        if curr == a[i]:
            idx = i
            break        
        curr += a[i]
        
        
    if idx != -1:    
        if n<=2: print("NO")
        elif len(Counter(a))==1: print("NO")
        else:
            print("YES")
            a[idx], a[(idx+1)%n] = a[(idx+1)%n], a[idx]
            for num in a: print(num, end=" ")
            print()
    else:
        print("YES")
        for num in a: print(num, end=" ")
        print()