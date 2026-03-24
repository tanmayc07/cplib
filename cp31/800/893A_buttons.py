import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))
    
    if c%2 == 0 and a <= b:
        print("Second")
    elif c%2 != 0 and a >= b:
        print("First")
    elif c%2 != 0 and a < b:
        print("Second")
    else:
        print("First")
        
'''
Depends on c. The idea is that to win the game, either of
them needs to have total buttons greater than the other
person has. if c is odd and a>=b, a wins else b wins, and if
c is even and a>b, a wins else b wins.
'''
