import pickle
import math
from lib.tsp_algo import greedy

tsp_node_obj = pickle.load(open("objects/tsp_node_obj.p",'rb'))
tsp_node_list = tsp_node_obj.get_nodes()

newlist = greedy(tsp_node_list)

print(newlist[0])

for node in newlist[1]:
    print(node)
