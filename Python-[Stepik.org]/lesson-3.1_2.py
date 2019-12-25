def modify_list(l):
    c = 1
    z = 0
    for i in range(1,len(l)+1):
        if l[-c]%2 != 0:
            l.remove(l[-c])
        else:
            c += 1
    for i in l:
        x = int(i/2)
        l[z] = x
        z += 1
