"""
Нарисуйте график на основе тех же данных.
"""
import matplotlib.pyplot as plt

coor = ((0, 0), (3, 5), (6, 2), (9, 8), (14, 10))
x = []
y = []

for coor_tup in coor:
    x.append(coor_tup[0])
    y.append(coor_tup[1])

plt.plot(x, y, 'o-')
plt.show()
