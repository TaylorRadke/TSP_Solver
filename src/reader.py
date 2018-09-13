import re
import sys
from queries import *
import mysql.connector
from mysql.connector.errors import Error

def reader(problem_file,problem_name,db_conn):
    cur = db_conn.cursor()

    #  Check if problem already exists
    try:
        tsp_nodes = open(problem_file,"r")
    except:
        print(problem_name + ".tsp does not exist")
        sys.exit(1)

    current_line = 1
    for  line in tsp_nodes.readlines():
        a = re.match("(\w+)\s*:*\s*([\w]*)",line)
        attr_label = a.group(1)
        attr_value = a.group(2)
        current_line += 1

        if attr_label == "NODE_COORD_SECTION":
            break
        elif attr_label == "DIMENSION":
            dimension = int(attr_value)   

    tsp_nodes.close()


    with open(problem_file,"r") as tsp_nodes:
        count = 0
        try:
            print("Adding " + problem_name +" to database")
            cur.execute(sql_add_problem.format(problem_name,dimension))
            

            for node in tsp_nodes.readlines()[current_line-1:-1]:
                node_list = list(filter(None,node.strip().replace("\n","").split(" ")))
                print("Adding nodes for " + problem_name + ": {}/{}".format(count,dimension),end="\r",flush=True)
                count += 1
                node = node_list[0]
                x = node_list[1]
                y = node_list[2]
                try:
                    cur.execute(sql_add_node.format(problem_name,node,x,y))
                except KeyboardInterrupt:
                    print("Unexpected interrupt while adding nodes to database")
                    sys.exit(1)
                except mysql.connector.IntegrityError:
                    pass
            db_conn.commit()
            print(problem_name + " has been successfully added to the database")

        except mysql.connector.IntegrityError:
            print("Duplicate Entry: problem %s is already in the database" % problem_name)
