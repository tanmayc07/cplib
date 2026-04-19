t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n==1: print(1)
    else:
        for i in range(n):
            print(2, end=" ")
        print()