import sys

input = sys.stdin.read

data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    
    freq = [0] * (n*n+1)
    
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            val = int(data[index])
            index += 1
            
            freq[val] += 1
            row.append(val)
        matrix.append(row)
        
    flag = True
    for i in range(len(freq)):
        if freq[i] > ((n*n)-n):
            flag = False
            break
        
    print("yes") if flag else print("no")


