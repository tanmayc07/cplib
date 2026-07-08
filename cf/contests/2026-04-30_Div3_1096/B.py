t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    
    if n%2: print("NO")
    else:
        oc = s.count('(')
        cc = s.count(')')
        if oc != cc:
            print("NO")
        else:
            print("YES")