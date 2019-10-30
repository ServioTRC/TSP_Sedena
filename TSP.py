#! /usr/bin/python3
import time
import argparse
from pprint import pprint
from algorithms.brute_force import brute
from CSV_formater import obtain_cities_from_csv, cities_to_csv, evolution_to_csv
from algorithms.genetic import geneticAlgorithm


def genetic(filtered_list, search_city):
    start_time = time.time()
    best_route, cost_track = geneticAlgorithm(population=filtered_list, popSize=400,
                                              eliteSize=20, mutationRate=0.01,
                                              generations=1000, origin_city=search_city,
                                              crossover=300)
    print(time.time() - start_time)
    cities_to_csv(best_route, "Output.csv")
    evolution_to_csv(cost_track, "Costs_Evolution.csv")

# def brute(filtered_list, search_city):
#     print('NOT IMPLEMENTED YET')


def main():
    # Parse arguments to run either brute or genetic algorithm.
    parser = argparse.ArgumentParser()
    parser.add_argument('--genetic', default=False, dest='genetic', action='store_true',
                        help='Runs genetic algorithm for the TSP program')
    parser.add_argument('--brute', default=False, dest='brute', action='store_true',
                        help='Runs brute force algorithm for the TSP program')
    args = parser.parse_args()

    # Filter cities from destination/rest.
    cityList = obtain_cities_from_csv("CiudadesMX.csv")
    origin_city = {"state": "Yucatan", "name": "Merida"}
    filtered_list = []
    for city in cityList:
        if city.name != origin_city["name"] and city.state != origin_city["state"]:
            filtered_list.append(city)
        else:
            search_city = city

    # Run corresponding algorithm
    if args.genetic:
        print('Running Genetic Algorithm')
        pprint(search_city)
        genetic(filtered_list, search_city)
    else:
        print('Running Brute Force Algorithm')
        brute(filtered_list, search_city)


if __name__ == '__main__':
    main()
