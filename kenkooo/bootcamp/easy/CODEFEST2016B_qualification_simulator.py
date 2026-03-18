import sys

data = iter(sys.stdin.read().split())

n = int(next(data))
a = int(next(data))
b = int(next(data))

s = next(data)

t = a+b
p = 0
bc = 0

for ch in s:
    if ch == 'c':
        print("No")
    elif ch == 'b':
        if p < t and bc < b:
            print("Yes")
            p += 1
            bc += 1
        else:
            print("No")
    else:
        if p < t:
            print("Yes")
            p += 1
        else:
            print("No")
    