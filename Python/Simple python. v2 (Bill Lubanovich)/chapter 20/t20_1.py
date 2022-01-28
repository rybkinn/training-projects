"""
Установите matplotlib. Нарисуйте диаграмму рассеивания
для следующих пар (x, y): ( (0, 0), (3,5), (6, 2), (9, 8), (14, 10) ).
"""
import matplotlib.pyplot as plt

coor = ((0, 0), (3, 5), (6, 2), (9, 8), (14, 10))
x = []
y = []

for coor_tup in coor:
    x.append(coor_tup[0])
    y.append(coor_tup[1])

plt.scatter(x, y)
plt.show()
