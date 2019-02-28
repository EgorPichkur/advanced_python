"""Homework 3: Thread Synchronization Using Locks"""

from threading import Lock
from threading import Thread


class LockThread(Thread):
    """My thread to work with locks"""

    even_lock = Lock()
    odd_lock = Lock()

    def __init__(self, thread_name):
        super().__init__()

        self.thread_name = thread_name

        if self.thread_name == 'even':
            self.nums = [x for x in range(101) if x % 2 == 0]
            self.odd_lock.acquire()
        else:
            self.nums = [x for x in range(101) if x % 2 == 1]

    def run(self):
        """Implementation of thread's activity"""

        for num in self.nums:
            if self.thread_name == 'even':
                self.even_lock.acquire()
                print(num)
                self.odd_lock.release()
            else:
                self.odd_lock.acquire()
                print(num)
                self.even_lock.release()


if __name__ == '__main__':
    even_thread = LockThread('even')
    odd_thread = LockThread('odd')

    odd_thread.start()
    even_thread.start()
