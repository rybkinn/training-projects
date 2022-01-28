"""Используйте функцию zip(), чтобы создать словарь с именем movies,
в котором объединены списки
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
и
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']."""

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

movies = dict(zip(titles, plots))

print(movies)
