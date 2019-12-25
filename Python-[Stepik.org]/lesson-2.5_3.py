a = [int(i) for i in input().split()]
a.sort()
b = len(a)
newA = []
c = 0
for i in a:
    if c < b-1:
        if (a[c] == a[c+1]) and (a[c] not in newA): #если элементы одинаковы и если нет такого элемента в новом списке
            newA.append(a[c])
    c = c + 1
for i in newA:
    print(i, end=' ')
