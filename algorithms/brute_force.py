import sys
import time
from pprint import pprint
sys.path.append("../")

from Degrees import obtain_distance_km

# The brute force of this algorithm for the project is a very naive and simple one given that there are no restrictions nor order on the cities that have to be visited.
# Given that the only cost consists of the distance between the cities, we can simply run a DFS traversal and backtrack to keep on finding the best path.

def brute(filtered_list, search_city):
    distance_list = traverse([search_city], filtered_list, 0)
    distance_list.sort(reverse=False)
    pprint(distance_list)

def traverse(city_stack, filtered_list, distance):
    # If all the cities have been reached, return to search_city.
    # Prints to console the distance taken to return.
    if len(filtered_list) == 0:
        # cities = list(map(lambda x: x.name, city_stack))
        # print((('=>'.join(cities))+'\t returned to '+cities[0]+' with distance %d')%distance)
        # print(obtain_distance_km(city_stack[-1], city_stack[0]))
        return distance + obtain_distance_km(city_stack[-1], city_stack[0])

    distance_list = []
    for city in filtered_list:
        # print("Moving from "+city_stack[-1].name+" to "+city.name)
        # Take out for backtrack.
        city_stack.append(city)
        cpy_filtered = list(filtered_list)
        cpy_filtered.remove(city)
        d = traverse(city_stack, cpy_filtered, distance + obtain_distance_km(city_stack[-1], city))
        if isinstance(d, int):
            distance_list.append(d)

        # Return to continue backtrack.
        city_stack.pop()
    
    return distance_list
