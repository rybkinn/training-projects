lst = [int(i) for i in input().split()]
x = int(input())
j = []
e = 0
for i in lst:
    if x == i:
        j.append(e)
    e += 1
if len(j) != 0:
    for i in j:
        print(i, end=' ')
else:
    print('Отсутствует')
