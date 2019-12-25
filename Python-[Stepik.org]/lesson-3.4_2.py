allwords = []
beforekeys = []
ENDKEYS = ''
ENDVALUES = 0
x = 0
conNumb = 0
conWord = ''
finNumb = 0
sov = {}
sV = 0
sovVal = 0
sovWor = {}
with open('dataset_3363_3.txt') as inF:
    for line in inF:
        line = line.strip().lower()
        words = line.split()
        allwords.extend(words)
n = len(allwords)
while x != n:
    for i in range(x, n):
        if allwords[x] == allwords[i]:
            conNumb += 1
    if x == 0:
        sov[allwords[x]] = conNumb
    if x > 0 and allwords[x] not in sov:
        sov[allwords[x]] = conNumb
    conNumb = 0
    x += 1
for key, value in sov.items():
    if sV == 0:
        sovVal = value
        sovWor[key] = value
    if value == sovVal:
        sovWor[key] = value
    if value > sovVal:
        sovWor.clear()
        sovVal = value
        sovWor[key] = value
    sV += 1
if len(sovWor) == 1:
    for key, value in sovWor.items():
        ENDKEYS = key
        ENDVALUES = value
else:
    for key in sovWor.keys():
        beforekeys.append(key)
    for i in beforekeys:
        for j in beforekeys:
            if i < j:
                ENDKEYS = j
    ENDVALUES = sovVal
FINISHwFILE = str(ENDKEYS) + ' ' + str(ENDVALUES)
with open('dataset_3363_3_out.txt', 'w') as finishfile:
    finishfile.write(FINISHwFILE)
