#!/usr/bin/env python3


import requests
from collections import defaultdict


def fetch_launches():
    """
    - Use this https://api.spacexdata.com/v3/launches to make request
    - All launches should be taking in consideration
    - Each line should contain the rocket name and the number of launches separated
      by : (format below in the example)
    - Order the result by the number launches (descending)
    - If multiple rockets have the same amount of launches, order them by alphabetic order (A to Z)
    - Your code should not be executed when the file is
      imported (you should use if __name__ == '__main__':)
        """
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
        rocket_launch_count = defaultdict(int)

        for launch in launches:
            rocket_name = launch['rocket']['rocket_name']
            rocket_launch_count[rocket_name] += 1

        # sort number of launches descending, then by rocket name
        sorted_rockets = sorted(rocket_launch_count.items(), key=lambda x: (-x[1], x[0]))

        for rocket in sorted_rockets:
            print(f"{rocket[0]}: {rocket[1]}")

if __name__ == '__main__':
    fetch_launches()
