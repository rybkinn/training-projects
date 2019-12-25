coordinate = [0, 0]

n = int(input())
commands = [input().split() for i in range(0, n)]

p = 0

for i in commands:
    for j in i:
        if j == 'восток':
            coordinate[0] += int(commands[p][1])
        elif j == 'север':
            coordinate[1] += int(commands[p][1])
        elif j == 'запад':
            coordinate[0] -= int(commands[p][1])
        elif j == 'юг':
            coordinate[1] -= int(commands[p][1])
    p += 1

for i in coordinate:
    print(i, end=' ')
print()
