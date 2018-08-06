import sys
from lib.tsp_node import TSP_NODE
import os.path as path
import pickle
import subprocess

tsp_file_name = "a280.tsp" #sys.argv[1]
tsp_allowed_time = None#sys.argv[2]

tsp_file_path = path.join('tsp_files',tsp_file_name)
tsp_file_handler = open(tsp_file_path,'r')
tsp_file_nodes = tsp_file_handler.readlines()
tsp_file_handler.close()

#Set object information about the problem from the file
tsp_node_obj = TSP_NODE(
name = tsp_file_nodes[0],
time_allowed = tsp_allowed_time, 
comments = tsp_file_nodes[1],
type_ = tsp_file_nodes[2],
dimension = tsp_file_nodes[3],
ewt = tsp_file_nodes[4]
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

pickle.dump(tsp_node_obj,open("objects/tsp_node_obj.p","wb"))
subprocess.call("python solver.py")