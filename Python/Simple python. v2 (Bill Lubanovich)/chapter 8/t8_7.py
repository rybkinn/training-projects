"""Выведите на экран высокоуровневые ключи словаря life."""

cats = ['Henri', 'Grumpy', 'Lucy']
octopi = {}
emus = {}

animals = {'cats': cats, 'octopi': octopi, 'emus': emus}

plants = {}
other = {}

life = {'animals': animals, 'plants': plants, 'other': other}

for key in life.keys():
    print(key)
