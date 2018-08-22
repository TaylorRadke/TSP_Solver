import sys
import os.path as path
from lib.file_handler import create_node_object
from lib.solver import greedy3opt
from lib.tsp_plot import build_plot

def main(tsp_file_name,tsp_allowed_time): 

    tsp_allowed_time = tsp_allowed_time

    tsp_file_path = path.join('tsp_files',tsp_file_name)
    tsp_node_obj = create_node_object(tsp_file_path)

    shortest = greedy3opt(tsp_node_obj.get_nodes(),tsp_allowed_time)
    build_plot(shortest)
    # print(tsp_file_name)
    # print("Shortest found tour length: " + str(shortest[0]))
    # print("Tour: ")
    # for route in shortest[1][:-1]:
    #     print(route[0])
    # print(shortest[1][-1])
    

if __name__ == "__main__":
    # main(sys.argv[1],sys.argv[2])
    main("d18512.tsp",20)