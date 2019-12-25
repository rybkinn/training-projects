with open('dataset_3363_2.txt') as filelinuxtxt:
    inputfile = filelinuxtxt.readline().strip()
outputfile = ''
skipID = True
x = 0
for i in inputfile:
    if skipID:
        if '0' <= i <= '9' and x != len(inputfile) - 1:
            nextInd = inputfile[x + 1]
            if '0' <= nextInd <= '9':
                dublnumber = inputfile[x] + inputfile[x + 1]
                p = inputfile[x - 1] * int(dublnumber)
                outputfile = outputfile + p
                skipID = False
                x += 1
                continue
            else:
                p = inputfile[x - 1] * int(i)
                outputfile = outputfile + p
    if x == len(inputfile) - 1:
        if '0' <= inputfile[-2] <= '9':
            dublnumber = inputfile[-1] + inputfile[-2]
            p = inputfile[-3] * int(dublnumber)
            outputfile = outputfile + p
        else:
            p = inputfile[-2] * int(inputfile[-1])
            outputfile = outputfile + p
    skipID = True
    x += 1
with open('dataset_3363_2_out.txt', 'w') as finishfile:
    finishfile.write(outputfile)
