def output(tsp_node_dict):
    print(tsp_node_dict["name"])
    print("Shortest Found Tour Length: " + str(tsp_node_dict["distance"]))
    print("Tour: ")

    for node in tsp_node_dict["tour"][:-1]:
        print(node)
    print(-1)