"""
Проанализируйте дату из строки today_string.
"""
import datetime

with open('today.txt', 'r') as today_txt:
    today_string = today_txt.readline()
    today_txt.close()

b = '%Y-%m-%d %H:%M:%S.%f'
t = datetime.datetime.strptime(today_string, b)
print(t)
print(type(t))
