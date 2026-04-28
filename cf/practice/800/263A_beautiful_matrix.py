mat = []
for i in range(5):
    mat.append(list(map(int, input().split())))

idx = (0, 0)
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1: idx = (i, j)
        
tc = abs(idx[0]-2) + abs(idx[1]-2)
print(tc)
        