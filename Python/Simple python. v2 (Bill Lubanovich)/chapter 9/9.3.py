"""Определите декоратор test, который выводит строку 'start'
при вызове функции и строку 'end', когда функция завершает свою работу."""


def test(func):
    def new_test():
        print('start')
        func()
        print('end')
    return new_test


@test
def test_func():
    print('work func')


test_func()
