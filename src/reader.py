import re


def reader(problem_file):

    tsp_nodes = open(problem_file,"r")
    current_line = 1
    node_reader = {
        "name":None,
        "dimension":None,
        "distance":None,
        "tour":[]
    }

    for line in tsp_nodes.readlines():
        a = re.match("(\w+)\s*:*\s*([\w]*)",line)
        attr_label = a.group(1)
        attr_value = a.group(2)

        if attr_label == "NAME":
            node_reader["name"] = attr_value

        elif attr_label == "NODE_COORD_SECTION":
            break   
        current_line += 1

    tsp_nodes.close()

    with open(tsp_node_file,"r") as tsp_nodes:
        for node in tsp_nodes.readlines()[current_line:-1]:
            node_list = list(filter(None,node.strip().replace("\n","").split(" ")))
            node_reader["tour"].append([int(node_list[0]),float(node_list[1]),float(node_list[2])])
    return node_reader
