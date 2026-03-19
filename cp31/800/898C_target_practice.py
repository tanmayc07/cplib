import sys

data = iter(sys.stdin.read().split())

t = int(next(data))

for _ in range(t):
    a = [next(data) for _ in range(10)]

    # BRUTE FORCE    
    tot = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                if ((i==0 or i==9) and j in range(0,10)) or ((j==0 or j==9) and i in range(0,10)):
                    tot += 1
                elif ((i==1 or i==8) and j in range(0,10)) or ((j==1 or j==8) and i in range(0,10)):
                    tot += 2
                elif ((i==2 or i==7) and j in range(0,10)) or ((j==2 or j==7) and i in range(0,10)):
                    tot += 3
                elif ((i==3 or i==6) and j in range(0,10)) or ((j==3 or j==6) and i in range(0,10)):
                    tot += 4
                elif (i==4 or i==5) and (j==4 or j==5):
                    tot += 5
    
    print(tot)
    
    # Math
    tot = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                d = min(i, 9-i, j, 9-j)
                tot += d+1
    
    print(tot)
                