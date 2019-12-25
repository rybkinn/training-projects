a = [int(i) for i in input().split()]
longA = len(a)
i = 0
summ = 0
while i <= longA - 1:
        summ = summ + a[i]
        i += 1
print(summ)
