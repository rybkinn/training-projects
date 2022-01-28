"""Используйте функцию zip(),
чтобы создать словарь из кортежа ключей ('optimist', 'pessimist', 'troll')
и кортежа значений ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')."""

t_key = ('optimist', 'pessimist', 'troll')
t_value = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

d = {key: value for key, value in zip(t_key, t_value)}

print(d)
