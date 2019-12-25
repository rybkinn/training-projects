import requests

i = 0
line2 = []

with open('dataset_3378_2.txt') as inf:
    for line in inf:
        line2.append(line.strip())
        pass

r = requests.get(line2[0])

for numbLine in r.content.splitlines():
    print(numbLine)
    i += 1
print(i)
with open('dataset_3378_2_out.txt', 'w') as file:
    file.write(str(i))
    pass
