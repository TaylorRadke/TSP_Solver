import sys
import os.path as path
from lib.reader import reader
from lib.solver import greedy2opt


def main(tsp_file_name,tsp_allowed_time): 

    tsp_allowed_time = tsp_allowed_time

    tsp_file_path = path.join('tsp_files',tsp_file_name)
    tsp_node_obj = reader(tsp_file_path)

    result = greedy2opt(tsp_node_obj["tour"], tsp_allowed_time)

    print(tsp_file_name)
    print("Shortest Found Tour Length: " + str(result[0]))
    print("Tour: ")
    for node in result[1]:
         print(node)
    print(-1)


if __name__ == "__main__":
    # main(sys.argv[1],sys.argv[2])
    main("berlin52.tsp",300)
