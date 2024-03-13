#!/usr/bin/python2.7
"""
Hadoop: Deletes Directories.
"""


from snakebite.client import Client



def deletedir(l):
    """
    Remove directories within HDFS.

    l: list of directory paths to be removed.

    Returns: None
    """
    # initialize snakebite client
    client = Client("localhost", 9000)

    # removing the directories
    for direct_path in l:
        client.rmdir([direct_path], recursive=True)



if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
