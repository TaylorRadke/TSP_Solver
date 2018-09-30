import re
from sys import path
import sys

class READER(object):
    def __init__(self,path):
        self._tsp_path = path


    def readIn(self,problem_name):

        problem_file =  self._tsp_path + problem_name + '.tsp'
        problem_attrs = {"problem":problem_name,"size":None,"comment":None}
        try:
            tsp_nodes = open(problem_file,"r")
        except FileNotFoundError as e:
            raise e

        nodes_start_line = 1

        for line in tsp_nodes.readlines():
            a = re.match("(\w+)\s*:*\s*([\w]*)",line)
            attr_label = a.group(1)
            attr_value = a.group(2)
            nodes_start_line += 1

            if attr_label == "NODE_COORD_SECTION":
                break
            elif attr_label == "DIMENSION":
                problem_attrs["size"] = int(attr_value) 
            elif attr_label == "COMMENT":
                problem_attrs["comment"] = attr_value
        tsp_nodes.close()

        with open(problem_file,"r") as tsp_nodes:
            nodes = []
            for node in tsp_nodes.readlines()[nodes_start_line-1:-1]:
                node_list = list(filter(None,node.strip().replace("\n","").split(" ")))

                nodes.append((node_list[0],node_list[1], node_list[2]))

        return  problem_attrs,nodes

