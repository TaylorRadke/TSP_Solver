import sys
import os.path as path
from lib.tsp_node import TSP_NODE

tsp_node_obj = TSP_NODE()

tsp_folder = "tsp_files"
tsp_file_name = sys.argv[1]
tsp_allowed_time = sys.argv[2]
tsp_file_path = path.join(tsp_folder,tsp_file_name)

del tsp_folder

tsp_file_handler = open(tsp_file_path,'r')
tsp_file_nodes = tsp_file_handler.readlines()
tsp_file_handler.close()

#Set object information about the problem from the file
tsp_node_obj.set(
    name = tsp_file_nodes[0],
    time_allowed = tsp_allowed_time, 
    comments = tsp_file_nodes[1],
    type_ = tsp_file_nodes[2],
    dimension = tsp_file_nodes[3],
    edge_weight_type = tsp_file_nodes[4]
    )

#Add all nodes to object's node list
for tsp_nodes in tsp_file_nodes[6:-1]:
    tsp_nodes = tsp_nodes.lstrip().split()
    tsp_node_obj.add_node(
        tsp_nodes[0],
        tsp_nodes[1],
        tsp_nodes[2]
    ) 

del tsp_file_nodes
print(tsp_node_obj)
