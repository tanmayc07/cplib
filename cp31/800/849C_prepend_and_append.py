t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    
    a = n
    for i in range(n//2):
        if (s[i]=='1' and s[n-i-1]=='0') or (s[i]=='0' and s[n-i-1]=='1'):
            a -= 2
        else:
            break
    
    print(a)        
    
'''
Simple loop to check each end and update the min length.
'''    