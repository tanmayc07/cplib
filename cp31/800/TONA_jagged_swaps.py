import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1

    a = list(map(int, data[index:index + n]))
    index += n
    
    if a[0] == 1:
        print("yes")
    else:
        print("no")
