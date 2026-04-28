t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    oc = s.count('1')
    p1 = s.count('101')
    p2 = s.count('111')
    print(f"{oc-p2} {oc+p1}")