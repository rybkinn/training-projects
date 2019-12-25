middleForStudents = []
middleForSubject = []
outSub = ''
i = 0  # переменная для посчета среднего балло по предметом для студента
m = 0  # накопление баллов для математики
f = 0  # накопление баллов для физики
r = 0  # накопление баллов для русского яз.
NumbStu = 0  # подсчет кол-ва студентов
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        i = (int(line[1]) + int(line[2]) + int(line[3])) / 3
        middleForStudents.append(i)
        m += int(line[1])
        f += int(line[2])
        r += int(line[3])
        NumbStu += 1
middleM = m / NumbStu
middleF = f / NumbStu
middleR = r / NumbStu
outSub = str(middleM) + ' ' + str(middleF) + ' ' + str(middleR)
with open('dataset_3363_4_out.txt', 'w') as outfile:
    for j in middleForStudents:
        outfile.write(str(j)) + outfile.write('\n')
    outfile.write(outSub)
