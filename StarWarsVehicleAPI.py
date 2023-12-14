import requests

def sw_vehicle_search(cargo_capacity: int, max_speed: int, cost: int) -> list:
    """
    Searches the Star Wars API for vehicles that match the specified criteria.

    Parameters:
    cargo_capacity (int): The minimum cargo capacity of the vehicle in kilograms.
    max_speed (int): The minimum max atmospheric speed of the vehicle.
    cost (int): The maximum cost of the vehicle in Galactic Credits.

    Returns:
    list: A list of vehicle names that meet the criteria.
    """

    vehicles = []
    url = "https://swapi.dev/api/vehicles/"

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        for vehicle in data['results']:
            try:
                vehicle_cost = int(vehicle['cost_in_credits']) if vehicle['cost_in_credits'].lower() not in ["unknown", "none"] else float('inf')
                vehicle_cargo_capacity = int(vehicle['cargo_capacity']) if vehicle['cargo_capacity'].lower() not in ["unknown", "none"] else 0
                vehicle_max_speed = int(vehicle['max_atmosphering_speed']) if vehicle['max_atmosphering_speed'].lower() not in ["unknown", "none"] else 0

                if (vehicle_cargo_capacity >= cargo_capacity and 
                    vehicle_max_speed >= max_speed and 
                    vehicle_cost <= cost):
                    vehicles.append(vehicle['name'])
            except ValueError:
                continue

        url = data['next']

    return vehicles

example_vehicles = sw_vehicle_search(1000, 150, 100000)
print(example_vehicles)
