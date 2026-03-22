import sys

data = iter(sys.stdin.read().split())

n = int(next(data))

ar = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        ar[i][j] = int(next(data))
    
ans = "No"
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if ar[i][j] + ar[j][k] < ar[i][k]:
                ans = "Yes"
                
print(ans)      

'''Upsolved
Easy simulation to check if the cost is maximum but the matrix
needs to be initialized properly.
'''
