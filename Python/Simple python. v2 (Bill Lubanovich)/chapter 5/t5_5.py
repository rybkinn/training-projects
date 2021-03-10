"""Присвойте значения переменным 'salutation', 'name', 'product',
'verbed' (глагол в прошедшем времени), 'room', 'animals', 'percent',
'spokesman' и 'job_title'.
С помощью функции letter.format() выведите на экран значение переменной letter,
в которую подставлены эти значения."""

salutation = 'Good day'
name = 'Tom'
product = 'keyboard'
verbed = 'saw'
room = '88'
animals = 'dog'
amount = '21'
percent = '70'
spokesman = 'Bill Lubanovich'
job_title = 'writer'

letter = '''Dear {0} {1},
Thank you for your letter. We are sorry that our {2}
{3} in your {4}. Please note that it should never
be used in a {4}, especially near any {5}.
Send us your receipt and {6} for shipping and handling.
We will send you another {2} that, in our tests,
is {7}% less likely to have {3}.
Thank you for your support.
Sincerely,
{8}
{9}'''.format(salutation, name, product, verbed, room, animals, amount, percent, spokesman, job_title)

print(letter)
