n = int(input())
if n == 1:
    print(n)
else:
    n2 = n*n
    a = [[0 for j in range(n)] for i in range(n)]
    if n%2 != 0:  
        p1 = int(((n+1)/2)-1)
    else:
        p1 = int(((n+1)/2)-1)+1
    k = 0
    f = 0
    while n-1 > 0:
        if f == 0:
            n -= 1
        for i in range(n):
            k += 1
            a[0+f][i+f] = k
        for j in range(n):
            k += 1
            a[j+f][n+f] = k
        for i in range(n,0,-1):
            k += 1
            a[n+f][i+f] = k
        for j in range(n,0,-1):
            k += 1
            a[j+f][0+f] = k
        n -= 2
        f += 1
    if n2 > 4:
        if n2%2 != 0:
            a[p1][p1] = n2
        else:
            a[p1-1][p1-1] = k+1
            a[p1-1][p1] = k+2
            a[p1][p1] = k+3
            a[p1][p1-1] = k+4
    for v in a:
        for w in v:
            print(w, end=' ')
        print()
