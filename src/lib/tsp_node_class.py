class TSP_NODE(object):
    def __init__(self,**kwargs):
        self.__name = kwargs.get('name')
        self.__comments = kwargs.get('comments')
        self.__type = kwargs.get("_type_")
        self.__dimension = kwargs.get('dimension')
        self.__edge_weight_type = kwargs.get('ewt')
        self.__nodes = []
     
    def add_node(self,a,b,c):
        self.__nodes.append([a,b,c])
    
    def get_nodes(self):
        return self.__nodes

    def get_name(self):
        return self.__name
    
    def get_comments(self):
        return self.__comments
    
    def get_type(self):
        return self.__type
   
    def get_dimension(self):
        return self.__dimension
    
    def get_edge_weight_type(self):
        return self.__edge_weight_type