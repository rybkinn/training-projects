"""
Прочтите текстовый файл today.txt и разместите данные в строке today_string.
"""

with open('today.txt', 'r') as today_txt:
    today_string = today_txt.readline()
    today_txt.close()
print(today_string)
