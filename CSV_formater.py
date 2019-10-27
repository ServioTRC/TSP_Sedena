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


def cities_to_csv(cities_list, filename):
    cities_file = open(filename, "w", encoding="utf8")
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


def evolution_to_csv(costs_list, filename):
    costs_file = open(filename, "w", encoding="utf8")
    costs_file.write(f"id,cost\n")
    for index, cost in enumerate(costs_list):
        costs_file.write(f"{index},{cost}\n")
    costs_file.close()
