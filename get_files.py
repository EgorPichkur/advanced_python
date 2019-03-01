"""This module exports a function that gets a list of files"""
import os


def get_files_list(url='http://ftp.mgts.by/test/'):
    """Creates a list of links

    This function creates a list of links to files
    for downloading"""

    url = 'http://ftp.mgts.by/test/'
    files = ("10Mb.txt", "50Mb.txt", "100Mb.txt")

    return [os.path.join(url, f) for f in files]
