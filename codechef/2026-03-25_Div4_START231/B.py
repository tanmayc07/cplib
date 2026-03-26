def check_div(n):
    return ((n%2==0 or n%5==0) and not (n%2==0 and n%5==0))

t = int(input())

for i in range(t):
    n = int(input())
    if check_div(n):
        print(0)
    else:
        if n%2==0 and n%5==0:
            print(2)
        else:
            print(1)
        