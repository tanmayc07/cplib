h, w = map(int, input().split())
mat = []
for i in range(h):
    mat.append(input())

ans = 0
for h1 in range(h):
    for h2 in range(h1, h):
        for w1 in range(w):
            for w2 in range(w1, w):
                ok = True
                for i in range(h1, h2+1):
                    for j in range(w1, w2+1):
                        if mat[i][j] != mat[h1+h2-i][w1+w2-j]:
                            ok = False
                            break
                if ok: ans += 1

print(ans)