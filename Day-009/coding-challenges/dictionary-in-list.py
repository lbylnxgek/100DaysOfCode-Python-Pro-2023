country = input("Country: ") # Add country name
visits = int(input("Number of visits: ")) # Number of visits
list_of_cities = eval(input("List of cities: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country_name, num_visits, cities_visited):
  travel_log.append({"country": country_name, "visits": num_visits, "cities": cities_visited})


# Do not change the code below
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
