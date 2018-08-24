import re

def reader(tsp_node_file):

    tsp_nodes = open(tsp_node_file,"r")
    current_line = 1
    node_reader = {
        "name":None,
        "comments":None,
        "type":None,
        "dimension":None,
        "edge-weight-type":None,
        "tour":[]
    }
    for line in tsp_nodes.readlines():
        a = re.match("(\w+)\s*:*\s*([\w\s]+)",line)
        b = a.group(1)
        c = a.group(2)

        if b == "NODE_COORD_SECTION":
            break
        elif b == "NAME":
            node_reader["name"] = c
        elif b == "COMMENT":
            node_reader["comments"] = c
        elif b == "TYPE":
            node_reader["type"] = c
        elif b == "DIMENSION":
            node_reader["dimension"] = c
        elif b == "EDGE_WEIGHT_TYPE":
            node_reader["edge-weight-type"] = c
        current_line += 1
    tsp_nodes.close()
    with open(tsp_node_file,"r") as tsp_nodes:
        for node in tsp_nodes.readlines()[current_line:-1]:
            node_list = list(filter(None,node.strip().replace("\n","").split(" ")))
            node_reader["tour"].append([int(node_list[0]),float(node_list[1]),float(node_list[2])])
    return node_reader
