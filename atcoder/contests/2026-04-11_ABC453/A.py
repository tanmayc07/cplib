N = int(input())
S = input()

ni = N
for i in range(N):
    if S[i]!='o':
        ni = i
        break

if ni<N:
    print(S[ni:])
else: print('')