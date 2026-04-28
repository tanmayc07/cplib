from collections import defaultdict, deque
n, m = map(int, input().split())    
a = [list(map(int, input().split())) for i in range(m)] 

hm = defaultdict(list)
for i in a:
    hm[i[0]].append(i[1])
    
a.sort()
hs = set()
seen = set()
q = deque([1])
while q:
    c = q.popleft()
    if c not in seen:
        for j in hm[c]:
            q.append(j)
            hs.add(j)
        seen.add(c)
        
print(len(seen))