if __name__ == "__main__":
    h, w = map(int, input().split())

    m = []
    for i in range(h):
        r = []
        for j in range(w):
            r.append('.')
        m.append(r)

    for i in range(h):
        if i==0 or i==h-1:
            for j in range(w):
                m[i][j] = '#'

    for j in range(w):
        if j==0 or j==w-1:
            for i in range(h):
                m[i][j] = "#"
            
            
    for i in range(h):
        for j in range(w):
            print(m[i][j], end='')
        print()