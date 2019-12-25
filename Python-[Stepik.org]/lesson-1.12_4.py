form = input()
if form == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(float(S))
elif form == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(float(S))
elif form == 'круг':
    r = int(input())
    p = float('3.14')
    S = p * (r * r)
    print(float(S))
else:
    print('Вы ввели несуществующую форму')
