import math
from time import time

def euclidean_distance(node1,node2):
    """Finds the euclidean distance between two nodes"""
    
    xd = abs(node1[1] - node2[1])
    yd = abs(node1[2] - node2[2])
    return math.sqrt(xd**2 + yd ** 2)

def euclidean_sum(a):
    a_sum = 0
    for i in range(len(a)-1):
        a_sum += euclidean_distance(a[i],a[i+1])
    return a_sum

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

    return tour_length,tour_list

def swap(node_list,i,j):

    temp = node_list[i]
    node_list[i] = node_list[j]
    node_list[j] = temp


def greedy3opt(node_list,allowed_time):

    start_time = time()
    greedy_result = greedy(node_list)

    s = greedy_result[1]
    z = greedy_result[0]
    print(z)

    while True:
        s_star = [node for node in s]
        z_star = z
        print(time() - start_time)
        for i in range(1,len(s)):
            for j in range(i+1,len(s)):
                s_dash = [s_star[i],s_star[j]]
                z_dash = euclidean_distance(s_dash[0],s_dash[1])
                if z_dash < z_star:
                    print(z_dash,flush=True)
                    z_star = z_dash
                    swap(s_star,i+1,j)

        if s != s_star:
            s = s_star
            z = z_star

        elif s == s_star:
            print(euclidean_sum(s_star))
            return s_star


