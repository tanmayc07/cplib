t = int(input())

for _ in range(t):
    x = int(input())
    
    c = 0
    while x:
        c += 1
        x //= 10
        
    print(10**c + 1)
    
'''
The core idea is that we select y such that it only has 0 and 1 so it is good by
itself and x.y resolves to x.10^d + x so it simply concatenates x by itself so no
new digits are added.
'''
