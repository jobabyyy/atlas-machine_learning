#!/usr/bin/env python3
"""
Hadoop: Mapper.
"""


import csv
import sys


def mapper(csv_file):
    """
    Process the rows of the salaries.csv file and print id, 
    company, and totalyearlycompensation.

    Args:
    csv_file: Path to the salaries.csv file.

    Returns: None
    """

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print id, company, and totalyearlycompensation in the desired format
            print(f"{row['id']}\t{row['company']},{row['totalyearlycompensation']}")
