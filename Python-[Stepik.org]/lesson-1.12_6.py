n = int(input())
x = int(n % 10)
y = int(n % 100)
if n >= 0:
    if n == 0 or (5 <= n <= 9):
        print(str(n) + ' программистов')
    elif n == 1:
        print(str(n) + ' программист')
    elif 2 <= n <= 4:
        print(str(n) + ' программиста')
    elif (11 <= n <= 14) or (11 <= y <= 14):
        print(str(n) + ' программистов')
    elif x == 0 or (5 <= x <= 9):
        print(str(n) + ' программистов')
    elif x == 1:
        print(str(n) + ' программист')
    elif 2 <= x <= 4:
        print(str(n) + ' программиста')
else: 
    print('Введите не отрицательное число')
