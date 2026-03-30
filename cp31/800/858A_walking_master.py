t = int(input())

for i in range(t):
    a,b,c,d = map(int, input().split())
    
    if d<b:
        print(-1)
        continue
    else:
        op = d-b
        a += op
        if c > a:
            print(-1)
            continue
        else:
            op += a-c
            print(op)
            
'''
Since y always increases, we can rule out if dest y>source y else
we can first reach y and then check if the dest x is to the left
or not, if yes we can add the remaining number of operations.
'''
