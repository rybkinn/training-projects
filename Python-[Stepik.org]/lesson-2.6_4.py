a = []
b = []
f = 0
while True:
    a.append([i for i in input().split()])
    f += 1
    if a[-1][0] == 'end':
        a = a[:f-1]
        break
    b.append([int(i) for i in a[f-1]])
c = [[0 for i in range(len(b[0]))] for i in range(len(b))]
for i in range(len(b)):
    for j in range(len(b[0])):
        if (i == len(b)-1) and (j != (len(b[0])-1)):
            c[i][j] = b[i-1][j] + b[0][j] + b[i][j-1] + b[i][j+1]
            continue
        if j == (len(b[0])-1) and i != len(b)-1:
            c[i][j] = b[i-1][j] + b[i+1][j] + b[i][j-1] + b[i][0]
            continue
        if j == (len(b[0])-1) and i == len(b)-1:
            c[i][j] = b[i-1][j] + b[0][j] + b[i][j-1] + b[i][0]
            break
        c[i][j] = b[i-1][j] + b[i+1][j] + b[i][j-1] + b[i][j+1]
for i in c:
    for j in i:
        print(j, end=' ')
    print()
