wcount = int(input())
wordlist = [input().lower() for i in range(0,wcount)]
textcount = int(input())
text = [input().lower().split() for j in range(0,textcount)]
exitword = set()

for i in text:
    for j in i:
        if j.lower() not in wordlist:
            exitword.add(j)

for notinword in exitword:
    print(notinword)
