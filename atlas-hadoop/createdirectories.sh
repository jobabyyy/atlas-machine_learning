#!/bin/bash
# HADOOP - bash scrip that creats the directory 'createdirectories'.

# holbies/ directory
hdfs dfs -mkdir -p /holbies

# now create the /holbies/input directpry
hdfs dfs -mkdir -p /holbies/input
