import sys
from collections import Counter

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1

    a = list(map(int, data[index:index + n]))
    index += n

    freq = Counter(a)
    
    if len(freq) == 1:
        print("Yes")
        continue
        
    if len(freq) == 2:
        counts = list(freq.values())
        
        if abs(counts[0]-counts[1]) <= 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

    '''prev sol
    if len(freq) == 1:
        print("Yes")
        continue
    
    if len(freq) == 2:
        if n%2 == 0 and freq.most_common(1)[0][1] == freq.most_common(2)[1][1]:
            print("Yes")
        elif n%2 != 0 and freq.most_common(1)[0][1]-freq.most_common(2)[1][1] == 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    '''    
    
    