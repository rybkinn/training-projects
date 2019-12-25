a = float(input())
b = float(input())
c = input()
if c == '*':
    d = a * b
    print(d)
elif c == '-':
    d = a - b
    print(d)
elif c == '+':
    d = a + b
    print(d)
elif c == 'pow':
    d = a ** b
    print(d)
elif b == float('0'):
    print('Деление на 0!')
elif c == 'mod':
    d = a % b
    print(d)
elif c == 'div':
    d = a // b
    print(d)
elif c == '/':
    d = a / b
    print(d)
else:
    print('введена не существующая операция')
