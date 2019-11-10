# TSP_Sedena

Project for the Intelligent Systems class...

## Requirements

```
Python3
Pandas (pip3 install pandas)
```

Please don't forget to use Python3...

You shouldn't be using Python2 anyways...

hopefully..?

## Overview

"Given a set of cities and distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point." Sounds familiar? Of course it does!

The goal is to have an environment to visualize the Travelling Salesman Problem (TSP), after solving the problem for n cities using a genetic algorithm.

This project will also contain a brute force search which will be a DFS in order to compare different cases using our algorithm and mutation/breeding heuristics.

## Usage

To run:
```
chmod +x ./TSP.py
./TSP.py --genetic
./TSP.py --brute
```

## Dependencies

•	The code was developed and tested using Python 3.7.2
•	With the following libraries:
    o	Numpy 1.16.4
    o	Pandas 0.25.1
•	For displaying the results was used Tableau 2019.2.4



## General Description

The code in the proposed solution was based upon the one created by Eric Stoltz and this article: https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

The main changes are:
•	The inputs and outputs from the program.
•	Changes in the aspect that we need to return to the original city rather than just covering all of them.
•	Added a crossover of four points.
•	Keeps the routes with the least cost without altering it.
•	Variable sizes for the crossover of the population and the individual mutation.

The core file is TSP.py, receives one argument. Either “--brute” for running the full search algorithm or “--genetic” for the genetic one.

The input file with the city’s information (city, state, latitude, longitude) is selected by the function “obtain_cities_from_csv” at line 35. Also, it is needed to add the origin city, that must be in the city’s files, adding the state and name in the dictionary at line 36.

Once the algorithm finishes, it generates two CSV files: “Output.csv” and “Costs_Evolution.csv”. The first file contains the routes among the cities, the second one has the costs of each. They were developed so it could be easily displayed in Tableau. generation.


## Demonstrative video
https://youtu.be/PHpQOB4lWq4 
