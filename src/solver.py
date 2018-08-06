import pickle
import math
from lib.tsp_algo import eu_dist,greedy

tsp_node_obj = pickle.load(open("objects/tsp_node_obj.p",'rb'))
tsp_nodes_list = tsp_node_obj.get_nodes()

tour_length_list = []
total_route_length = 0

greedy(tsp_nodes_list)


# for i in tour_length_list:
#     print(i)