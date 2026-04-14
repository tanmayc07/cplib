t = int(input())

for _ in range(t):
    x = int(input())
    c = 0
    y = x+1
    while y<x+100:
        y1 = y
        s = 0
        while y1!=0:
            d = y1%10
            s += d
            y1 = y1//10
        if y-s == x: c += 1
        y += 1
    print(c)
    
'''
Even though the number 10**9 seems very big, its max sum
of digits can be 81 that is 9*9. Since we know that y
will be greater than x by d(y) amount and d(y) can only
reach 81, we can simply check numbers from x+1 to x+81
and it will only take us 81*9 operations at maximum.
'''
