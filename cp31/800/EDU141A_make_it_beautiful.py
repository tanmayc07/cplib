from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a = sorted(a)
    if a[0]==a[n-1]: print("NO")
    else:
        print("YES")
        print(a[n-1], end=" ")
        for i in range(n-1): print(a[i], end=" ")
        print()
        
'''
If there are no distict numbers in the array, we can't make it
beautiful. We can check for distinct numbers by simply checking
min and max because we simply need the min and max to be diff
to make it beautiful.
'''
