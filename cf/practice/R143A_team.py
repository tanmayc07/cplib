n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

c = 0
for e in a:
    if e[0]+e[1]+e[2]>1:
        c+=1

print(c)