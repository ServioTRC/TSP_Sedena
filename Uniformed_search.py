import numpy as np, random, operator
from CSV_formater import obtain_cities_from_csv

cityList = obtain_cities_from_csv("CiudadesMX.csv")
origin_city = {"state": "Yucatan", "name": "Merida"}
filtered_list = []
for city in cityList:
    if city.name != "Merida" and city.state != "Yucatan":
        filtered_list.append(city)
    else:
        search_city = city

salida = []
previous_city = search_city
used = True
while filtered_list:
    if len(filtered_list) > 31/2:
        min_distance = None
        min_city_pos = None 
        for index, city in enumerate(filtered_list):
            current = city.distance(previous_city)
            if not min_distance or current < min_distance:
                min_distance = current
                min_city_pos = index
        salida.append(filtered_list[min_city_pos])
        del(filtered_list[min_city_pos])
    else:
        min_distance = None
        min_city_pos = None 
        for index, city in enumerate(filtered_list):
            current = city.distance(previous_city)
            if not min_distance or current > min_distance:
                min_distance = current
                min_city_pos = index
        salida.append(filtered_list[min_city_pos])
        del(filtered_list[min_city_pos])


def cities_to_csv(cities_list):
    cities_file = open("Output_Uninformed.csv", "w", encoding="utf8")
    count = 1
    size = len(cities_list)
    cities_file.write(f"id,ciudad,estado,lat,lon\n")
    for index, city in enumerate(cities_list):
        if index + 1 < size:
            cities_file.write(f"{count},")
            cities_file.write(city.csv_representation())
            cities_file.write("\n")
            cities_file.write(f"{count},")
            cities_file.write(cities_list[index + 1].csv_representation())
            cities_file.write("\n")
            count += 1
    cities_file.close()


salida.insert(0, search_city)
salida.append(search_city)
cities_to_csv(salida, "Output_Uninformed.csv")
