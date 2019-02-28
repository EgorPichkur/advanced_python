"""Homework 4: Multiprocessing"""

from multiprocessing import Lock
from multiprocessing import Process


class SyncedProcess(Process):
    """My class for multiprocessing work"""

    even_lock = Lock()
    odd_lock = Lock()

    def __init__(self, process_name):
        super().__init__()

        self.process_name = process_name

        if self.process_name == 'even':
            self.nums = [x for x in range(101) if x % 2 == 0]
            self.odd_lock.acquire()
        else:
            self.nums = [x for x in range(101) if x % 2 == 1]

    def run(self):
        """Implementation of process' activity"""

        for num in self.nums:
            if self.process_name == 'even':
                self.even_lock.acquire()
                print(num)
                self.odd_lock.release()
            else:
                self.odd_lock.acquire()
                print(num)
                self.even_lock.release()


if __name__ == '__main__':
    processes = []

    processes.append(SyncedProcess('odd'))
    processes.append(SyncedProcess('even'))

    for pr in processes:
        pr.start()

    for pr in processes:
        pr.join()
