"""Homework 3: Thread Synchronization Using Conditions"""

from threading import Condition
from threading import Thread


def print_odd(cv):
    """Function to print odd numbers"""
    nums = [x for x in range(101) if x % 2 == 1]
    for num in nums:
        with cv:
            cv.wait()
            print(num)
            cv.notify()


def print_even(cv):
    """Function to print even numbers"""
    nums = [x for x in range(101) if x % 2 == 0]
    for num in nums:
        with cv:
            print(num)
            cv.notify()
            if (num != 100):
                cv.wait()


if __name__ == '__main__':
    condition = Condition()
    odd = Thread(name='odd', target=print_odd, args=(condition,))
    even = Thread(name='even', target=print_even, args=(condition,))

    odd.start()
    even.start()
