t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    print(1+max(n,m))
    
'''Mistake
Didn't consider max(n,m) because the test cases all had n<=m. Must make my
own test cases with all possibilities.
'''
