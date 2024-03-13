#!/usr/bin/python2.7


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
    client = Client("localhost", 9000)

    # create directories
    for dir_path in l:
        client.mkdir([dir_path], create_parent=True)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
