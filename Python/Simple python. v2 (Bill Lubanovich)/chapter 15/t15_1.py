"""
Используйте модуль multiprocessing, чтобы создать три отдельных процесса.
Заставьте каждый из них подождать случайное количество секунд между
нулем и единицей, вывести текущее время, а затем завершить работу.
"""
import multiprocessing
import random
import datetime
import time


def printTime():
    rnd_time = random.random()
    print(f'Wait time: {rnd_time} seconds')
    time.sleep(rnd_time)
    print(f'Time is: {datetime.datetime.now().time()}\n')


if __name__ == "__main__":
    for numb_proc in range(3):
        p = multiprocessing.Process(target=printTime())
        p.start()
