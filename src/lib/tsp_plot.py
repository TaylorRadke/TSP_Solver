import matplotlib.pyplot as plt


def build_plot(node_list):

    x = [x[1] for x in node_list]
    x.append(x[0])
    y = [y[2] for y in node_list]
    y.append(y[0])

    plt.plot(x,y)
    plt.show()