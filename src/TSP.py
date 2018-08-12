import sys
import os.path as path
from lib.file_handler import create_node_object
from lib.solver import solve_tsp

tsp_file_name = sys.argv[1]
tsp_allowed_time = float(sys.argv[2])

tsp_file_path = path.join('tsp_files',tsp_file_name)


tsp_node_obj = create_node_object(tsp_file_path)
solve_tsp(tsp_node_obj.get_nodes(),tsp_allowed_time)