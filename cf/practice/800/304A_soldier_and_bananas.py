k, n, w = map(int, input().split())

x = k*(w*(w+1))//2
if n >= x: print(0)
else: print(k*(w*(w+1))//2-n)