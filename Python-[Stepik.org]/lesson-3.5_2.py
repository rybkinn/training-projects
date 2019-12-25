import sys

i = 1
for arg in sys.argv:
    if i == 1:
        i += 1
        continue
    elif i == len(sys.argv):
        print(arg)
        i = 1
    else:
        print(arg, end=' ')
    i += 1
