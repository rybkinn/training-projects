# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    k2 = key * 2
    if key in d:
        d[key].append(value)
    elif k2 in d:
        d[k2].append(value)
    else:
        d[k2] = [value]
# не добавляйте кода вне функции
