"""
Pipeline - APIs.
Task 1: Where I Am?
"""


import requests


def sentientPlanets():
  """
  By using the Swap API create a method that returns
  the list of the home planets of all sentient species.

  Prototype: def sentientPlanets():
  > Dont forget the pagination <
  
  Sentient: type is either in the classification or designation attributes.
  """

  url = "https://swapi-api.hbtn.io/api/species/"
  planets = []

  while url:
      responses = requests.get(url)
      data = responses.json()
      for species in data['results']:
          if 'sentient' in species[
             'classification'].lower() or 'sentient' in species[
             'designation'].lower():
              if species['homeworld'] is not None:
                 home_response = requests.get(species['homeworld'])
                 planet_data = home_response.json()
                 planets.append(planet_data['name'])
      url = data['next']

  return planets

if __name__ == '__main__':
    planets = sentientPlanets()
    for planet in planets:
        print(planet)
