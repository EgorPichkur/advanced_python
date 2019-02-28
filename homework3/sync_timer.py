"""Homework 3: Thread Synchronization Using Timer"""

from threading import Timer
from time import sleep


def timer_thread(start_num, sleep_time):
    for num in range(start_num, 101, 2):
        print(num)
        sleep(sleep_time)


if __name__ == '__main__':
    sleep_time = 1
    even_start_num = 0
    odd_start_num = 1

    even_thread = Timer(sleep_time / 2, timer_thread,
                        args=[even_start_num, sleep_time])
    odd_thread = Timer(sleep_time, timer_thread,
                       args=[odd_start_num, sleep_time])

    even_thread.start()
    odd_thread.start()
