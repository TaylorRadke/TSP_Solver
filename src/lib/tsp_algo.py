import math


def eu_dist(node1,node2):
    xd = abs(int(node1[1]) - int(node2[1]))
    yd = abs(int(node1[2]) - int(node2[2]))
    return math.sqrt(xd**2 + yd ** 2)



def findNextShortest(node_list):
    route_length = []
    for i in range(1,len(node_list)):
        route_length.append((i,eu_dist(node_list[0],node_list[i])))
    route_length.sort(key = lambda x: x[1])
    return route_length[0]


def greedy(node_list):
    """
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

    while(len(node_list)-1 > 0 ):
        tour_list.append(node_list[0])
        next_node = findNextShortest(node_list)
        tour_length += next_node[1]
        next_node_index = next_node[0] - 1
        node_list[0] = node_list[next_node_index]
        node_list.pop(next_node_index)
    
    node_list.append(start_point)
    tour_length += eu_dist(node_list[0],node_list[1])
    tour_list.append(node_list[0])
    tour_list.append(-1)
    return (tour_length,tour_list)
