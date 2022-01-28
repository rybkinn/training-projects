"""Определите исключение OopsException. Сгенерируйте его и посмотрите, что произойдет.
Затем напишите код, позволяющий поймать это исключение и вывести строку 'Caught an oops'."""


class OopsException(Exception):
    pass


# raise OopsException

try:
    raise OopsException('Caught an oops')
except OopsException as oe:
    print(oe)
