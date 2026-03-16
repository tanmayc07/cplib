import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1

    if n%3 == 0:
        print("Second")
    else:
        print("First")
