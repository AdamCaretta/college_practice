import requests

def starship_piloted_species(starship: str) -> list:
    """
    Uses the Star Wars API to retrieve information regarding species that piloted a specified starship.

    Parameters:
    starship (str): The name of the starship in the Star Wars universe.

    Returns:
    list: A list of species names that piloted the given starship.
    """

    species_set = set()

    starships_url = "https://swapi.dev/api/starships/"
    while starships_url:
        starships_response = requests.get(starships_url)
        if starships_response.status_code != 200:
            break

        starships_data = starships_response.json()
        for starship_data in starships_data['results']:
            if starship_data['name'].lower() == starship.lower():
                for pilot_url in starship_data['pilots']:
                    pilot_response = requests.get(pilot_url)
                    if pilot_response.status_code == 200:
                        pilot_data = pilot_response.json()

                        if pilot_data['species']:
                            species_response = requests.get(pilot_data['species'][0])
                            if species_response.status_code == 200:
                                species_data = species_response.json()
                                species_set.add(species_data['name'])
                        else:
                            species_set.add("Human")
                break

        starships_url = starships_data['next']

    return list(species_set)


example_species = starship_piloted_species("Millennium Falcon")
print(example_species)
