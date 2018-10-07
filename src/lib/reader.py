import re
from os import path


class READER(object):
    def __init__(self):
        try:
            with open("tsp_path.txt","r") as tsp:
                self._tsp_path = tsp.readline()
        except FileNotFoundError:
            with open("tsp_path.txt","w") as tsp:
                self._tsp_path = path.abspath("C:\\")
                tsp.write(self._tsp_path)

    def getPath(self):
        return self._tsp_path

    def setPath(self,path):
        self._tsp_path = path
        with open("tsp_path.txt","w")  as tsp:
            tsp.write(self._tsp_path)

    def readIn(self,problem_name):

        problem_file =  path.join(self._tsp_path, problem_name + '.tsp')
        problem_attrs = {"problem":problem_name,"size":None,"comment":""}
        try:
            with open(problem_file,"r") as tsp_attributes:
                nodes_start_line = 1

                for line in tsp_attributes.readlines():
                    a = re.match("(\w+)\s*:*\s*([\w]*)",line)
                    attr_label = a.group(1)
                    attr_value = a.group(2)
                    nodes_start_line += 1

                    if attr_label == "NODE_COORD_SECTION":
                        break
                    elif attr_label == "DIMENSION":
                        problem_attrs["size"] = int(attr_value) 
                    elif attr_label == "COMMENT":
                        problem_attrs["comment"] += line.split(":")[1].lstrip().replace("\n"," ")

            with open(problem_file,"r") as tsp_nodes:
                nodes = []
                for node in tsp_nodes.readlines()[nodes_start_line-1:-1]:
                    node_list = list(filter(None,node.strip().replace("\n","").split(" ")))

                    nodes.append((int(node_list[0]),float(node_list[1]), float(node_list[2])))
            return  problem_attrs,nodes
        except FileNotFoundError as e:
            raise e

