"""Homework 3: Thread Synchronization Using Events"""

from threading import Event, Thread


class EventThread(Thread):
    """My thread to work with events"""

    main_event = Event()

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
                while self.main_event.isSet():
                    pass
                print(num)
                self.main_event.set()
            else:
                self.main_event.wait()
                print(num)
                self.main_event.clear()


if __name__ == '__main__':
    even_thread = EventThread('even')
    odd_thread = EventThread('odd')

    odd_thread.start()
    even_thread.start()
