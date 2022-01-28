"""
В какой день недели вы родились?
"""
import datetime

data = datetime.date(1992, 7, 24)
d_w = ("Понедельник",
       "Вторник",
       "Среда",
       "Четверг",
       "Пятница",
       "Суббота",
       "Воскресенье"
       )
w = data.weekday()
for el in range(7):
    if el == w:
        print(d_w[el])
