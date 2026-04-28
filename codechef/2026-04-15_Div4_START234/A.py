N, K = map(int, input().split())

cost = N*100
if (N*60)+K <= cost: print((N*60)+K)
else: print(cost)