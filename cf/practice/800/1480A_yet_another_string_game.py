t = int(input())

for _ in range(t):
    s = list(input())
    for i in range(0, len(s), 2):
        if s[i]=='a': s[i] = 'b'
        else: s[i] = 'a'
    
    for i in range(1, len(s), 2):
        if s[i]=='z': s[i] = 'y'
        else: s[i] = 'z'
        
    print(''.join(s))
        