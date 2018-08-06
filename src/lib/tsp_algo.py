import math


def eu_dist(node1,node2):
    xd = abs(int(node1[1]) - int(node2[1]))
    yd = abs(int(node1[2]) - int(node2[2]))
    return math.sqrt(xd**2 + yd ** 2)

def greedy(node_list):
    """
    (1) Add the current node to list
    (2) Find the next shortest path
    (3) Set current to next
    (4) Pop previous node from main list
    """
    route_length = []

    for i in range(0,len(node_list)):
        for j in range(0,len(node_list)):
            route_length.append([node_list[i][0],eu_dist(node_list[i],node_list[j])])


def findNextShortest():
    pass