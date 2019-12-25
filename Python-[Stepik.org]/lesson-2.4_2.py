s = input()
news = ''
long = len(s)
if long != 1:
    i = 0
    x = 1
    while i < long - 1:
        if s[i] == s[i+1]:
            x += 1
        else:
            news = news + s[i] + str(x)
            x = 1
        if i == long - 2:
            news = news + s[i+1] + str(x)
        i += 1
else:
    news = s + str(1)
print(news)
