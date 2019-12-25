# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
a = int(input())
s = {}
while a > 0:
    x = int(input())
    if x not in s:
        result = f(x)
        s[x] = result
    print(s[x])
    a -= 1
