"""Выведите значения life['animals']['cats']."""

cats = ['Henri', 'Grumpy', 'Lucy']
octopi = {}
emus = {}

animals = {'cats': cats, 'octopi': octopi, 'emus': emus}

plants = {}
other = {}

life = {'animals': animals, 'plants': plants, 'other': other}

for values in life['animals']['cats']:
    print(values)
