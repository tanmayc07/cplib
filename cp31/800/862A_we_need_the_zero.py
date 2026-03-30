t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    tot_xor = 0
    for num in a:
        tot_xor ^= num
    
    if n%2 == 1:
        print(tot_xor)
    else:
        if tot_xor==0: print(tot_xor)
        else: print(-1)
        
'''
Use XOR properties and try to group x to find the relation
between n and number of x.
'''
