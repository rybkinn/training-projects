n = int(input())
s = []
long = 0
w = 1
while True:
    for i in range(w):
        s.append(w) #нужно записать столько раз, сколько итераций прошел цикл
    long = len(s)
    w += 1
    if long >= n:
        if long > n:
            s = s[:n] #отсечение всех числе что после n
            break
        else: #если равна
            break
for i in s:
    print(i, end = " ")
