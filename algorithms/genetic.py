import argparse
import numpy as np, random, operator
import pandas as pd
from pprint import pprint
from algorithms.brute_force import brute
from Fitness import Fitness
from CSV_formater import obtain_cities_from_csv, cities_to_csv, evolution_to_csv


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


def swap_random(seq, size):
    idx = range(len(seq)-2)
    value = len(seq)
    for _ in range(1000):
        i1, i2 = random.sample(idx, 2)
        if i1+1+size < value and i2+1+size < value and not(set(range(i1+1, i1+1+size)).intersection(set(range(i2+1, i2+1+size)))):
            seq[i1+1:i1+1+size], seq[i2+1:i2+1+size] = seq[i2+1:i2+1+size], seq[i1+1:i1+1+size]
            return seq
    return seq


def breedPopulation(matingpool, eliteSize, crossover, crossover_size):
    children = []
    crossover = 0 if crossover <= 0 else crossover
    crossover_end = eliteSize + crossover
    # pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(eliteSize, crossover_end):
        #children.append(matingpool[i])
        children.append(swap_random(matingpool[i], crossover_size))

    for i in range(crossover_end, len(matingpool)):
        child = breed(matingpool[i], matingpool[len(matingpool)-i-1])
        children.append(child)

    return children


def mutate(individual, mutationRate):
    # Mutaciones de multiples grupos
    for swapped in range(1, len(individual) - 2):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * (len(individual) - 2)) + 1

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual


def mutatePopulation(population, mutationRate, beginning):
    mutatedPop = []
    for ind in range(0, len(population)):
        if ind <= beginning:
            mutatedPop.append(population[ind])
        else:
            mutatedInd = mutate(population[ind], mutationRate)
            mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate, crossover, crossover_size):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize, crossover, crossover_size)
    nextGeneration = mutatePopulation(children, mutationRate, eliteSize+crossover)
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations, origin_city, crossover):
    cost_track = []
    pop = initialPopulation(popSize, population, origin_city)
    initial_distance = str(1 / rankRoutes(pop)[0][1])
    fifth = popSize // 5 
    values = {fifth * 1: True, fifth * 2: True, fifth * 3: True, fifth * 4: True}
    crossover_size = 4

    for i in range(0, generations):
        if i % 100 == 0:
            print(f"Generation number {i} out of {generations}")
        if values.get(i):
            crossover_size -= 1
            crossover -= 50
        pop = nextGeneration(pop, eliteSize, mutationRate, crossover, crossover_size)
        cost_track.append(str(1 / rankRoutes(pop)[0][1]))

    print("Initial distance: " + initial_distance)
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute, cost_track
