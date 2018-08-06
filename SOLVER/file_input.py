import random
import os

for files in os.listdir("/TSP"):
    tsp_file = open("/TSP/" + files,"r").readlines()
    for nodes in tsp_file[6:-1]:
        nodes = nodes.lstrip().split()
        nodes =  [files,nodes[0],nodes[1],nodes[2]]
