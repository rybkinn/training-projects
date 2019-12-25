file = list()
klassi = {i: 0 for i in range(1, 12)}
i = 0

with open('dataset_3380_5.txt') as inf:
    for line in inf:
        file.append(line.split())

for _numclass in range(1, 12):
    for _elementfile in file:
        if _numclass == int(_elementfile[0]):
            klassi[_numclass] += int(_elementfile[2])
            i += 1
        else:
            continue
    if klassi[_numclass] != 0:
        klassi[_numclass] = float(klassi[_numclass] / i)
    else:
        klassi[_numclass] = '-'
    i = 0

for key, value in klassi.items():
    print(key, value, end='\n')
