t = int(input())

for _ in range(t):
    s = input()
    c = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]: c += 1
    if c>2: print("No")
    else: print("Yes")
    
'''Upsolved
Since we are allowed to do the operation only once, we need
to do case work to check how we can fix the string if
it has one pair of equal adjacent elements, two pair of
equal adjacent elements and >2 pairs. The critical observation
is that we can only fix the string if it has atmost 2 pair
of equal adjacent elements.
'''