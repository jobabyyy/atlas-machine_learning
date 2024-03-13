#!/bin/bash
# bash script that uploads the file lao.txt to the /holbies/input directory.

hdfs dfs -touchz /holbies/input/lao.txt
