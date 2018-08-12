import matplotlib.pyplot as plt
import numpy as np

def build_plot(node_list):
    tour_length = node_list[0]

    node_list = list(node_list[1][:-1])
    
    x = [node[1] for node in node_list]
    x.append(x[0])
    y = [node[2] for node in node_list] 
    y.append(y[0])
    
  
    plt.plot(x,y)
    plt.show()