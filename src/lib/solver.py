from .tsp_algo import greedy
from time import time

def solve_tsp(node_list,allowed_time):

    start_time = time()
    shortest_tour = list(greedy(node_list))
    node_list.append(node_list.pop(0))

    for i in range(len(node_list)-1):
        if time() - start_time <= allowed_time:
            current_tour = list(greedy(node_list))
            if current_tour[0] < shortest_tour[0]:
                shortest_tour = current_tour
            node_list.append(node_list.pop(0))

        print("Time elapsed: {}".format(str(time()-start_time)), end = '\r',flush=True)
    
    print("Tour Length: " + str(shortest_tour[0]))
    print("Tour: ")
    for route in shortest_tour[1]:
        print(route)
  

    return shortest_tour