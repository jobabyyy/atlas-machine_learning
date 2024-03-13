#!/usr/bin/env python3
"""
Hadoop: Reducer.
"""


import sys


def reducer():
    """
    Reduce function to find the top ten salaries
    sorted by totalyearlycompensation.

    Args: None

    Returns: None
    """
    # initialize an empty list to store the top ten salaries.
    top_salaries = []

    # iterate over each line of input from stdin.
    for line in sys.stdin:
        # split line into fields.
        fields = line.strip().split('\t')
        id_, company, total_yr_comp = fields

        # convert totalyearlycompensation to float.
        total_yr_comp = float(total_yearly_compensation)

        # adding the current salary to the list of top salaries.
        if len(top_salaries) < 10:
            top_salaries.append((id_, company, total_yr_comp))
        elif total_yr_comp > top_salaries[-1][2]:
            top_salaries.pop()
            top_salaries.append((id_, company, total_yr_comp))

        # sort top salaries list in descending order by totalyearlycompensation.
        top_salaries.sort(key=lambda x: x[2], reverse=True)

    # print the top ten salaries
    for salary in top_salaries:
        print('\t'.join(map(str, salary)))
