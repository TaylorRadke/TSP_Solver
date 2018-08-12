from .tsp_node_class import TSP_NODE
    
def create_node_object(tsp_node_file):

    tsp_nodes = open(tsp_node_file,"r").readlines()

    #file attribs from 0-6
    tsp_file_attributes = [line.replace(" ","").replace("\n","").split(":")[1] for line in tsp_nodes[:5]]

    node_object = TSP_NODE(
        name = tsp_file_attributes[0],
        comments = tsp_file_attributes[1],
        _type_ = tsp_file_attributes[2],
        dimension = tsp_file_attributes[3],
        ewt = tsp_file_attributes[4]
    )

    for node in tsp_nodes[6:-1]:
        node_list = list(filter(None,node.strip(" ").replace("\n","").split(" ")))
        node_object.add_node(
            node_list[0],
            node_list[1],
            node_list[2]
        )

    return node_object