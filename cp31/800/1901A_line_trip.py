import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    index += 2

    a = list(map(int, data[index:index + n]))
    index += n

    m = a[0]-0
    for i in range(1, len(a)):
        m = max(m, a[i]-a[i-1])
    m = max(m, 2*(x-a[-1]))
    
    print(m)