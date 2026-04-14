t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if (x+y)%3==0 and -(x/4)<=y<=x/2:
        print("YES")
    else: print("NO")
    
'''
Vector reachability uses slope to determine the upper
and lower bound and adds the remaining component.
'''