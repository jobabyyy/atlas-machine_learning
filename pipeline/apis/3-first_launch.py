#!/usr/bin/env python3
"""
Pipeline: APIs
Task 3: First Launch
"""


import requests


def fetch_first_launch():
    """
    By using the (unofficial) SpaceX API, write a script that displays the
    first launch with these information:

    - Name of the launch
    - The date (in local time)
    - The rocket name
    - The name (with the locality) of the launchpad
    """
    url = "https://api.spacexdata.com/v4/launches"
    launches_response = requests.get(url)


    if launches_response.status_code == 200:
        launches = launches_response.json()
        if launches:

            sorted_launches = sorted(launches, key=lambda x: x['date_unix'])
            first_launch = sorted_launches[0]

            rocket_url = f"https://api.spacexdata.com/v4/rockets/{first_launch['rocket']}"
            response = requests.get(rocket_url)
            rocket_name = (
                response.json()['name'] if response.status_code == 200 else "Unknown Rocket")


            launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{first_launch['launchpad']}"
            launchpad_response = requests.get(launchpad_url)
            if launchpad_response.status_code == 200:
                launchpad_data = launchpad_response.json()
                launchpad_name = launchpad_data['name']
                launchpad_locality = launchpad_data['locality']
            else:
                launchpad_name = "Unknown Launchpad"
                launchpad_locality = "Unknown Locality"

            launch_date = first_launch['date_local']

            print(f"{first_launch['name']} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
        else:
            print("No launches found.")
    else:
        print("Failed to fetch launches.")

if __name__ == '__main__':
    fetch_first_launch()
