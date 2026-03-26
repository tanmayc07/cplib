import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    n = int(next(data))
    k = int(next(data))
    x = int(next(data))
    
    if x != 1:
        print("YES")
        print(n)
        print('1 '*n)
    else:
        if n%2 == 0 and k>1:
            print("YES")
            print(n//2)
            print(f'{2} '*(n//2))
        elif n%2 != 0 and k>2:
            print("YES")
            print((n-3)//2 + 1)
            print(f'{2} '*((n-3)//2), end="")
            print(3)
        else:
            print("NO")
                    
                    
'''
If we have 1, we can make any possible integer, if not it
depends on the parity of n, if even we can simply use 2s if 
they are available and if odd combine 2s and 3s if 3 are
available else print No.
'''