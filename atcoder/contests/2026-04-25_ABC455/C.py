from collections import Counter
from operator import itemgetter

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)
sm = {}
for ke, v in c.items():
    sm[ke] = ke*v

sn = sorted(sm.items(), key=itemgetter(1), reverse=True)
sn = sn[k:]
if not sn: print(0)
else:
    s = 0
    for t in sn:
        s += t[1]
    print(s)