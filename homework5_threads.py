"""Homework 5: Downloading multiple files using threads"""
from get_files import get_files_list
import os
from queue import Queue
import threading
import time
import urllib.request


class DownloadThread(threading.Thread):
    """Implementation of a thread to download"""

    def __init__(self, queue, dest):
        super().__init__()
        self.queue = queue
        self.dest = dest
        self.daemon = True

    def run(self):
        "Implementation of thread's activity"
        while True:
            url = self.queue.get()
            try:
                self.download_url(url)
            except Exception as e:
                print("Error: {}".format(e))
            self.queue.task_done()

    def download_url(self, url):
        "Download a file from an URL"
        name = url.split('/')[-1]
        destfile = os.path.join(self.dest, name)
        print("downloading {} -> {}".format(url, destfile))
        urllib.request.urlretrieve(url, destfile)


def download(urls, destfolder, numthreads=2):
    """Threads master that controls downloading of all files"""
    queue = Queue()
    for url in urls:
        queue.put(url)

    for i in range(numthreads):
        t = DownloadThread(queue, destfolder)
        t.start()

    queue.join()


if __name__ == '__main__':
    files = get_files_list()
    start_time = time.time()
    download(files, '/tmp')
    print("Final time: {:.2f}".format((time.time() - start_time)))
