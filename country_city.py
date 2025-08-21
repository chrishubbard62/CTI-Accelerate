num_countries = int(input())
city_map = {}

for i in range(num_countries):
  current = input().split()
  country = current[0]
  for i in range(1, len(current)):
    city_map[current[i]] = country

num_cities = int(input())

for i in range(num_cities):
  print(city_map[input()])
