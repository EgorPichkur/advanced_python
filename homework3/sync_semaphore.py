"""Homework 3: Thread Synchronization Using Semaphores"""

from threading import Semaphore, Thread


class SemaphoreThread(Thread):
    """My thread to work with semaphores"""

    even_sem = Semaphore(1)
    odd_sem = Semaphore(0)

    def __init__(self, thread_name):
        super().__init__()

        self.thread_name = thread_name
        if self.thread_name == 'even':
            self.nums = [x for x in range(101) if x % 2 == 0]
        else:
            self.nums = [x for x in range(101) if x % 2 == 1]

    def run(self):
        """Implementation of thread's activity"""

        for num in self.nums:
            if self.thread_name == 'even':
                self.even_sem.acquire()
                print(num)
                self.odd_sem.release()
            else:
                self.odd_sem.acquire()
                print(num)
                self.even_sem.release()


if __name__ == '__main__':
    even_thread = SemaphoreThread('even')
    odd_thread = SemaphoreThread('odd')

    even_thread.start()
    odd_thread.start()
