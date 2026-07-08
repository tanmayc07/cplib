t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    l1 = [x for x in a if not x%6]
    l2 = [x for x in a if not x%2 and x%3]
    l3 = [x for x in a if not x%3 and x%2]
    l4 = [x for x in a if x%2 and x%3]
    
    ans = []
    ans.extend(l1) 
    ans.extend(l2)
    ans.extend(l4)
    ans.extend(l3)
    print(*ans)
    
'''Upsolved
We start by forming groups of elements based on factors
of 6 - 2,3,6. So s6 - group of elements divisible by 6, since
this group already has 2 and 3 we must place these elements
at the edge of the array so that the subarrays will be
minimized. s2 - divisible by 2, s3 - divisible by 3, we should
place this one after another. s1 - not divisible by 2 and 3, this
group when placed between s2 and s3 will act like a buffer
and will not allow more subarrays to form.
'''
