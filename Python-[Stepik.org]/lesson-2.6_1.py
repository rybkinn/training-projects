numb = []
i = 0
while i == 0:
    a = int(input())
    numb.append(a)
    p = sum(numb)
    if p == 0:
        numb = [x * x for x in numb]
        finish = sum(numb)
        break
print(finish)
