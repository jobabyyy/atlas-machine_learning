"""
Pipeline - APIs.
Task 0: Can I Join?
"""


import requests


def availableShips(passengerCount):
    """
    By using the Swap API, create a method that returns
    the list of ships that can hold a given number of
    passengers.

    Prototype: availableShips
    > dont forget the pagination

    Return: empty list if no ship available.
    """
    url = "https://swapi.dev/api/starships/"
    ships = []

    # iterate through pages until no more results are available
    while url:
        response = requests.get(url)
        data = response.json()
        
        # Extract starships from the current page
        for ship in data['results']:
            passengers = ship['passengers']

            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship['name'])

        url = data['next']
    
    return ships

if __name__ == '__main__':
    ships = availableShips(4)
    if ships:
        for ship in ships:
            print(ship)
    else:
        print("No ships available for the given passenger count.")
