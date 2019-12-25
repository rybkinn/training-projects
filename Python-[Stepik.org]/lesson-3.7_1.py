GameFinish = int(input())
Teams = {}

for i in range(0, GameFinish):
    _igra = input()
    resultigr = _igra.split(';')

    if resultigr[0] not in Teams:
        Teams[resultigr[0]] = [0, 0, 0, 0, 0]
    if resultigr[2] not in Teams:
        Teams[resultigr[2]] = [0, 0, 0, 0, 0]
    Teams[resultigr[0]][0] += 1
    Teams[resultigr[2]][0] += 1
    if resultigr[1] > resultigr[3]:
        Teams[resultigr[0]][1] += 1
        Teams[resultigr[2]][3] += 1
        Teams[resultigr[0]][4] += 3
    elif resultigr[1] < resultigr[3]:
        Teams[resultigr[0]][3] += 1
        Teams[resultigr[2]][1] += 1
        Teams[resultigr[2]][4] += 3
    else:
        Teams[resultigr[0]][2] += 1
        Teams[resultigr[2]][2] += 1
        Teams[resultigr[0]][4] += 1
        Teams[resultigr[2]][4] += 1

for key, value in Teams.items():
    print(key + ':', end='')
    for i in value:
        print(i, end=' ')
    print()
