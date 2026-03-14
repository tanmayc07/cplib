import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1

    row = data[index]
    index += 1
    
    f = 0
    count = 0
    for i in range(len(row)):
        if row[i] == '.':
            count += 1
            
    for i in range(1, len(row)-1):            
        if row[i] == '.' and row[i-1] == '.' and row[i+1] == '.':
            f = 1
    
    print(2) if f==1 else print(count)    
            