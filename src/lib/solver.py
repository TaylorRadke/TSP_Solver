import math
from time import time

def euclidean_distance(node1,node2):
    """Finds the euclidean distance between two nodes"""
    
    xd = abs(node1[1] - node2[1])
    yd = abs(node1[2] - node2[2])
    return math.sqrt(xd**2 + yd ** 2)

def find_next_shortest(node_list):
    """Finds the next closest node"""

    shortest_route = euclidean_distance(node_list[0],node_list[1])
    index_shortest_route = 1

    for i in range(2,len(node_list)-1):
        check_route = euclidean_distance(node_list[0],node_list[i])
        if (check_route < shortest_route):
            shortest_route = check_route
            index_shortest_route = i

    yield index_shortest_route,shortest_route



def greedy(node_list,allowed_time):
    """
    How it works\n
    (1) Add 0th element in node_list to tour_list as it is the current node
    (2) Get next closest node and add its distance to tour_length
    (3) set next node as 0th element in node_list so that it is now the current node
    (4) pop the next node from where it was to delete is duplicate
    ---------------------
    After completion need to get back to starting node
    (1) find the length from current node to start node and add the route distance to tour_length
    (2) Add current node to tour_list
    """

    tour_list = []
    tour_length = 0
    start_point = node_list[0]
    start_time = time()

    while(len(node_list)-1 > 0 and time() - start_time <= allowed_time):
        tour_list.append(node_list[0])
        next_node = list(find_next_shortest(node_list))
        tour_length += next_node[0][1]
        next_node_index = next_node[0][0]
        node_list[0] = node_list[next_node_index]
        node_list.pop(next_node_index)
    
    node_list.append(start_point)
    tour_length += euclidean_distance(node_list[0],node_list[1])
    tour_list.append(node_list[0])
    tour_list.append(-1)
    return tour_length,tour_list