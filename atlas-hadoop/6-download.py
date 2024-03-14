#!/usr/bin/python2.7
"""
Hadoop: Download files from HDFS.
"""


from snakebite.client import Client




def download(file_list):
    """
    Retrieve files from HDFS and store them in the /tmp folder of the user.

    Args:
        file_list: list of file paths to be retrieved from HDFS.

    Returns: None
    """
    client = Client('localhost', 9000)

    for file_path in client.copyToLocal(l, '/tmp'):
        print(file_path)