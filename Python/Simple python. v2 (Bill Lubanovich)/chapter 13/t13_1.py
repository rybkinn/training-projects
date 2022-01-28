"""
Запишите текущие дату и время как строку в текстовый файл today.txt.
"""
import datetime

with open('today.txt', 'w') as f:
    f.write(str(datetime.datetime.now()))
    f.close()