import numpy as np, random, operator
import pandas as pd
from Fitness import Fitness
from CSV_formater import obtain_cities_from_csv, cities_to_csv


def createRoute(cityList, origin_city):
    route = random.sample(cityList, len(cityList))
    route.insert(0, origin_city)
    route.append(origin_city)
    return route


def initialPopulation(popSize, cityList, origin_city):
    population = []
    for i in range(0, popSize):
        population.append(createRoute(cityList, origin_city))
    return population


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    origin_city = parent1[0]
    parent1 = parent1[1:-1]
    parent2 = parent2[1:-1]
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    child.insert(0, origin_city)
    child.append(origin_city)
    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(1, len(individual) - 1):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * (len(individual) - 1)) + 1

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations, origin_city):
    pop = initialPopulation(popSize, population, origin_city)
    initial_distance = str(1 / rankRoutes(pop)[0][1])

    for i in range(0, generations):
        if i % 100 == 0:
            print(f"Generation number {i} out of {generations}")
        pop = nextGeneration(pop, eliteSize, mutationRate)

    print("Initial distance: " + initial_distance)
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


cityList = obtain_cities_from_csv("CiudadesMX.csv")
origin_city = {"state": "Yucatan", "name": "Merida"}
filtered_list = []
for city in cityList:
    if city.name != "Merida" and city.state != "Yucatan":
        filtered_list.append(city)
    else:
        search_city = city
best_route = geneticAlgorithm(population=filtered_list, popSize=400,
                              eliteSize=20, mutationRate=0.01,
                              generations=10000, origin_city=search_city)

cities_to_csv(best_route)
