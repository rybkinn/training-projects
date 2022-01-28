"""Выведите на экран ключи life['animals']."""

cats = ['Henri', 'Grumpy', 'Lucy']
octopi = {}
emus = {}

animals = {'cats': cats, 'octopi': octopi, 'emus': emus}

plants = {}
other = {}

life = {'animals': animals, 'plants': plants, 'other': other}

for key in life['animals'].keys():
    print(key)
