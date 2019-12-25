a = [int(i) for i in input().split()]
if len(a)==1:
    print(a[0])
else:
    b = []
    c = 0
    for i in a:
        if c==0:
            b.append(a[-1] + a[1])
        elif c==len(a)-1:
            b.append(a[-2] + a[0])
        else:
            b.append(a[c-1] + a[c+1])
        c = c + 1
    for i in b:
        print(i, end=' ')
