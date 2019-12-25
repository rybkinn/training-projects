a = int(input())
b = int(input())
c = int(input())
#вычисляем макс число
if a >= b and a >= c:
    mx = a
elif b >= a and b >= c:
    mx = b
elif c >= a and c >= b:
    mx = c
#вычисляем мин число
if a <= b and a <= c:
    mn = a
elif b <= a and b <= c:
    mn = b
elif c <= a and c <= b:
    mn = c
#вычисляем оставшееся число
if mx == a and mn == b:
    avg = c
elif mx == a and mn == c:
    avg = b
elif mx == b and mn == a:
    avg = c
elif mx == b and mn == c:
    avg = a
elif mx == c and mn == a:
    avg = b
elif mx == c and mn == b:
    avg = a
#вычисляем оставшееся число если 2 числа равны
if a == b and a == c:
    avg = a
elif a == b and a != c:
    avg = a
elif a != b and a == c:
    avg = a
print(mx)
print(mn)
print(avg)
