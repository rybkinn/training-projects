"""
Напишите декоратор, оптимизирующий работу декорируемой функции. 
Декоратор должен сохранять результат работы функции на ближайшие 
три запуска и вместо выполнения функции возвращать сохранённый 
результат. После трёх запусков функция должна вызываться вновь, 
а результат работы функции — вновь кешироваться.
"""

def cache_numb(func):
    CACHE = 0
    CALL_COUNT = 0

    def wrapper(*args):
        nonlocal CACHE
        nonlocal CALL_COUNT
        CALL_COUNT += 1

        if CALL_COUNT == 1:
            CACHE = func(*args)
            return CACHE
        elif CALL_COUNT <= 3:
            return CACHE
        else:
            print('Функцию вызвали больше 3 раз.')
            CALL_COUNT = 1
            CACHE = func(*args)
            return CACHE

    return wrapper

@cache_numb
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(55)) # 55
print(sum_numbers(412, 1, 0, 73)) # 55
print(sum_numbers(5, 7, 3)) # 55

print(sum_numbers(2, 44, 245)) 
print(sum_numbers(43, 37, 13))
print(sum_numbers(26, 11, 9))

print(sum_numbers(12, 34, 10))
print(sum_numbers(12, 34, 10))
print(sum_numbers(12, 34, 10))

print(sum_numbers(10))
