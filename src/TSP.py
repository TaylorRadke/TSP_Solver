import sys
import os.path as path
from lib.file_handler import create_node_object
from lib.solver import greedy
from time import time
from lib.tsp_plot import build_plot

def main(tsp_file_name,tsp_allowed_time): 
    tsp_file_name = sys.argv[1]
    tsp_allowed_time = float(tsp_allowed_time)

    tsp_file_path = path.join('tsp_files',tsp_file_name)
    tsp_node_obj = create_node_object(tsp_file_path)

    solved = greedy(tsp_node_obj.get_nodes(),tsp_allowed_time)
    print(tsp_file_name)
    print("Shortest found tour length: " + str(solved[0]))
    print("Tour: ")
    # for route in solved[1][:-1]:
    #     print(route[0])
    # print(solved[1][-1])
    build_plot(solved)

    
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
