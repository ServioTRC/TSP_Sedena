from City import City


def obtain_cities_from_csv(filename):
    cities = []
    cities_file = open(filename, "r", encoding="utf8")
    for line in cities_file.readlines()[1:]:
        values = line.split(',')
        estado = values[1]
        ciudad = values[2]
        lat = float(values[3])
        lon = float(values[4])
        cities.append(City(state=estado, name=ciudad, lat=lat, lon=lon))
    cities_file.close()
    return cities


def cities_to_csv(cities_list):
    cities_file = open("Output.csv", "w", encoding="utf8")
    for city in cities_list:
        cities_file.write(city.csv_representation())
        cities_file.write("\n")
    cities_file.close()
