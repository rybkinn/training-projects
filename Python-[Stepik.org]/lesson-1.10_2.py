n = int(input())
a = bool(n % 4 == 0)
b = bool(n % 100 != 0)
c = bool(n % 400 == 0)
if 1900 <= n <= 3000:
    if a and b or c:
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Некорректная дата')
