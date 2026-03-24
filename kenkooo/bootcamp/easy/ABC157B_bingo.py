import sys

data = iter(sys.stdin.read().split())

a = [[int(next(data)) for _ in range(3)] for _ in range(3)]
n = int(next(data))
b = [int(next(data)) for _ in range(n)]

ap = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if b[k] == a[i][j]:
                ap[i][j] = 1
        
ans = "No"
for i in range(3):
    if ap[i][0] == 1 and ap[i][1] == 1 and ap[i][2] == 1:
        ans = "Yes"

for i in range(3):
    if ap[0][i] == 1 and ap[1][i] == 1 and ap[2][i] == 1:
        ans = "Yes"
        
if ap[0][0] == 1 and ap[1][1] == 1 and ap[2][2] == 1:
    ans = "Yes"
    
if ap[0][2] == 1 and ap[1][1] == 1 and ap[2][0] == 1:
    ans = "Yes"
    
print(ans)


'''
Just loop over the grid and mark if the given numbers exist
in a seperate array. Then we can use this new array to figure
out. Struggling with kind of grid problems.
'''
