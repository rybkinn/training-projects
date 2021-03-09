"""Напишите функцию, принимающую в виде аргументов два списка и определяющую,
являются ли они противоположными друг другу. Функция должна возвращать True или False.
Каждая пара списков будет состоять из одинаковых элементов (типа a и b).
Список считается анти-списком, если все элементы в нем противоположны соответствующим
элементам в первом списке."""


def anti_list(l1=list, l2=list):
    l_elem = tuple(set(l2))
    for l1_item, l2_item in zip(l1, l2):
        if l1_item != l2_item and l_elem.count(l1_item) == 1:
            continue
        else:
            return False
    return True


result = anti_list(["1", "0", "0", "1"], ["0", "1", "1", "0"])

print(result)