import requests

def borders(country_name_a: str, country_name_b: str) -> bool:
    """
    Uses the Rest Countries API to determine if two countries are neighbors.

    Parameters:
    country_name_a (str): Partial name of the first country.
    country_name_b (str): Partial name of the second country.

    Returns:
    bool: True if a country matching `country_name_a` borders a country matching `country_name_b`, otherwise False.
    """

    response_a = requests.get(f"https://restcountries.com/v3.1/name/{country_name_a}")
    if response_a.status_code != 200:
        return False
    countries_a = response_a.json()

    response_b = requests.get(f"https://restcountries.com/v3.1/name/{country_name_b}")
    if response_b.status_code != 200:
        return False
    countries_b = response_b.json()

    cca3_codes_b = {country['cca3'] for country in countries_b}

    for country_a in countries_a:
        if 'borders' not in country_a:
            continue

        if any(border in cca3_codes_b for border in country_a['borders']):
            return True

    return False

example_result_1 = borders("united", "united")
example_result_2 = borders("sweden", "republic")
example_result_3 = borders("united", "tanzania")
example_result_4 = borders("british", "sweden")

example_result_1, example_result_2, example_result_3, example_result_4
