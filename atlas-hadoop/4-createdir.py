#!/usr/bin/env python2.7
"""
Hadoop: Create Directories.
"""


from snakebite.client import Client


def createdir(l):
    """
    Create directories within HDFS.

    Args:
        l: list of directory paths to be created.

    Returns:
        None
    """
    client = Client('localhost', 9000)
    for dir_path in l:
        result = client.mkdir([dir_path], create_parent=True)
        print({'path': dir_path, 'result': next(result)['result']})

if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)