t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    print(len(s[:s.find('L')+1]))    