import re
import mysql.connector

def reader(problem_file,problem_name,db_conn):
    cur = db_conn.cursor()

    tsp_nodes = open(problem_file,"r")

    current_line = 1
    for  line in tsp_nodes.readlines():
        a = re.match("(\w+)\s*:*\s*([\w]*)",line)
        attr_label = a.group(1)
        attr_value = a.group(2)
        current_line += 1

        if attr_label == "NODE_COORD_SECTION":
            break   

    tsp_nodes.close()

    sql_add_node = """
    INSERT INTO Nodes (Name,ID,x,y) Values ('{}',{},{},{});
    """

    with open(problem_file,"r") as tsp_nodes:
        for node in tsp_nodes.readlines()[current_line-1:-1]:
            node_list = list(filter(None,node.strip().replace("\n","").split(" ")))

            node = node_list[0]
            x = node_list[1]
            y = node_list[2]

            try:
                 cur.execute(sql_add_node.format(problem_name,node,x,y))
                 db_conn.commit()
            except mysql.connector.errors.DataError as e:
                raise "Something went wrong " + e

    db_conn.close()
