import math
from time import time


def euclidean_distance(node1, node2):
    """Finds the euclidean distance between two nodes"""

    xd = abs(node1[1] - node2[1])
    yd = abs(node1[2] - node2[2])
    return math.sqrt(xd**2 + yd ** 2)


def euclidean_sum(a):
    sum = 0
    for i in range(len(a)-1):
        sum += euclidean_distance(a[i], a[i+1])
    sum += euclidean_distance(a[0], a[-1])
    return sum


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

def greedy(node_list):
    tour_list = []
    tour_length = 0
    start_point = node_list[0]

    while(len(node_list)-1 > 0):
        tour_list.append(node_list[0])
        next_node = list(find_next_shortest(node_list))
        tour_length += next_node[0][1]
        next_node_index = next_node[0][0]
        node_list[0] = node_list[next_node_index]
        node_list.pop(next_node_index)
    
    node_list.append(start_point)
    tour_length += euclidean_distance(node_list[0],node_list[1])
    tour_list.append(node_list[0])

    return tour_list


def opt_swap_2(route,i,k):

    new_tour = []
    new_tour[0:i-1] = [route[j] for j in range(0, i)]
    new_tour[i:k-1] = reversed(route[i:k])
    new_tour[k:] = route[k:]

    return new_tour


def opt2(route):
    best_distance = euclidean_sum(route)

    for i in range(1, len(route)-1):
        for k in range(i+1,len(route)):
            new_route = opt_swap_2(route[:], i, k)
            new_distance = euclidean_sum(new_route)
            if new_distance < best_distance:
                best_distance = new_distance
                route = new_route
    return route


def greedy2opt(node_list,allowed_time):
    start_time = time()
    route = greedy(node_list[:])

    improved = True

    while improved and time() - start_time <= allowed_time:
        s_route = route[:]
        route = opt2(route[:])
        if s_route == route:
            improved = False

    return euclidean_sum(route),route



