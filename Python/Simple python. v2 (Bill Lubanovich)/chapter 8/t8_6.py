"""Создайте многоуровневый словарь life.
Используйте следующие строки для ключей верхнего уровня:
'animals', 'plants' и 'other'.
Сделайте так, чтобы ключ 'animals' ссылался на другой словарь,
имеющий ключи 'cats', 'octopi' и 'emus'.
Сделайте так, чтобы ключ 'cats' ссылался на список строк со значениями
'Henri', 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари."""

cats = ['Henri', 'Grumpy', 'Lucy']
octopi = {}
emus = {}

animals = {'cats': cats, 'octopi': octopi, 'emus': emus}

plants = {}
other = {}

life = {'animals': animals, 'plants': plants, 'other': other}

print(life)
