#!/usr/bin/python2.7
"""
Hadoop: Download files from HDFS.
"""


from snakebite.client import Client
import os



def download(file_list):
    """
    Retrieve files from HDFS and store them in the /tmp folder of the user.

    Args:
        file_list: list of file paths to be retrieved from HDFS.

    Returns: None
    """
    # initialize snakebite client
    client = Client("localhost", 9000)

    # iterate over each file(s) path in the list
    for file_path in file_list:
        # extract file name from the path
        file_name = os.path.basename(file_path)

        # download the file from HDFS
        with open(f"/tmp/{file_name}", "wb") as f:
            for chunk in client.cat([file_path]):
                f.write(chunk)



if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    download(l)
    with open("/tmp/lao.txt", "r") as f:
        print(f.read())
