#!/usr/bin/env python3


"""
Pipeline: APIs.
Task 2: Rate Me is You Can!
"""


import requests
import sys
from datetime import datetime, timezone


def get_user_location(api_url):
    """
    By using the GitHub API, write a script that prints the location of a specific user:

    - The user is passed as first argument of the script with the full API URL,
      example: ./2-user_location.py https://api.github.com/users/holbertonschool
    - If the user doesn’t exist, print Not found
    - If the status code is 403, print Reset in X min where X is the number of minutes
      from now and the value of X-Ratelimit-Reset
    - Your code should not be executed when the file is
      imported (you should use if __name__ == '__main__':)
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get('location')

            if location:
                print(location)
            else:
                print("Location not available")
        elif response.status_code == 404:
            print("Not found")

        elif response.status_code == 403:
            reset_timestamp = int(response.headers.get('X-Ratelimit-Reset', 0))
            reset_time = datetime.fromtimestamp(reset_timestamp, tz=timezone.utc)
            now_time = datetime.now(timezone.utc)
            minutes_until_reset = (reset_time - now_time).total_seconds() / 60
            print(f"Reset in {int(minutes_until_reset)} min")

        else:
            print(f"An error occurred: HTTP {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# test file
if __name__ == '__main__':
    if len(sys.argv) == 2:
        api_url = sys.argv[1]
        get_user_location(api_url)
