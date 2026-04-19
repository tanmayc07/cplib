t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    
    if 67 in a: print("YES")
    else: print("NO")
    
'''
Since 67 is a prime number, we only need to check if 
67 is present in the array or not.
'''
