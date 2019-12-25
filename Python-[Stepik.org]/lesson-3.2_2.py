enter = [i for i in input().lower().split()]
repeatNumber = {}
f = 0
for i in enter:
    for x in range(len(enter)):
        if i == enter[x]:
            f += 1
    repeatNumber[i] = f
    f = 0
for key, value in repeatNumber.items():
    print(key, value, end='\n')
