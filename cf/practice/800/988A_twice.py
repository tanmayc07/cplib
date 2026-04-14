t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    hs = set()
    
    sc = 0
    for i in range(n):
        for j in range(i+1, n):
            if i not in hs and j not in hs and i!=j and a[i]==a[j]:
                sc += 1
                hs.add(i)
                hs.add(j)
                
    print(sc)
    
'''
Since we do not want i and j to be chosen again
after they are used once, we can simply use set here.
Also since the constraints are small, we can do it in O(n^2).
'''
