t = int(input())

for i in range(t):
    n = int(input())
    d = 1
    c = 9
    i = 10
    while i<=n:
        if d*10-i==0:
            d = i
        c += 1
        i += d

    print(c if n>=10 else n)
    
'''
Simply adjust the step in loop after i>=10 to always 
take the numbers with only one non-zero digit.
'''
