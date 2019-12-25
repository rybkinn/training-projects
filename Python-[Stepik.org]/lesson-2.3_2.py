a = int(input())
b = int(input())
t = int(0)
d = int(0)
for x in range(a,b+1):
    if x % 3 == 0 :
        t += 1
        d = d + x
e = float(d / t)
print(e)
