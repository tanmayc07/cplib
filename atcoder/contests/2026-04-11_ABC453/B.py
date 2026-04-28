t, X = map(int, input().split())
a = list(map(int, input().split()))

ls = a[0]
print(f"0 {a[0]}")
for i in range(1, t+1):
    if abs(a[i]-ls)>=X:
        ls = a[i]
        print(f"{i} {a[i]}")