a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= 10 and b <= 10 and c <= 10 and d <= 10 :
    if a <= b :
        if c <= d :
            for x in range(c,d+1):
                print('     ', x, end='')
            print()
            for i in range(a,b+1):
                print(i, end='    ')
                for j in range(c,d+1):
                    print(i*j, end='    ')
                print()
        else:
            print('C должно быть меньше либо равно D')
    else:
        print('A должно быть меньше или равно B')
else:
    print('Введеные цифры долджны быть не больше 10')
