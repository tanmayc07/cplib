from heapq import heappush, heappop

q = int(input())

hp = []

for i in range(q):
    t, h = map(int, input().split())
    
    if t==1: heappush(hp, h)
    else:
        while hp and hp[0]<=h:
            heappop(hp)
    
    print(len(hp))
    
'''Upsolved
This problem is an exercise for Priority Queue/Heap. Since,
we need to remove all elements<=h and the constraint is 
in the order or 10^5, we can't use set or hashmap as removing
will take O(n) inside the outer loop. Heap brings it down to
O(QlogQ).
'''
