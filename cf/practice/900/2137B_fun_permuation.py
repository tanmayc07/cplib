t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    
    for i in a:
        print(n+1-i, end=" ")
    print()
    
'''
For adjacent elements to exist, n>=2. Since gcd of two equal numbers
equal the same number, we need to make pi+qi = n+1 because if n>=2,
n+1>=3 so if we make pi+qi=n+1, we guarantee that the gcd>=3.
'''
