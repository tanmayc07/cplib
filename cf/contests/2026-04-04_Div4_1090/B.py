'''
4
41 41 41 41 41 41 41
6 9 4 20 6 7 67
1 2 3 4 5 6 7
6 7 6 7 6 7 6
'''

t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    n = len(a)
    
    a.sort()
    s = 0
    for i in range(n-1): s+=(-1)*a[i]
    s += a[n-1]
    
    print(s)
