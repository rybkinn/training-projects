"""Создайте defaultdict с именем dict_of_lists и передайте ему аргумент list.
Создайте список dict_of_lists['a'] и присоедините к нему значение
'something for a' за одну операцию. Выведите на экран dict_of_lists['a']."""
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')

print(dict_of_lists['a'])
