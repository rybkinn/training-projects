import requests

urlcurse = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as firstfile:
    f = firstfile.readline().strip()

req = requests.get(f)

while True:

    newfile = str(req.content)[2:-1]

    if newfile[:2] == 'We':
        break

    newurlcurse = urlcurse + newfile
    print(newurlcurse)

    req = requests.get(newurlcurse)

with open('dataset_3378_3_out.txt', 'w') as lastfile:
    lastfile.write(req.text)

print(req.text)
