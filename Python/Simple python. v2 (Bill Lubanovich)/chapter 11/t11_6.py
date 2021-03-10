"""Создайте OrderedDict с именем fancy из пар «ключ — значение»,
приведенных в упражнении 11.5, и выведите его на экран.
Изменился ли порядок ключей?"""
from collections import OrderedDict

fancy = OrderedDict({'a': 1,
                     'b': 2,
                     'c': 3
                     })

print(fancy)
