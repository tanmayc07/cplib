t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mxa = max(a)
    print(mxa*n)