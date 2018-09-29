import re
import sys
sys.path.append("..")
from lib.queries import *


def reader(problem_file,problem_name,db):

    #  Check if problem file exists
    try:
        tsp_nodes = open(problem_file,"r")
    except FileNotFoundError as e:
        raise e

    current_line = 1
    for line in tsp_nodes.readlines():
        a = re.match("(\w+)\s*:*\s*([\w]*)",line)
        attr_label = a.group(1)
        attr_value = a.group(2)
        current_line += 1

        if attr_label == "NODE_COORD_SECTION":
            break
        elif attr_label == "DIMENSION":
            dimension = int(attr_value) 
        elif attr_label == "COMMENT":
            comment = attr_value

    tsp_nodes.close()


    with open(problem_file,"r") as tsp_nodes:
        count = 0
        db.query(sql_add_problem.format(
            name = problem_name,
            size = dimension,
            comment = comment))

        for node in tsp_nodes.readlines()[current_line-1:-1]:
            node_list = list(filter(None,node.strip().replace("\n","").split(" ")))
            print("Adding nodes for " + problem_name + ": {}/{}".format(count,dimension),end="\r",flush=True)
            count += 1
            node = node_list[0]
            x = node_list[1]
            y = node_list[2] 
            db.query(sql_add_cities.format(name = problem_name,id = node,x = x,y = y))

        db.save()      

