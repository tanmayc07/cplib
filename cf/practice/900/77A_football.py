S = input()
z = 0
o = 0
f = 0

i = 0
while i < len(S)-1:
    if S[i]=='0':
        z = 1
        while i<len(S)-1 and S[i+1]=='0': 
            i += 1
            z += 1
        if z>=7: 
            f = 1
            break
    else:
        o = 1
        while i<len(S)-1 and S[i+1]=='1': 
            i += 1
            o += 1
        if o>=7:
            f = 1
            break
    i += 1
        
if f: print("YES")
else: print("NO")
        
        