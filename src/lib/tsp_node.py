class TSP_NODE(object):
    def __init__(self):
        self.__name = None
        self.__time_allowed = None
        self.__comments = None
        self.__type = None
        self.__dimension = None
        self.__edge_weight_type = None
        self.__nodes = []
    
    def __str__(self,*args):
        print(
            self.__name +\
            "Allowable Seconds : " + self.__time_allowed + "\n" +\
            self.__type +\
            self.__comments +\
            self.__dimension +\
            self.__edge_weight_type,
            "\bNodes: ",
            end=''
        )
        for nodes in self.__nodes:
            print(nodes)
        return ''

    def set(self,**kwargs):
        self.__name = kwargs.get('name')
        self.__time_allowed = kwargs.get('time_allowed')
        self.__comments = kwargs.get('comments')
        self.__type = kwargs.get('type_')
        self.__dimension = kwargs.get('dimension')
        self.__edge_weight_type = kwargs.get('edge_weight_type')

    def add_node(self,a,b,c):
        self.__nodes.append([a,b,c])